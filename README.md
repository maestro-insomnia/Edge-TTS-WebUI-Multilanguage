# edge-tts-webui-multilanguage

**`edge-tts-webui-multilanguage`** 是 [edge-tts](https://github.com/rany2/edge-tts)的web界面版，采用`Gradio`进行开发，在[edge-tts-webui](https://github.com/ycyy/edge-tts-webui)的基础上修改，新增音调调整，增加了[tts-samples](https://github.com/yaph/tts-samples)中所列的所有语言并导入了音色试听样本。

**`edge-tts-webui-multilanguage`** is a web interface version of [edge-tts](https://github.com/rany2/edge-tts), developed using `Gradio`. It is based on [edge-tts-webui](https://github.com/ycyy/edge-tts-webui), with modifications to add pitch adjustment and include all the languages listed in [tts-samples](https://github.com/yaph/tts-samples), along with imported voice sample previews.

本人菜鸟一枚，如有错误请大佬多多指点。

I am a beginner, so if there are any mistakes, please kindly point them out.

![](Snipaste.png)


## 普通安装/Standard Installation

### 安装/Install

    pip install edge-tts
    pip install gradio
    pip install asyncio

### 运行/Run

    python tts-ui.py

### 浏览器访问/Access via browser at

    http://localhost:7860/

## Docker安装/Install via Docker

### 在Dockerfile所在目录创建镜像/Run the following command in the directory containing the Dockerfile

    docker build -t edgetts-webui-multilanguage .

### 运行容器/Run the container

    docker run -d -p 7860:7860 --name edgetts-webui-container edgetts-webui-multilanguage

### 浏览器访问/Access via browser at

    http://localhost:7860
