import matplotlib.pyplot as plt
from matplotlib import font_manager

fruits = ["Apple", "Banana", "Melon","Grape" ]
ratio = [34, 32, 16, 18]
explode = [0, 0.11, 0, 0.13]
colors = ['red', 'yellow', 'green', 'purple']
wedgeprops = {'width' : 0.7, 'edgecolor' : 'black'}

plt.pie(ratio, labels=fruits, autopct='%.1f%%', explode=explode, colors=colors, wedgeprops=wedgeprops)
plt.show()