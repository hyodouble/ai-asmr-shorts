"""List sustained narrow tones (chimes/bells) in a mono wav: freq, start, end.
A tone = a bin >= PROM dB above the local spectrum (+-300 Hz median) for >= MIN_DUR s."""
import sys, wave, numpy as np
PROM, MIN_DUR, FMIN, FMAX = 14.0, 0.12, 300, 9000
w = wave.open(sys.argv[1]); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
N, H = 4096, 512
win = np.hanning(N); f = np.fft.rfftfreq(N, 1 / sr); df = f[1]
k = int(300 / df)
rows = []
for i in range(0, len(x) - N, H):
    s = 20 * np.log10(np.abs(np.fft.rfft(x[i:i + N] * win)) + 1e-9)
    # local median via sliding window over frequency
    pad = np.pad(s, k, mode='edge')
    loc = np.array([np.median(pad[j:j + 2 * k + 1]) for j in range(0, len(s), 4)])
    loc = np.interp(np.arange(len(s)), np.arange(0, len(s), 4), loc)
    peak = (s - loc > PROM) & (s >= np.roll(s, 1)) & (s >= np.roll(s, -1)) & (f > FMIN) & (f < FMAX)
    rows.append(set(np.nonzero(peak)[0]))
# track bins (+-1) across frames
tones, active = [], {}
for t, bins in enumerate(rows + [set()]):
    nxt = {}
    for b in bins:
        src = next((a for a in (b, b - 1, b + 1) if a in active), None)
        nxt[b] = active.pop(src) if src is not None else t
    for b, t0 in active.items():
        if (t - t0) * H / sr >= MIN_DUR:
            tones.append((round(f[b]), round(t0 * H / sr, 2), round(t * H / sr + N / sr, 2)))
    active = nxt
for fr, a, b in sorted(tones, key=lambda z: z[1]):
    print(fr, a, b)
