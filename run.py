import matplotlib.pyplot as plt
import numpy as np
import os

# 出力用のフォルダを作成
output_folder = 'output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 方角と角度の対応
directions = [
    ('n', 0), ('nne', 22.5), ('ne', 45), ('ene', 67.5),
    ('e', 90), ('ese', 112.5), ('se', 135), ('sse', 157.5),
    ('s', 180), ('ssw', 202.5), ('sw', 225), ('wsw', 247.5),
    ('w', 270), ('wnw', 292.5), ('nw', 315), ('nnw', 337.5)
]

# 各方向に対して個別に画像を生成
for direction, angle in directions:
    # 新しい図を作成、32x32ピクセルの画像を設定
    fig, ax = plt.subplots(figsize=(1, 1), dpi=32)  # 32x32ピクセルに調整
    ax.set_aspect('equal')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')

    # 矢印の長さを設定
    arrow_length = 1.5

    # 矢印の中心が(0,0)になるように開始位置を計算
    x_start = -np.cos(np.radians(angle)) * (arrow_length / 2)
    y_start = -np.sin(np.radians(angle)) * (arrow_length / 2)

    # 終点を計算（開始点から矢印の長さ分）
    x_end = np.cos(np.radians(angle)) * (arrow_length / 2)
    y_end = np.sin(np.radians(angle)) * (arrow_length / 2)

    # 矢印を描画（矢印の頭も大きくする）
    ax.arrow(x_start, y_start, x_end - x_start, y_end - y_start,
             head_width=0.15, head_length=0.15, fc='black', ec='black')

    # 画像をoutputフォルダ内に保存 (小文字の方向名を使用)
    output_path = os.path.join(output_folder, f'{direction}.png')
    
    # 保存時にdpiを適切に設定
    pixel = 64
    plt.savefig(output_path, dpi=pixel, bbox_inches=None, pad_inches=0)
    plt.close(fig)  # 画像を閉じる

print("画像をoutputフォルダに保存しました。")
