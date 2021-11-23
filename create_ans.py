import os
import cv2
import json

filepath = 'runs/detect/exp/labels/'
data_listdir = os.listdir(filepath)

data = []
for img_name in data_listdir:
    image_id = int(img_name[:-4])
    print(image_id)

    if not os.path.isfile(filepath+str(image_id)+'.txt'):
        a = {"image_id": image_id,
             "score": 0.5,
             "category_id": 0,
             "bbox": (1, 1, 1, 1)}
        data.append(a)
    else:
        f = open(filepath+str(image_id)+'.txt', 'r')
        contents = f.readlines()
        img_name = str(image_id) + '.png'
        im = cv2.imread('data/svhn/test/'+img_name)
        h, w, c = im.shape

        for content in contents:
            a = {}
            content = content.replace('\n', '')
            c = content.split(' ')
            a['image_id'] = (image_id)
            a['score'] = (float(c[5]))
            a['category_id'] = (int(c[0]))
            w_center = w*float(c[1])
            h_center = h*float(c[2])
            width = w*float(c[3])
            height = h*float(c[4])

            left = float(w_center - width/2)
            top = float(h_center - height/2)

            # A list ( [left_x, top_y, width, height] )
            a['bbox'] = (tuple((left, top, width, height)))

            print(a)
            data.append(a)
        f.close()
ret = json.dumps(data, indent=4)

print(len(data))
with open('answer.json', 'w') as fp:
    fp.write(ret)
