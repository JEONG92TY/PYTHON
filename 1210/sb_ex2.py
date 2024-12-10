import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

flights = sns.load_dataset('flights')

'''
result1 = flights.groupby("year").agg({
    "passengers" : "mean"
    })
result1["passengers"].plot(x=result1.index, color="green")
plt.title("Average Body Mass by Species", fontsize=13)
plt.xlabel("Year", fontsize=10)
plt.ylabel("Passengers", fontsize=10)
plt.xticks(rotation=0)
plt.show()
'''

'''
data = flights.pivot(index="year", columns="month", values="passengers")
sns.heatmap(data)
plt.show()
'''

data1 = flights[flights["year"] == 1958]
sns.barplot( data=data1, x="month", y="passengers")
plt.show()