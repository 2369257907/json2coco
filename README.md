# json2coco
这个脚本可以将人体姿态识别数据集从json(每张图片对应一张json)格式转换成主流的MS COCO，供你在mmpose等主流姿态检测模型中使用。


##

运行
python json2coco.py
将json转为MS COCO格式，转换后的标签文件为train.json

运行
python visualize_pose.py
将train.json标签对应的图片的标注可视化

![Uploading image.png…]()

