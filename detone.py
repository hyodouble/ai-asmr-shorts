"""Remove tonal (bell/chime) components from ASMR clip audio, keep broadband crackle.

Median-filter HPSS: in a spectrogram a bell is a horizontal ridge (steady pitch over
time), a crackle is a vertical ridge (broadband, instant). Median over time estimates
the tonal part, median over frequency the percussive part; a Wiener mask keeps the
percussive part only.
"""
import sys, wave, numpy as np
from numpy.lib.stride_tricks import sliding_window_view

N, H = 2048, 512
KT, KF = 31, 31          # median kernel: 0.33 s over time, 730 Hz over frequency
PEAK_CEIL = 4.0          # a bin may exceed its frequency-neighbourhood median by 12 dB
KEEP_TONAL = 0.02        # -34 dB bleed: enough to keep it from sounding gated

def med(a, k, axis):
    pad = [(0, 0), (0, 0)]
    pad[axis] = (k // 2, k // 2)
    return np.median(sliding_window_view(np.pad(a, pad, mode='edge'), k, axis=axis), axis=-1)

def main(src, dst):
    w = wave.open(src)
    sr, ch = w.getframerate(), w.getnchannels()
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float64) / 32768
    x = x.reshape(-1, ch)

    out = []
    for c in range(ch):
        s = x[:, c]
        pad = (-(len(s) - N) % H) + N
        s = np.concatenate([s, np.zeros(pad)])
        win = np.hanning(N)
        idx = range(0, len(s) - N, H)
        X = np.array([np.fft.rfft(s[i:i + N] * win) for i in idx])
        S = np.abs(X)
        Ht, Pf = med(S, KT, 0), med(S, KF, 1)
        mask = Pf**2 / (Pf**2 + Ht**2 + 1e-12)
        Y = X * (mask + KEEP_TONAL * (1 - mask))
        # Short dings survive the HPSS mask (too brief to read as "sustained"), so also
        # flatten any bin that sticks far above its own frequency neighbourhood: a crackle
        # is broadband and sits near the local median, a bell partial is a single spike.
        S2 = np.abs(Y)
        Pf2 = med(S2, KF, 1)
        Y *= np.minimum(1.0, Pf2 * PEAK_CEIL / (S2 + 1e-12))

        y = np.zeros(len(s)); wsum = np.zeros(len(s))
        for j, i in enumerate(idx):
            y[i:i + N] += np.fft.irfft(Y[j]) * win
            wsum[i:i + N] += win**2
        out.append((y / np.maximum(wsum, 1e-9))[:x.shape[0]])

    y = np.stack(out, 1)
    y = np.clip(y, -1, 1)
    o = wave.open(dst, 'w'); o.setnchannels(ch); o.setsampwidth(2); o.setframerate(sr)
    o.writeframes((y * 32767).astype('<i2').tobytes()); o.close()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
