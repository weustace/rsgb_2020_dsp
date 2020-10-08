import matplotlib.pyplot as plt
import numpy as np
import tqdm
fs=1000
x = np.linspace(0,10,fs*10)
y = np.sin(2*np.pi*10*x)
y = np.where(x<5,y,0)
fig,(ax1,ax2) = plt.subplots(2,1)

ax1.plot(x,y)

y_fs = []
for k in tqdm.tqdm(range(0,x.shape[0])):
    cur_val = 0
    for t in range(0,x.shape[0]):
        cur_val += np.exp(- 2*np.pi * t * 1j * k / x.shape[0]) * y[t]
    y_fs.append(cur_val)
ax2.plot(np.abs(y_fs))

plt.show()