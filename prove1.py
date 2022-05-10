import matplotlib.pyplot as plt
import random


# nrows = 2
# ncols = 4
# fig2, axes = plt.subplots(nrows=nrows, ncols=ncols, constrained_layout=True)
# r_hex = (lambda: random.randint(0, 255))
#
# gino = []
# for ii in range(4):
#     gino.append(axes.flatten()[ii].axhline(y=random.randint(1, 9), color='#%02X%02X%02X' % (r_hex(), r_hex(), r_hex()),
#                                            linestyle='-', label='Storage_cap_max'))
#     gino.append(axes.flatten()[ii].axhline(y=random.randint(1, 9), color='#%02X%02X%02X' % (r_hex(), r_hex(), r_hex()),
#                                            linestyle='-', label='Spillagesd'))
#
# ginone = []
# for tt in range(4, 8):
#     ginone.append(axes.flatten()[tt].axhline(y=random.randint(1, 9), color='#%02X%02X%02X' % (r_hex(), r_hex(), r_hex()),
#                                              linestyle='-', label='Gino'))
#     ginone.append(axes.flatten()[tt].axhline(y=random.randint(1, 9), color='#%02X%02X%02X' % (r_hex(), r_hex(), r_hex()),
#                                              linestyle='-', label='Geeeeeno'))
#
# # plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
# # fig2.set_size_inches(9, 7)
# # lines = axes.get_lines()
#
#
# # lines = plt.gca().get_lines()
# # print(lines, *lines)
#
# legend1 = plt.legend(gino[:2], [ff.get_label() for ff in gino[:2]], bbox_to_anchor=(1.01, 1), loc="upper left")  # 'Storage_cap_max', 'Spillagesd'
# legend2 = plt.legend(ginone[:2], [fa.get_label() for fa in ginone[:2]], bbox_to_anchor=(1.01, 0.5), loc="upper left")
# plt.gca().add_artist(legend1)
#
# plt.show()
# plt.close()


nrows = 2
ncols = 4
fig2, axes = plt.subplots(nrows=nrows, ncols=ncols, constrained_layout=True)
r_hex = (lambda: random.randint(0, 255))

gino = []
for ii in range(4):
    gino.append(axes.flatten()[ii].axhline(y=random.randint(1, 9), color='#%02X%02X%02X' % (r_hex(), r_hex(), r_hex()),
                                           linestyle='-', label='Storage_cap_max'))
    gino.append(axes.flatten()[ii].axhline(y=random.randint(1, 9), color='#%02X%02X%02X' % (r_hex(), r_hex(), r_hex()),
                                           linestyle='-', label='Spillagesd'))

ginone = []
for tt in range(4, 8):
    ginone.append(axes.flatten()[tt].axhline(y=random.randint(1, 9), color='#%02X%02X%02X' % (r_hex(), r_hex(), r_hex()),
                                             linestyle='-', label='Gino'))
    ginone.append(axes.flatten()[tt].axhline(y=random.randint(1, 9), color='#%02X%02X%02X' % (r_hex(), r_hex(), r_hex()),
                                             linestyle='-', label='Geeeeeno'))

# legend1 = plt.legend(gino[:2], [ff.get_label() for ff in gino[:2]], bbox_to_anchor=(1.01, 1), loc="upper left")  # 'Storage_cap_max', 'Spillagesd'
# legend2 = plt.legend(ginone[:2], [fa.get_label() for fa in ginone[:2]], bbox_to_anchor=(1.01, 0.5), loc="upper left")
# plt.gca().add_artist(legend1)

# fig2.legend((*gino[:2], *ginone[:2]), (*[ff.get_label() for ff in gino[:2]], *[fa.get_label() for fa in ginone[:2]]), bbox_to_anchor=(1.01, 0.5), loc="upper left")
# fig2.legend((*gino[:2], *ginone[:2]), (*[ff.get_label() for ff in gino[:2]], *[fa.get_label() for fa in ginone[:2]]), bbox_to_anchor=(1.15, 0.6))

# fig2.legend(handles=[*gino[:2], *ginone[:2]], labels=[*[ff.get_label() for ff in gino[:2]], *[fa.get_label() for fa in ginone[:2]]],
#             loc='upper right')

# fig2.legend(handles=[*gino[:2]], labels=[*[ff.get_label() for ff in gino[:2]]], bbox_to_anchor=(1.01, 1), loc='upper right')
#
# fig2.legend(handles=[*ginone[:2]], labels=[*[ff.get_label() for ff in ginone[:2]]], bbox_to_anchor=(1.01, 1), loc='lower right')


legend1 = plt.legend(gino[:2], [ff.get_label() for ff in gino[:2]], bbox_to_anchor=(1.01, 2.1), loc="upper left")  # 'Storage_cap_max', 'Spillagesd'
legend2 = plt.legend(ginone[:2], [fa.get_label() for fa in ginone[:2]], bbox_to_anchor=(1.01, 0.97), loc="upper left")

fig2.add_artist(legend1, legend2)

plt.show()
plt.close()
