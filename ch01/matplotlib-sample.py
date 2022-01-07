import numpy as np
import matplotlib.pyplot as plt

# データの作成
x = np.arange(0, 6, 0.1) # 0から６まで0.1刻みで生成
y = np.sin(x)
plt.plot(x, y)
plt.show()

