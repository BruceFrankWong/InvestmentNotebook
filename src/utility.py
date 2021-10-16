# -*- coding: utf-8 -*-

__author__ = 'Bruce Frank Wong'


from typing import Dict, List, Any, Optional
import os
from pathlib import Path
import json


def load_json(json_file: Path) -> dict:
    """
    加载 json 文件为 dict。
    :param json_file: Path，json 文件的路径。
    :return: dict.
    """
    with open(json_file, mode='r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def save_json(json_file: Path, data: dict) -> None:
    """
    将字典保存为 json 文件。
    :param json_file: Path，json 文件的路径。
    :param data: dict，要保存的数据。
    :return: None
    """
    with open(json_file, mode='w+', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def create_default_config() -> None:
    """
    创建默认的配置文件。
    :return: None
    """
    default_config: Dict[str, Any] = {
        'database': {
            'driver': 'SQLite',
            'database': 'investment.sqlite',
            # 以下项对 SQLite 无效，保留在这里将会写入配置文件，方便以后手工修改。
            'host': '127.0.0.1',
            'port': '5432',
            'user': 'user',
            'password': 'password',
        }
    }
    save_json(CONFIG_FILE, default_config)


def is_run_in_jupyter() -> bool:
    """
    是否运行在 Jupyter 环境中。
    :return: bool，如果运行在 Jupyter 环境中返回 True，反之返回 False。
    """
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter


def clean_directory(directory: Path, file_type: List[str]):
    """
    删除指定文件夹下的指定扩展名的文件。
    :param directory: Path，要清理的目录。
    :param file_type: List[str]，内容是文件扩展名（包括 . ）。
    :return: None
    """
    for item in directory.iterdir():
        if item.suffix in file_type:
            item.unlink()


# JupyterLab 运行时的路径。
NOTEBOOK_PATH: Optional[Path] = Path(os.path.abspath('')) if is_run_in_jupyter() else None

# 定义项目文件夹路径。
PACKAGE_PATH: Path = Path(__file__).parent

# 定义配置文件夹路径。
CONFIG_PATH: Path = Path.home().joinpath(f'.investment')

# 如果配置文件夹不存在，创建它。
if not CONFIG_PATH.exists():
    CONFIG_PATH.mkdir()

# 定义配置文件路径。
CONFIG_FILE: Path = CONFIG_PATH.joinpath('config.json')

# 如果配置文件不存在，创建默认的版本。
if not CONFIG_FILE.exists():
    create_default_config()

# 读取配置文件。
CONFIGS: Dict[str, Any] = load_json(CONFIG_FILE)