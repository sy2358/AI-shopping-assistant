import os
import zipfile
import csv

label_list = ['accessories', 'bag', 'belt', 'blazer', 'blouse', 'bodysuit', 'boots', 'bra',
              'bracelet', 'cape', 'cardigan', 'clogs', 'coat', 'dress', 'earrings', 'flats',
              'glasses', 'gloves', 'hair', 'hat', 'heels', 'hoodie', 'intimate', 'jacket', 'jeans',
              'jumper', 'leggings', 'loafers', 'necklace', 'panties', 'pants', 'pumps', 'purse',
              'ring', 'romper', 'sandals', 'scarf', 'shirt', 'shoes', 'shorts', 'skin', 'skirt',
              'sneakers', 'socks', 'stockings', 'suit', 'sunglasses', 'sweater', 'sweatshirt',
              'swimwear', 't-shirt', 'tie', 'tights', 'top', 'vest', 'wallet', 'watch', 'wedges']

zip_list = []
label_dict = {}

for i in range(len(label_list)):
    label_dict[label_list[i]] = i
    zip_list.append(zipfile.ZipFile('zipfiles/' + label_list[i] + '.zip', 'w'))

f = open('tags.csv', 'rb')
rdr = csv.reader(f)
for line in rdr:
    number = line[0]
    print number
    for i in range(1, len(line)):
        label = line[i]
        if label == '':
            print number, "============================"
            continue
        zip_list[label_dict[label]].write('photos/%04d.jpg' % int(number), '%04d.jpg' % int(number), compress_type=zipfile.ZIP_DEFLATED)
f.close()

for i in range(len(zip_list)):
    zip_list[i].close()

# f = open('tags.csv', 'r', encoding='utf-8')
# rdr = csv.reader(f)
# for line in rdr:
#     number = line[0]
#     for i in range(1, len(line)):
#         label = line[i]
#
# for label in label_list:
#     img_list = []
#     label_zip = zipfile.ZipFile(label + '.zip', 'w')
#     for img in img_list:
#         label_zip.write('photos/%04d.jpg' % int(img), compress_type=zipfile.ZIP_DEFLATED)
#     label_zip.close()