# 👇模型训练部分
## 项目文件说明
```
Cifar10/
    checkpoints/   # 文件夹：训练好的权重文件
        model.pth
        ...
    datasets/         # 文件夹：数据集
    
    models/          # 文件夹：模型文件
        cifar10_net_02.py   # 自定义CNN模型
        lenet.py            # LeNet模型
        mobilenetv2.py      # MobileNetV2模型
        pretrain_mobilenet.py   # MobileNetV2预训练模型
        pretrain_resnet.py      # ResNet预训练模型
        
    testimages/      # 文件夹：测试图片（网上搜集的）
    
    wandb/          # 文件夹：训练日志（含权重文件、训练过程acc、loss）
    
    cifar10_mean_std.py # 计算cifar10数据集的mean、std
    
    download_data.py # 下载cifar数据集
    
    hand_random_test_image.png # 数据增强后的测试集
    
    hand_random_train_image.png # 数据增强后的训练集
    
    load_data.py # 加载数据
    
    lr-test.py # 学习率策略测试代码
    
    main.py 
    
    predict_cap.py  # 预测摄像头
    
    predict_img.py # 预测图片
    
    predict_video.py # 预测视频
    
    print_color.py  # 打印颜色字体
    
    random_test_image.png # 原始测试集
    
    random_train_image.png # 原始训练集
    
    README.md # 介绍
    
    requirements.txt # 依赖库
    
    show_dataset.py # 可视化数据集
    
    temp.py # 临时文件
    
    testvideo.mp4   # 测试视频
    
    train.py # 训练代码
    
    train_cap.py # 训练摄像头
```