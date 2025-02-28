# 1. 使用 Python 3.11 的精简版镜像
FROM python:3.11.11-slim-bullseye

# 2. 修改 APT 源、安装 Git & 证书、设置国内 PyPI 源
RUN sed -i 's|http://deb.debian.org|http://mirrors.aliyun.com|g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends git ca-certificates && \
    rm -rf /var/lib/apt/lists/* && \
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 3. 设置工作目录 & 从 GitHub 下载代码
WORKDIR /app/Edge-TTS-Webui-Multilanguage
RUN git clone --depth=1 https://github.com/maestro-insomnia/Edge-TTS-Webui-Multilanguage.git . && \
    rm -rf .git && \
    apt-get remove -y git && apt-get autoremove -y && apt-get clean

# 4. 安装 Python 依赖
RUN pip install --no-cache-dir edge-tts gradio asyncio

# 5. 暴露端口
EXPOSE 7860

# 6. 运行应用
CMD ["python", "tts-ui.py"]
