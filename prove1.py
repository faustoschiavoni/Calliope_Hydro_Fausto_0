import random
import matplotlib.pyplot as plt


nrows = 2
ncols = 4
fig2, axes = plt.subplots(nrows=nrows, ncols=ncols, constrained_layout=True)
r_hex = (lambda: random.randint(0, 255))


dicto = {'y': random.randint(1, 9), 'color': '#%02X%02X%02X' % (r_hex(), r_hex(), r_hex()), 'linestyle': '--',
         'label': 'Storage_cap_max'}
gino = []
for ii in range(4):
    axes.flatten()[ii].axhline(**dicto)
    axes.flatten()[ii].axhline(y=random.randint(1, 9), color='#%02X%02X%02X' % (r_hex(), r_hex(), r_hex()),
                                           linestyle='-', label='Spillagesd')

ginone = []
for tt in range(4, 8):
    axes.flatten()[tt].axhline(y=random.randint(1, 9), color='#%02X%02X%02X' % (r_hex(), r_hex(), r_hex()),
                                             linestyle='-', label='Gino')
    axes.flatten()[tt].axhline(y=random.randint(1, 9), color='#%02X%02X%02X' % (r_hex(), r_hex(), r_hex()),
                                             linestyle='-', label='Geeeeeno')


plt.show()
plt.close()
