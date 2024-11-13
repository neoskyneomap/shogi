# ====================
# 学習サイクルの実行
# ====================

# パッケージのインポート
import tensorflow as tf
from dual_network import dual_network
from self_play import self_play
from train_network import train_network
from evaluate_network import evaluate_network
from pathlib import Path
from shutil import copy
import config

# GPU設定の読み込み
config.setup_gpu()

# デュアルネットワークの作成
dual_network()

for i in range(20):
    print('Train', i, '====================')
    # セルフプレイ部
    self_play()

    # パラメータ更新部
    train_network()

    # 新パラメータ評価部
    updated = evaluate_network()

    # ベストモデルのコピーを保存
    best_model_path = Path(f'./model/best{i}.h5')
    copy('./model/best.h5', best_model_path)
    print(f'Best model saved as best{i}.h5')

    # ベストプレイヤーの交代が行われたかを出力
    if updated:
        print(f'New best model found in cycle {i}.')
    else:
        print(f'No improvement in cycle {i}; current best model retained.')