# 目录


## 说明

1. 定位

涉及到数据就免不了和文件系统打交道，涉及到文件的读取、写入等操作。但是项目托管在平台上，落地到本机的时候不能确定具体的文件路径，比如到底是在 D:\ 还是在 E:\Investment。唯一可靠的就是在编写时确定的项目结构。本项目中的文件全部采用相对路径，依赖于 Jupyter 的 .ipynb 文件来定位（即每个 .ipynb 开头第一个格子内的代码）。

2. 依赖库

需要使用到的第三方库：

- requests

- lxml

- lxrd

- openpyxl

- peewee

- pandas

## 开发环境搭建

- [开发环境搭建](development_environment.md)

## 获取交易所历史数据

- [获取中金所历史数据](collect_data\download_cffex_history_data.ipynb)

- [处理zip压缩文件](collect_data\process_zip_files.ipynb)

- [读取中金所历史数据](collect_data\read_cffex_history_data.ipynb)

- [写入数据库](collect_data\save_to_database.ipynb)

- [获取上期所历史数据](collect_data\download_shfe_history_data.ipynb)

- [获取郑商所历史数据](collect_data\download_czce_history_data.ipynb)

- [获取大商所历史数据](collect_data\download_dce_history_data.ipynb)

## 获取交易所其它数据

## 获取 Tick 数据

## 图表

## 指标

## 回测
