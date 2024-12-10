import matplotlib.pyplot as plt
from matplotlib import font_manager

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales_2019 = [100,120,140,110,130,150,160,170,180,200,190,210]
sales_2020 = [90,110,130,120,140,160,170,160,150,180,200,190]

plt.xlabel("Month")
plt.ylabel("Sales")
plt.plot(months, sales_2019, sales_2020)
plt.title("Monthly Sales Comparison (2019-2020)")
plt.legend(["2019", "2020"], loc = "upper left")

plt.show()