import matplotlib.pyplot as plt
from matplotlib import gridspec

fig = plt.figure(figsize=(18,18))

gs = gridspec.GridSpec(3, 3)

ax1 = fig.add_subplot(gs[0,:])
ax1.plot([1,2,3,4,5], [10,5,10,5,10], 'r-')

ax2 = fig.add_subplot(gs[1,:-1])
ax2.plot([1,2,3,4], [1,4,9,16], 'k-')

ax3 = fig.add_subplot(gs[1:, 2])
ax3.plot([1,2,3,4], [1,10,100,1000], 'b-')

ax4 = fig.add_subplot(gs[2,0])
ax4.plot([1,2,3,4], [0,0,1,1], 'g-')

ax5 = fig.add_subplot(gs[2,1])
ax5.plot([1,2,3,4], [1,0,0,1], 'c-')

gs.update(wspace=0.5, hspace=0.5)

plt.show()