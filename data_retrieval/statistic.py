
import numpy as np


statistics_path = './statistic/statis_dev_30k.npy'
save_fig_path = './statistic/'
fig_name = 'statis_dev_mi_30k.pdf'
data = np.load(statistics_path)
y_ = []
for i in range(0, len(data), 2):
    y_.append(data[i] - data[i+1])
x = range(len(y_))
n, bins, patches = plt.hist(y_)
# plt.plot(x, y_)
plt.savefig(save_fig_path+fig_name, bbox_inches='tight')
plt.show()


# plt.savefig(save_fig_path+fig_name, format="svg")

