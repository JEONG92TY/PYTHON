import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')

'''
result1 = penguins.groupby("species").agg({
    "body_mass_g" : "mean"
    })
result1["body_mass_g"].plot.bar(x=result1.index, color="green")
plt.title("Average Body Mass by Species", fontsize=13)
plt.xlabel("Species", fontsize=10)
plt.ylabel("Body Mass(g)", fontsize=10)
plt.xticks(rotation=0)
plt.show()
'''

'''
sns.scatterplot(data=penguins, x="bill_length_mm",
                y="bill_depth_mm", hue="species")
plt.show()
'''

'''
sns.violinplot(x=penguins["island"], y=penguins["body_mass_g"])
plt.show()
'''