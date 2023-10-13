这个脚本可以将人体姿态识别数据集从json(每张图片对应一张json)格式转换成主流的MS COCO，供你在mmpose等主流姿态检测模型中使用。

### 1、格式转换
运行：
```bash
python json2coco.py
```
将普通json格式转换为MS COCO格式
### 2、标注可视化
运行：
```bash
python visualize_pose.py
```
将train.json标签对应的图片的标注可视化

![image](https://github.com/2369257907/json2coco/assets/67651900/e680a8bf-d06b-408e-9b20-4f6f8738ba79)
