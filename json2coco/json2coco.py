import os
import json
from PIL import Image

input_dir = r'json_dataset'  #替换成数据集的路径
output_file = 'train.json'
categories = [
    {
        "supercategory": "human",
        "id": 1,
        "name": "up",
        "keypoints": [
            "head",
            "nose",
            "neck",
            "left shoulder",
            "right shoulder",
            "left elbow",
            "right elbow",
            "left wrist",
            "right wrist",
            "torso",
            "pelvis",
            "left hip",
            "right hip",
            "left knee",
            "right knee",
            "left ankle",
            "right ankle"
        ],
        "skeleton": [[11, 13], [13, 15], [15, 17],[14, 15],[16, 17],
            [5, 7], [7, 9], [3, 10], [10, 11], [11, 12], [12, 14], [14, 16],
            [1, 2], [2, 3], [3, 4], [4, 6], [6, 8], [3, 5]]
    },
    {
        "supercategory": "human",
        "id": 2,
        "name": "down",
        "keypoints": [
            "head",
            "nose",
            "neck",
            "left shoulder",
            "right shoulder",
            "left elbow",
            "right elbow",
            "left wrist",
            "right wrist",
            "torso",
            "pelvis",
            "left hip",
            "right hip",
            "left knee",
            "right knee",
            "left ankle",
            "right ankle"
        ],
        "skeleton": [[11, 13], [13, 15], [15, 17],[14, 15],[16, 17],
            [5, 7], [7, 9], [3, 10], [10, 11], [11, 12], [12, 14], [14, 16],
            [1, 2], [2, 3], [3, 4], [4, 6], [6, 8], [3, 5]]
    },
    {
        "supercategory": "human",
        "id": 3,
        "name": "shake",
        "keypoints": [
            "head",
            "nose",
            "neck",
            "left shoulder",
            "right shoulder",
            "left elbow",
            "right elbow",
            "left wrist",
            "right wrist",
            "torso",
            "pelvis",
            "left hip",
            "right hip",
            "left knee",
            "right knee",
            "left ankle",
            "right ankle"
        ],
        "skeleton": [[11, 13], [13, 15], [15, 17],[14, 15],[16, 17],
            [5, 7], [7, 9], [3, 10], [10, 11], [11, 12], [12, 14], [14, 16],
            [1, 2], [2, 3], [3, 4], [4, 6], [6, 8], [3, 5]]
    },
    {
        "supercategory": "human",
        "id": 4,
        "name": "sit",
        "keypoints": [
            "head",
            "nose",
            "neck",
            "left shoulder",
            "right shoulder",
            "left elbow",
            "right elbow",
            "left wrist",
            "right wrist",
            "torso",
            "pelvis",
            "left hip",
            "right hip",
            "left knee",
            "right knee",
            "left ankle",
            "right ankle"
        ],
        "skeleton": [[11, 13], [13, 15], [15, 17],[14, 15],[16, 17],
            [5, 7], [7, 9], [3, 10], [10, 11], [11, 12], [12, 14], [14, 16],
            [1, 2], [2, 3], [3, 4], [4, 6], [6, 8], [3, 5]]
    }
]
data = []
image_id_counter = 1
coco_images = []
coco_annotations=[]
annotation_id_counter = 1

# 遍历目录下的所有jpg文件
for file_name in os.listdir(input_dir):
    if file_name.endswith('.jpg'):
        jpg_file = os.path.join(input_dir, file_name)
        json_file = os.path.join(input_dir, file_name.replace('.jpg', '.json'))

        # 读取json文件中的内容
        with open(json_file, 'r') as f:
            json_data = json.load(f)

        # 提取所需的信息
        annotations = json_data['data']
        image_id = image_id_counter
        image_id_counter += 1

        # 获取图像宽度和高度
        image_path = os.path.join(input_dir, file_name)
        image_width, image_height = 0, 0
        if os.path.exists(image_path):
            with Image.open(image_path) as image:
                image_width, image_height = image.size

        # 构造图像信息
        image_info = {
            'id': image_id,
            'file_name': file_name,
            'height': image_height,
            'width': image_width
        }

        print(coco_images)
        coco_images.append(image_info)


        for annotation in annotations:
            category_id = annotation['rect']['groupId']
            keypoints = [0] * len(categories[category_id - 1]['keypoints']) * 3
            group_name = annotation['rect']['groupName']

            # 从rect中读取x1, x2, y1, y2并计算bbox的坐标和宽度、高度
            x1 = annotation['rect']['x1']
            x2 = annotation['rect']['x2']
            y1 = annotation['rect']['y1']
            y2 = annotation['rect']['y2']
            bbox_width = x2 - x1
            bbox_height = y2 - y1

            # 构造bbox
            bbox = [x1, y1, bbox_width, bbox_height]


            # 设置关键点的坐标和可见性
            for i, key in enumerate(categories[category_id - 1]['keypoints']):
                pos = annotation[key]
                keypoints[i * 3] = pos['x']
                keypoints[i * 3 + 1] = pos['y']
                keypoints[i * 3 + 2] = 2  # 设置可见性为2，表示可见但未标注

            # 构造标注信息
            coco_annotation = {
                'id': annotation_id_counter,
                'image_id': image_id,
                'category_id': category_id,
                'keypoints': keypoints,
                'iscrowd': 0,
                'bbox': bbox,
                'area': bbox_width * bbox_height,
                'segmentation': []
            }
            annotation_id_counter += 1
            coco_annotations.append(coco_annotation)

        # 构造最终的mscoco格式数据
        mscoco_format = {
            'licenses': [],
            'info': {},
            'categories': categories,
            'images': coco_images,
            'annotations': coco_annotations
        }

        # 将数据保存为json文件
        with open(output_file, 'w') as f:
            json.dump(mscoco_format, f)

        print('转换完成！')