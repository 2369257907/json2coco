import json
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# 读取标签文件
with open('train.json', 'r') as f:
    label_data = json.load(f)

# 遍历每张图像的注释
for annotation in label_data['annotations']:
    image_id = annotation['image_id']
    image_info = next(image for image in label_data['images'] if image['id'] == image_id)

    # 读取图像文件
    image_file = r'C:\Users\Administrator\PycharmProjects\json2coco\json_dataset\\' + image_info['file_name']
    image = plt.imread(image_file)

    # 显示图像
    plt.imshow(image)
    ax = plt.gca()

    # 绘制包围框
    bbox = annotation['bbox']
    rect = Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], linewidth=2, edgecolor='r', facecolor='none')
    ax.add_patch(rect)

    # 绘制关节点
    keypoints = annotation['keypoints']
    print("Keypoints length:", len(keypoints))  # 调试语句，输出关节点列表的长度
    x = keypoints[0::3]
    y = keypoints[1::3]
    v = keypoints[2::3]

    # 按既定骨架连接关节点
    skeleton = next(category['skeleton'] for category in label_data['categories'] if category['id'] == annotation['category_id'])
    for sk in skeleton:
        if v[sk[0] - 1] > 0 and v[sk[1] - 1] > 0:
            ax.plot([x[sk[0] - 1], x[sk[1] - 1]], [y[sk[0] - 1], y[sk[1] - 1]], marker='o', markersize=6, linewidth=2,
                    color='r')

    # 设置图像标题
    category_name = next(category['name'] for category in label_data['categories'] if category['id'] == annotation['category_id'])
    plt.title('Image ID: {}, Category: {}'.format(image_id, category_name))

    # 显示图像
    plt.show()