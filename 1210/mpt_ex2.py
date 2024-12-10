import matplotlib.pyplot as plt
from matplotlib import font_manager

categories = ["Category 1", "Category 2", "Category 3", "Category 4", "Category 5"]
data = [20, 35, 15, 27, 45]
#plt.figure(figsize=(5,5))

plt.bar(categories, data)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart")
plt.xticks(rotation=45)
plt.grid()

plt.show()