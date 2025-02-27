[中文](./README.md) | [EN](./README.en.md)

# 🍦 edge-tts-webui-multilanguage

**`edge-tts-webui-multilanguage`** is a web interface version of [edge-tts](https://github.com/rany2/edge-tts), developed using `Gradio`. It is based on [edge-tts-webui](https://github.com/ycyy/edge-tts-webui), with modifications to add pitch adjustment and include all the languages listed in [tts-samples](https://github.com/yaph/tts-samples), along with imported voice sample previews.

I am a beginner, so if there are any mistakes, please kindly point them out.

![](Snipaste.png)


## Standard Installation

- ### Install

```
    pip install edge-tts
    pip install gradio
    pip install asyncio
```

- ### Run

```
    python tts-ui.py
```

- ### Access via browser at

```
    http://localhost:7860/
```

## Install via Docker

- ### Run the following command in the directory containing the Dockerfile

```
    docker build -t edgetts-webui-multilanguage .
```

- ### Run the container

```
    docker run -d -p 7860:7860 --name edgetts-webui-container edgetts-webui-multilanguage
```

- ### Access via browser at

```
    http://localhost:7860
```
