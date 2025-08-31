# python-reversi-ml

リバーシ（オセロ）の機械学習プロジェクトです。TensorFlowとKerasを使用してニューラルネットワークを構築し、セルフプレイによる強化学習でAIエージェントを訓練します。

## 機能

- リバーシゲームの実装
- デュアルネットワーク（方策と価値を出力）
- モンテカルロ木探索（MCTS）
- セルフプレイによる学習データ生成
- ニューラルネットワークの訓練
- ネットワーク性能の評価
- 人間対戦モード

## Docker での実行方法

### 1. 基本的な学習サイクルの実行

```bash
# Dockerイメージをビルド
docker build -t reversi-ml .

# 学習サイクルを実行（デフォルト）
docker run -v $(pwd)/model:/app/model -v $(pwd)/data:/app/data reversi-ml
```

### 2. Docker Compose を使用した実行

```bash
# 学習サイクルを実行
docker-compose up reversi-ml

# 対話的なシェルを起動
docker-compose --profile interactive up reversi-interactive

# 人間対戦モードを起動
docker-compose --profile play up reversi-play
```

### 3. 個別のスクリプトを実行

```bash
# デュアルネットワークの初期作成
docker run -v $(pwd)/model:/app/model reversi-ml python dual_network.py

# セルフプレイの実行
docker run -v $(pwd)/model:/app/model -v $(pwd)/data:/app/data reversi-ml python self_play.py

# ネットワークの訓練
docker run -v $(pwd)/model:/app/model -v $(pwd)/data:/app/data reversi-ml python train_network.py

# 人間対戦
docker run -it -v $(pwd)/model:/app/model reversi-ml python human_play.py
```

## ローカル環境での実行

### 必要な環境

- Python 3.9以上
- TensorFlow 2.13.0
- NumPy 1.24.3

### インストール

```bash
pip install -r requirements.txt
```

### 実行

```bash
# 初回実行時（ネットワークの作成）
python dual_network.py

# 学習サイクルの実行
python train_cycle.py

# 人間対戦
python human_play.py
```

## ディレクトリ構造

```
python-reversi-ml/
├── game.py              # リバーシゲームのロジック
├── dual_network.py      # デュアルネットワークの定義
├── pv_mcts.py          # モンテカルロ木探索の実装
├── self_play.py        # セルフプレイによる学習データ生成
├── train_network.py    # ニューラルネットワークの訓練
├── evaluate_network.py # ネットワーク性能の評価
├── train_cycle.py      # 学習サイクルの実行
├── human_play.py       # 人間対戦モード
├── vs.py              # 対戦モード
├── agent.py           # エージェント関連
├── model/             # 学習済みモデル保存ディレクトリ
└── data/              # 学習データ保存ディレクトリ
```

## 注意事項

- 初回実行時は `dual_network.py` を実行してベースとなるニューラルネットワークを作成してください
- 学習には時間がかかります（CPUの場合は特に）
- GPUを使用する場合は、TensorFlow-GPUとCUDAの設定が必要です