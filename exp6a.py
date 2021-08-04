import numpy as np
import matplotlib.pyplot as plt
s=np.random.normal(0,1,10000)
count,bins,ignored=plt.hist(s,100,density=True)
plt.plot(bins,np.ones_like(bins),linewidth=2,color='r')
plt.show()
sig=np.repeat([-1.,-1.,1.,-1.,1.,-1.,-1.,1.],128)
sig_noise=sig+np.random.normal(0,50,len(sig))
#correleation with recantangular pulse
corr=np.correlate(sig_noise, np.ones(128), mode='same')/128
clock=np.arange(64, len(sig), 128)
clock==np.arange(64,len(sig),128)
fig, (ax_orig, ax_noise, ax_corr) = plt.subplots(3, 1, sharex=True)
ax_orig.plot(sig)
ax_orig.plot(clock,sig[clock], 'ro')
ax_orig.set_title('Original signal')
ax_noise.plot(sig_noise)
ax_noise.set_title('Signal with noise')
ax_corr.plot(corr)
ax_corr.plot(clock,corr[clock], 'ro')
ax_corr.axhline(0.5,ls='--')
ax_corr.set_title('Cross-correlated with rectangular pulse')
ax_orig.margins(0,0.1)
fig.tight_layout()
fig.show()