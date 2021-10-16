# 目录


## 说明

1. 用法

Jupyter （Jupyter Notebook 或者 Jupyter Lab）适合交互式编程，就是敲一行或多行代码看看有什么结果，然后继续下一个步骤。或者结合 Markdown 格式，做一个代码和结果的混合呈现。

我个人把它作为一个“草稿本”，做一些推演工作。完成之后的工作（程序片段）整理为适合连续运行的纯 Python 版本，归纳到 src 目录下。

2. 定位（文件系统）

涉及到数据就免不了和文件系统打交道，涉及到文件的读取、写入等操作。但是项目托管在平台上，落地到本机的时候不能确定具体的文件路径，比如到底是在 D:\ 还是在 E:\Investment。唯一可靠的就是在编写时确定的项目结构。本项目中的文件全部采用相对路径，依赖于 Jupyter 的 .ipynb 文件来定位（即每个 .ipynb 开头第一个格子内的代码）。

3. 依赖库

依赖库详见各子目录下的 **requirement.txt**。

通过 `pip install requirement.txt` 安装（注意 requirement.txt 的路径）。


## 开发环境搭建

- [开发环境搭建](development_environment/development_environment.md)


## 获取交易所历史数据

- [获取中金所历史数据](collect_data/download_cffex_history_data.ipynb)

- [解压缩zip文件](collect_data/uncompress_zip_file.ipynb)

- [读取中金所历史数据](collect_data/read_cffex_history_data.ipynb)

- [写入数据库](collect_data/save_to_database.ipynb)

- [完整的流程](collect_data/completed_flow.ipynb)

- [获取上期所历史数据](collect_data/download_shfe_history_data.ipynb)

- [获取郑商所历史数据](collect_data/download_czce_history_data.ipynb)

- [获取大商所历史数据](collect_data/download_dce_history_data.ipynb)

## 获取交易所其它数据

## 获取 Tick 数据

## 图表

## 指标

## 回测
