# Python 3.9を使用したベースイメージ
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# システムパッケージの更新と必要なライブラリのインストール
RUN apt-get update && apt-get install -y \
    libhdf5-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 必要なPythonパッケージのインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションファイルをコピー
COPY . .

# model/とdata/ディレクトリを作成
RUN mkdir -p model data

# デフォルトで学習サイクルを実行
CMD ["python", "train_cycle.py"]
