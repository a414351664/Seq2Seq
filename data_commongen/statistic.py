
import numpy as np
from tqdm import tqdm

train_src = './valid.src'
train_tgt = './valid.tgt'

len_sum = []
with open(train_src, 'r', encoding='utf-8') as infile:
    for line in tqdm(infile, desc="Load Data: "):
        subs = line.strip().split('\t')
        len_sample = len(subs[0].split(' ')) + len(subs[1].split(' '))
        len_sum.append(len_sample)
print('avg, ', np.mean(len_sum))
print('avg, ', np.percentile(len_sum, 95))
