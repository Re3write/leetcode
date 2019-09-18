import time

video_dict = {}

Type_List = ['mask', 'paint', 'style', 'erase', 'face', 'dance']

for type in Type_List:
    video_dict[type] = {}


def add(dict, type, id):
    dict[type][id] = ('name', time.time())


def get_list(dict, type, number=4):
    video_list = sorted(dict[type].items(), key=lambda x: x[1], reverse=True)
    id_list = [video[0] for video in video_list]
    if len(id_list) < number:
        return id_list
    else:
        return id_list[:number]


add(video_dict, 'mask', 1)
time.sleep(0.1)
add(video_dict, 'mask', 2)
time.sleep(0.1)
add(video_dict, 'mask', 3)
time.sleep(0.1)
add(video_dict, 'mask', 4)
time.sleep(0.1)
add(video_dict, 'mask', 5)
time.sleep(0.1)


print(get_list(video_dict,'mask'))
