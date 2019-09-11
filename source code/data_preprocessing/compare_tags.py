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
label_coappearance = np.zeros((l,l)).tolist()

for i in range(l):
    label_dict[label_list[i]] = i

f = open('tags.csv', 'rb')
rdr = csv.reader(f)
for line in rdr:
    number = line[0]
    print number
    for i in range(1, len(line)):
        for j in range(i+1, len(line)):
            if label_dict[line[i]] < label_dict[line[j]]:
                label_coappearance[label_dict[line[i]]][label_dict[line[j]]] += 1
            else:
                label_coappearance[label_dict[line[j]]][label_dict[line[i]]] += 1
f.close()

print label_dict

fw = open('coappearance.csv', 'wb')
wtr = csv.writer(fw)
wtr.writerow([' '] + label_list)
for idx in range(l):
    wtr.writerow([label_list[idx]] + label_coappearance[idx])
fw.close()