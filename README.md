[中文](./README.md) | [EN](./README.en.md)

<div align="center">
<h1>🍦 edge-tts-webui-multilanguage</h1>
</div>

**`edge-tts-webui-multilanguage`** 是 [edge-tts](https://github.com/rany2/edge-tts)的web图形界面版，支持全球74种语言。采用`Gradio`进行开发，在[edge-tts-webui](https://github.com/ycyy/edge-tts-webui)的基础上修改，新增音调调整，新增[tts-samples](https://github.com/yaph/tts-samples)中所列的所有语言并导入了音色试听样本。

本人菜鸟一枚，如有错误请大佬多多指点。

![](Snipaste.jpeg)


## 普通安装

- ### 安装

```
    pip install edge-tts
    pip install gradio
    pip install asyncio
```
- ### 运行
 
```
    python tts-ui.py
```

- ### 浏览器访问
  
 ```
    http://localhost:7860/
```


## Docker安装

- ### 在Dockerfile所在目录创建镜像

```
    docker build -t edgetts-webui-multilanguage .
```

- ### 运行容器

```
    docker run -d -p 7860:7860 --name edgetts-webui-container edgetts-webui-multilanguage
```

- ### 浏览器访问

```
    http://localhost:7860
```
