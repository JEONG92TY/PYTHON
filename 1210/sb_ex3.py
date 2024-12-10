import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic.head())

'''
sns.catplot(x="class", y="survived", data = titanic, kind = "bar")
plt.show()
'''

sns.kdeplot(x="age", hue="survived", data = titanic)
plt.show()