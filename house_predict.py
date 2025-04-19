import numpy as np

# 假資料：面積 (X) 和房價 (y)
X = np.array([30, 50, 70, 90, 110])
y = np.array([100, 150, 200, 250, 300])

# 計算斜率 a 和截距 b（線性回歸公式）
x_mean = np.mean(X)
y_mean = np.mean(y)

a = np.sum((X - x_mean) * (y - y_mean)) / np.sum((X - x_mean)**2)
b = y_mean - a * x_mean

# 預測房價（例如：80 平方公尺）
x_new = 80
y_pred = a * x_new + b

print(f"斜率 a: {a:.2f}")
print(f"截距 b: {b:.2f}")
print(f"預測房價（面積 80 平方公尺）：{y_pred:.2f} 萬元")