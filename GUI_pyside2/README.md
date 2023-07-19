# 👇GUI界面部分

## 启动系统界面脚本（假设相关依赖已安装）：
```bash
python login.py
```


## 项目文件说明

```
GUI_pyside2/
    images/     # 文件夹：界面的一些图片素材
        cab.ico
        image.jpg
        ...
        
    pytorch/     # 文件夹：模型预测相关
        testimages/     # 文件夹：待预测图片
        cat.png
        cifar10_net_02.py       # 自定义网络结构
        model.pth       # 模型权重文件
        predict_img.py  # 预测图片脚本
        testvideo.mp4   # 待预测视频
    
    CloudAPI.py     # 腾讯云对象存储接口
    
    forgetpwd.py    # 忘记密码界面
    
    login.py        # 登陆界面（系统启动界面）
    
    main.py         # 预测主界面
    
    need.prc        # 需要的资源文件
    
    needs_rs.py     # 需要的资源文件
    
    README.md       # 介绍
    
    regist.py       # 注册界面
    
    Ui_Forgetpwd.py # 忘记密码界面py文件
    
    Ui_Forgetpwd.ui # 忘记密码界面ui文件
    
    Ui_Login.py     # 登陆界面py文件
    
    Ui_Login.ui     # 登陆界面ui文件
    
    Ui_Main.py      # 预测主界面py文件
    
    Ui_Main.ui      # 预测主界面ui文件
    
    Ui_Regist.py    # 注册界面py文件
    
    Ui_Regist.ui    # 注册界面ui文件
```