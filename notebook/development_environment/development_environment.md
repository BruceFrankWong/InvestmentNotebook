# 开发环境搭建

## Windows

基于 Windows 10 x64，因为 Python 3.9 起不再支持 Windows 7，且默认为 64 位。

1. 安装 Python

    [Python 官网](https://www.python.org/)，挑一个不那么新的版本（因为可能其它第三方库还没有更新）。

    本项目使用 [Python 3.8.9](https://www.python.org/ftp/python/3.8.9/python-3.8.9-amd64.exe) 编写。
      
    安装时最好自定义安装路径，安装到 C:\Python 之类比较简单的地方，以便于后续安装、使用的时候在 CMD 窗口输入路径。

2. 安装 Python 虚拟环境

    程序写的多了之后，就会遇到在同一台电脑上运行不同的程序：

        - 需要不同版本的 Python；
        - 相同版本的 Python，但是依赖库的版本不同；
        - 不希望把不同程序的依赖库混在一起。


    虚拟环境是用来处于这个目的，用来建立“软隔离”（硬隔离就是一台电脑一个程序，壕无人性）的工具。

    1. 安装 virtualenv
      
        ```
        pip install virtualenv
        ```
      
    2. 安装 virtualenvwrapper-win
      
        ```
        pip install virtualenvwrapper-win
        ```
      
    3. 配置 virtualenvwrapper-win
      
        默认情况下，新建的虚拟环境位于 C:\Users\<用户名>\Envs 下面。
         
        如果要改变这个位置：Windows 菜单 -> 设置 -> 系统 -> 关于（在左侧） -> 高级系统设置（在右侧） -> 环境变量 -> 新建系统变量，如下图：
         
        ![virtualenvwrapper_workon_home](attachment/virtualenvwrapper_workon_home.png)

    4. 使用
    
        1. 创建虚拟环境
        
            ```
            mkvirtualenv <ENV> [-a project_path]
            ```
        
        2. 使用虚拟环境
        
            ```
            workon <ENV>
            ```
        
        3. 退出虚拟环境
        
            ```
            deactivate
            ```
        
        4. 查看所有的虚拟环境
        
            ```
            workon
            ```
        
3. 安装 Nodejs

    Nodejs 是 JupyterLab 的 Extesion manager（扩展管理器）运行需要的依赖，JupyterLab 本身不需要。
    
    [在 Nodejs 官网下载](https://nodejs.org/zh-cn/download/)，用默认值安装即可。

4. 安装 JupyterLab

    以下在复制代码是不要复制大于号（>），这是一个 Windows 命令行提示符的标志（Linux 使用美元符号）。

    1. 创建虚拟环境
    
       ```
       > mkvirtualenv <ENV>
       ```
       
       可以先建立一个纯粹的 JupyterLab 虚拟环境，安装好必须的库，以后可以用:
       
       ```
       cpvirtualenv ENVNAME [TARGETENVNAME]
       ```
       
       来复制一个工作用的 JupyterLab 环境。当然也可以每次都从头创建。
       
       在我们的例子中，用 Jupyter 做虚拟环境名称，路径位于 D:\Jupyter。
       
       ```
       # 如果 D:\Jupyter 文件夹还不存在：
       > mkdir D:\Jupyter
       
       > mkvirtualenv Jupyter -a D:\Jupyter
       ```
       
       CMD 窗口的提示符会有变化，最前面以 (Jupyter) 开头，表示位于虚拟环境中。
       
       以下步骤均须在虚拟环境中操作，切换至虚拟环境使用：`workon Jupyter`。
       
    2. 安装 JupyterLab
    
        ```
        > pip install JupyterLab
        ```
    
    3. 安装依赖库
    
        ```
        > pip install [依赖库]
        ```
        
    4. 启动
    
        ```
        > jupyter lab
        ```

5. 其它可选工具

    1. git
    
        git 是一个版本管理工具，教程在[这里](https://git-scm.com/book/zh/v2)，下载在[这里](https://git-scm.com/downloads)。
        
        同时有几个 git 托管平台，[GitHub](https://github.com/)、[GitLab](https://gitlab.com/)、[Gitee](https://gitee.com/)。前面两个是国外的，可能要使用技术手段才能访问；第三个是国内的。


## Linux

我估计没什么人用 Linux，或者用的人都会，不写了。


## macOS

同 Linux。
