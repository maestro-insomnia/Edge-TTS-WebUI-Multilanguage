# edge-tts-webui-multilanguage

`edge-tts-webui-multilanguage` 是 [edge-tts](https://github.com/rany2/edge-tts)的web界面版，采用`Gradio`进行开发，在[edge-tts-webui](https://github.com/ycyy/edge-tts-webui)的基础上修改，新增了[tts-samples](https://github.com/yaph/tts-samples)中的所有语言并导入了音色试听样本。

`edge-tts-webui-multilanguage` is a web interface version of [edge-tts](https://github.com/rany2/edge-tts), developed using `gradio`. It is based on [edge-tts-webui](https://github.com/ycyy/edge-tts-webui), with modifications to add all the languages from [tts-samples](https://github.com/yaph/tts-samples) and import voice sample previews.


![](Snipaste.png)

## 安装/Installation

    pip install edge-tts
    pip install gradio
    pip install asyncio

## 运行/Run

    python tts-ui.py

## 使用/Usage

浏览器访问/Access via browser at:
```
localhost:7860
