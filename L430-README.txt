#########历史核心区街景语义分割#############
注：本项目是基于mmsegmentation项目的基础上更改得到的，运行本代码需要先安装mmsegmentation

训练集位于data文件夹下，核心区街景数据集为l430sv
参数设置文件位于configs文件夹内
本项目目前训练并使用了FCN、PSANet、ANNN、DeepLabV3+和Fast-SCNN五种网络，
训练设置文件后缀_l430sv，预训练参数保存至checkpoints文件夹，训练后模型参数保存于工作文件夹work_dirs中
使用tools/train.py和tools/test.py进行训练和测试，
训练后可使用tools/analyze_logs.py绘制训练过程中的loss曲线及metric曲线
已有可视化输出结果位于testdata文件夹中，大量图片可视化时可用testimg_multi.py

另注：主要参数更改位于configs文件夹内网络子文件夹中，如有任何疑问及优化建议欢迎随时联系
                         
                         ——尹思铭，联系方式：13683183127，或siming_yin@hotmail.com