import matplotlib.pyplot as plt
import numpy as np

# 方角と角度の対応
directions = [
    ('n', 0), ('nne', 22.5), ('ne', 45), ('ene', 67.5),
    ('e', 90), ('ese', 112.5), ('se', 135), ('sse', 157.5),
    ('s', 180), ('ssw', 202.5), ('sw', 225), ('wsw', 247.5),
    ('w', 270), ('wnw', 292.5), ('nw', 315), ('nnw', 337.5)
]

# 各方向に対して個別に画像を生成
for direction, angle in directions:
    # 新しい図を作成、画像サイズを64x64に設定
    fig, ax = plt.subplots(figsize=(2, 2), dpi=32)  # 64x64ピクセルに調整
    ax.set_aspect('equal')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')

    # 矢印の長さを画像に収める
    arrow_length = 0.9  # 矢印の長さを0.9に設定して、収める

    # 矢印の開始位置を中央に設定
    x_start = 0
    y_start = 0

    # 矢印の終点を計算
    x_end = np.cos(np.radians(angle)) * arrow_length
    y_end = np.sin(np.radians(angle)) * arrow_length

    # 矢印を描画
    ax.arrow(x_start, y_start, x_end, y_end,
              head_width=0.1, head_length=0.1, fc='black', ec='black')

    # 画像を保存 (小文字の方向名を使用)
    plt.savefig(f'{direction}.png', dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(fig)  # 画像を閉じる

print("画像を保存しました。")

