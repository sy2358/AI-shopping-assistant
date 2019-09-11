import os
import zipfile
import csv
import numpy as np

label_list = ['accessories', 'bag', 'belt', 'blazer', 'blouse', 'bodysuit', 'boots', 'bra',
              'bracelet', 'cape', 'cardigan', 'clogs', 'coat', 'dress', 'earrings', 'flats',
              'glasses', 'gloves', 'hair', 'hat', 'heels', 'hoodie', 'intimate', 'jacket', 'jeans',
              'jumper', 'leggings', 'loafers', 'necklace', 'panties', 'pants', 'pumps', 'purse',
              'ring', 'romper', 'sandals', 'scarf', 'shirt', 'shoes', 'shorts', 'skin', 'skirt',
              'sneakers', 'socks', 'stockings', 'suit', 'sunglasses', 'sweater', 'sweatshirt',
              'swimwear', 't-shirt', 'tie', 'tights', 'top', 'vest', 'wallet', 'watch', 'wedges']

notags = ['intimate', 'panties', 'swimwear']

label_dict = {}
l = len(label_list)
tag_counter = np.zeros(l).tolist()

for i in range(l):
    label_dict[label_list[i]] = i

f = open('tags.csv', 'rb')
rdr = csv.reader(f)
for line in rdr:
    number = line[0]
    print number
    for i in range(1, len(line)):
        tag_counter[label_dict[line[i]]] += 1
f.close()

for idx in range(l):
    print label_list[idx], ',', tag_counter[idx]