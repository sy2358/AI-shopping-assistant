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

binary_list = ['bag', 'hat', 'sunglasses']

zip_list = []
label_dict = {}
if not os.path.exists('zipfile_binary/'):
    os.makedirs('zipfile_binary/')

for tag in binary_list:
    # for i in range(len(label_list)):
    #     label_dict[label_list[i]] = i
    #     zip_list.append(zipfile.ZipFile('zipfiles/' + label_list[i] + '.zip', 'w'))
    zip_pos = zipfile.ZipFile('zipfile_binary/' + tag + '.zip', 'w')
    zip_neg = zipfile.ZipFile('zipfile_binary/no_' + tag + '.zip', 'w')

    f = open('tags_training.csv', 'rb')
    rdr = csv.reader(f)
    for line in rdr:
        number = line[0]
        print tag, number
        # for i in range(1, len(line)):
        #     label = line[i]
        #     if label == '':
        #         print number, "============================"
        #         continue
        #     zip_list[label_dict[label]].write('photos/%04d.jpg' % int(number), '%04d.jpg' % int(number), compress_type=zipfile.ZIP_DEFLATED)
        if tag in line:
            zip_pos.write('photos/%04d.jpg' % int(number), '%04d.jpg' % int(number), compress_type=zipfile.ZIP_DEFLATED)
        else:
            zip_neg.write('photos/%04d.jpg' % int(number), '%04d.jpg' % int(number), compress_type=zipfile.ZIP_DEFLATED)
    f.close()

    zip_pos.close()
    zip_neg.close()
