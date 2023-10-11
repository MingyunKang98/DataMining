import matplotlib.pyplot as plt
# 누적막대그래프
x = [1,2,3,4,5]
y1 = [6,7,8,2,4]
y2 = [7,8,2,4,2]
plt.bar(x,y1, label='bar1')
plt.bar(x,y2, label='bar2', bottom=y1)
plt.legend()
plt.show()

import pandas as pd
# 박스플랏
data = [[2, 4, 6, 8, 10],[6,7, 8, 2, 4],[1, 3, 5, 7, 9],[7, 8, 2, 4, 2]]
x = pd.DataFrame(data)
plt.boxplot(x)
plt.show()

# 영역그래프
days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]
plt.stackplot(days, sleeping, eating, working, playing)
plt.legend(labels=['sleeping', 'eating', 'working', 'playing'])
plt.show()
