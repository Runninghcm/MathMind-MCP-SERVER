FROM python:3.13

WORKDIR /app

RUN rm -rf /etc/apt/sources.list.d/* \
    && mkdir -p /etc/apt && echo "deb https://mirrors.ustc.edu.cn/debian bookworm main contrib non-free-firmware" > /etc/apt/sources.list \
    && echo "deb https://mirrors.ustc.edu.cn/debian bookworm-updates main contrib non-free-firmware" >> /etc/apt/sources.list \
    && echo "deb https://mirrors.ustc.edu.cn/debian-security bookworm-security main contrib non-free-firmware" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

#RUN uv sync
RUN pip install -i https://mirrors.aliyun.com/pypi/simple  fastmcp
RUN pip install  -i https://mirrors.aliyun.com/pypi/simple  requests
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# CMD ["uv", "run","-m", "src.mathmind_mcp_server.server", "--transport", "sse"]
CMD ["uv", "run","-m", "src.mathmind_mcp_server.server","--transport", "sse"]