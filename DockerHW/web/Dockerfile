# 使用 Python 3.9 作為基礎映像 FROM baseImage
FROM python:3.11-slim

# 設定工作目錄 WORKDIR /the/workdir/path
WORKDIR /app

# 複製應用程式檔案到容器內 COPY source test
COPY . .

# 安裝所需的 Python 套作 RUN command
RUN pip install -r requirements.txt

# 指定 Flask 啟動命令 CMD [ "executable" ]
CMD ["python", "main.py"]
