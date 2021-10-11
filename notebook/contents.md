# 目录


## 目的

所有的研究，无论是基本面还是技术面，不仅仅是金融领域，都是从获取数据开始，再到总结出规律，最终为交易或者预测服务。

获取数据是一件很重要的事情。可能因为一个数据的变动，一个逻辑就反转了。

所以**数据来源一定要可靠**。

但是对于小投资者没有财力购买商业数据库，那么交易所官方数据就几乎是唯一的来源了。

交易所每天都公布交易数据，最新数据截至到最后一个结算完成的交易日。其中包括交易数据（量价信息，日线）、排名靠前的席位、仓单等等数据。

这些数据用人工下载非常消耗时间，我们可以写一个简单的爬虫来辅助处理。


## 说明

1. 定位

涉及到数据就免不了和文件系统打交道，涉及到文件的读取、写入等操作。但是项目托管在平台上，落地到本机的时候不能确定具体的文件路径，比如到底是在 D:\ 还是在 E:\Investment。唯一可靠的就是在编写时确定的项目结构。本项目中的文件全部采用相对路径，依赖于 Jupyter 的 .ipynb 文件来定位。

因此 .ipynb 文件中开头会有：

```
import os
from pathlib import Path

NOTEBOOK_PATH: Path = Path(
    os.path.abspath('')
)
```

这么一段，这就是用来定位的。其中：

```
os.path.abspath('')    # 定位 .ipynb 的路径。

Path()                 # 转换为 Path 对象。
```

如果不使用 Jupyter，那么该段内容可能发生变化。

2. 特殊文件夹

项目打包了一个文件夹 **RESULT/**，这个文件夹中只有一个文件，主要是担心新手克隆了整个项目到本地，但是没有创建该文件夹，结果本地运行出错。

3. 依赖库

需要使用到的第三方库：

- requests

- lxml

- lxrd

- pylxml

- peewee


## 从中金所开始

- [获取中金所历史数据](collect_data\download_cffex_history_data.ipynb)

- [处理zip压缩文件](collect_data\process_zip_files.ipynb)

- [读取中金所历史数据](collect_data\read_cffex_history_data.ipynb)

- [写入数据库](collect_data\save_to_database.ipynb)


## 获取其它交易所数据

- [获取上期所历史数据](collect_data\download_shfe_history_data.ipynb)

- [获取郑商所历史数据](collect_data\download_czce_history_data.ipynb)

- [获取大商所历史数据](collect_data\download_dce_history_data.ipynb)
