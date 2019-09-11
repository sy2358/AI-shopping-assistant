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

top_list = ['blouse', 'shirt', 'sweater', 't-shirt', 'top']
pants_list = ['dress', 'jeans', 'pants', 'shorts', 'skirt']
outer_list = ['blazer', 'coat', 'jacket', 'suit', 'vest']
shoes_list = ['boots', 'heels', 'sandals', 'shoes']

class_list = [top_list, pants_list, outer_list, shoes_list]
class_name = ['top', 'pants', 'outer', 'shoes']

for idx in range(len(class_list)):
    zip_list = []
    label_dict = {}
    if not os.path.exists('zipfile_class/' + class_name[idx]):
        os.makedirs('zipfile_class/' + class_name[idx])

    for i in range(len(class_list[idx])):
        label_dict[class_list[idx][i]] = i
        zip_list.append(zipfile.ZipFile('zipfile_class/' + class_name[idx] + '/'
                                        + class_list[idx][i] + '.zip', 'w'))
    zip_list.append(zipfile.ZipFile('zipfile_class/' + class_name[idx] + '/other.zip', 'w'))

    f = open('tags_training.csv', 'rb')
    rdr = csv.reader(f)
    for line in rdr:
        number = line[0]
        # print number
        counter = [0, 0, 0, 0, 0]
        for i in range(1, len(line)):
            label = line[i]
            if label in class_list[idx]:
                counter[label_dict[label]] = 1
        if sum(counter) == 0:
            zip_list[len(class_list[idx])].write('photos/%04d.jpg' % int(number), '%04d.jpg' % int(number),
                                            compress_type=zipfile.ZIP_DEFLATED)
        elif sum(counter) == 1:
            zip_list[counter.index(1)].write('photos/%04d.jpg' % int(number), '%04d.jpg' % int(number),
                                                 compress_type=zipfile.ZIP_DEFLATED)
        else:
            print class_name[idx], number
    f.close()

    for i in range(len(zip_list)):
        zip_list[i].close()
