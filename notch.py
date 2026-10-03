"""Build time-gated notch chain from findtones output and write raw/sN_clean.wav."""
import subprocess, sys
from pathlib import Path
n = sys.argv[1]
out = subprocess.run(["python3", str(Path(__file__).with_name("findtones.py")), f"raw/s{n}.wav"], capture_output=True, text=True).stdout.split()
tones = [(int(out[i]), float(out[i + 1]), float(out[i + 2])) for i in range(0, len(out), 3)]
# merge same frequency (+-25 Hz) segments that overlap or sit within 0.5 s
tones.sort()
merged = []
for f, a, b in tones:
    if merged and abs(merged[-1][0] - f) <= 25 and a <= merged[-1][2] + 0.5:
        merged[-1][2] = max(merged[-1][2], b)
    else:
        merged.append([f, a, b])
# ponytail: fixed 0.4 s tail for bell decay, tune if rings leak
chain = ",".join(
    f"equalizer=f={f}:t=h:w={max(40, f // 40)}:g=-30:enable='between(t,{max(0, a - 0.05):.2f},{b + 0.4:.2f})'"
    for f, a, b in merged) or "anull"
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-i", f"raw/s{n}.wav", "-af", chain,
                "-c:a", "pcm_s16le", f"raw/s{n}_clean.wav", "-y"], check=True)
print(f"s{n}: {len(merged)} notches")
