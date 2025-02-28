# 1. 使用 Python 3.11 的精简版镜像
FROM python:3.11.11-slim-bullseye

# 2. 设置工作目录
WORKDIR /app/Edge-TTS-Webui-Multilanguage

# 3. 从 GitHub 下载代码
RUN apt-get update && \
    apt-get install -y --no-install-recommends git ca-certificates && \
    git clone --depth=1 https://github.com/maestro-insomnia/Edge-TTS-Webui-Multilanguage.git . && \
    rm -rf .git && \
    apt-get remove -y git && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 4. 安装 Python 依赖
RUN pip install --no-cache-dir edge-tts gradio asyncio

# 5. 暴露端口
EXPOSE 7860

# 6. 运行应用
CMD ["python", "tts-ui.py"]
