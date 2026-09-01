import sys, wave, numpy as np
w=wave.open(sys.argv[1]); sr=w.getframerate(); ch=w.getnchannels()
x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
x=x.reshape(-1,ch).mean(1)
N,H=4096,1024; win=np.hanning(N)
hits=0; worst=0
for i in range(0,len(x)-N,H):
    row=20*np.log10(np.abs(np.fft.rfft(x[i:i+N]*win))+1e-12)
    f=np.fft.rfftfreq(N,1/sr); k=int(np.argmax(row)); prom=row[k]-np.median(row)
    if prom>34 and f[k]>500:
        hits+=1; worst=max(worst,prom)
print(f"{sys.argv[1]}: tonal frames {hits}, worst prominence {worst:.1f} dB")
