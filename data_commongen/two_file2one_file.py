
import numpy as np

train_src = 'valid.src'
train_tgt = 'valid.tgt'
target_file = 'fra_eng.valid'
# target_file = 'fra_eng.dev'

with open(train_src, "r", encoding="utf-8") as f:
    source_text = f.read().split('\n')
# French target data
with open(train_tgt, "r", encoding="utf-8") as f:
    target_text = f.read().split('\n')
with open(target_file, "w", encoding="utf-8") as f:
    for i in range(len(source_text)-1):
        tmp = source_text[i].replace('\t', '.') + '\t' + target_text[i]
        f.write(tmp)
        f.write('\n')
