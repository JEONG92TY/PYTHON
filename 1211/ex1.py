from pydataset import data
import seaborn as sns
import matplotlib.pyplot as plt

mtcars = data('mtcars')
#print(mtcars.head())

def ex1() :
    avg = mtcars.groupby('cyl')["mpg"].mean().reset_index()
    sns.barplot(data=avg, x = "cyl", y="mpg")
    plt.show()

def ex2() :
    avg = mtcars.groupby('am')["hp"].mean().reset_index()
    sns.barplot(data=avg, x = "am", y="hp")
    plt.show()


def ex3() :
    data = mtcars.pivot_table(index="cyl", columns="gear", values="mpg")
    sns.heatmap(data)
    plt.show()

def ex4() :
    mtcars_data = mtcars[["mpg", "hp", "wt"]]
    data = mtcars_data.corr(method="pearson")
    sns.heatmap(data, annot=True)
    plt.show()

ex1()
ex2()
ex3()
ex4()