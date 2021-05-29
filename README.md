## 环境：Require

1. Anaconda3

### 安装

centos

```
yum install screen
```

debian,ubuntu

```
apt-get install screen
```

### 进入

创建一个窗口，指令如下

```
screen -S fastapi
```

然后就进入了一个全新的窗口



## Quick start

在合适的目录下克隆项目

- git clone 这个项目

  ```git
  git clone https://github.com/github-HDC/FastApi-.git
  ```

- 部署环境:

  ```python
  conda env update -f=environment.yaml
  conda activate 
  ```

---



​	【注意：针对Linux或者没有Anaconda3】使用包管理工具`pip`安装所需模块,
可以自行百度虚拟环境在linux中的操作，激活虚拟环境再安装如下包，再运行主程序

```bash
pip install requests
pip install fastapi
pip install uvicorn[standard]
```





---



- 开启运行程序

  ```python
  python main.py  ##默认端口为8080，防止端口冲突,需要被外部访问需要将main.py源码中的host改为 '0.0.0.0'
  ```

  The command `uvicorn main:app` refers to:

  - `main`: the file `main.py` (the Python "module").
  - `app`: the object created inside of `main.py` with the line `app = FastAPI()`.
  - `--reload`: make the server restart after code changes. Only do this for development.









| 请求方式 | 参数 | 说明                               | 必要性 |
| :------- | ---- | ---------------------------------- | ------ |
|          |      |                                    |        |
| GET      | word | 需要翻译的单词（可以是英文和汉语） | 是     |
|          |      |                                    |        |





详细查看：https://fastapi.tiangolo.com/

