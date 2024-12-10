import pandas as pd


data = {
    "Name" : ["홍길동", "임꺽정", "성춘향"],
    "Age" : [25, 30, 35],
    "City" : ["Seoul", "Busan", "Incheon"]
}

df = pd.DataFrame(data)
print(df)
print(df.loc[df["Age"] == 30])

'''
result = df.isin(["성춘향", "홍길동", "20"])
print(result)
'''

#s1= pd.DataFrame([10,20,30])
#s2 = pd.DataFrame([5,15,25])
#result = s.agg(["sum", "mean", "max"])
#print(result)

#result1 = df.groupby("group")["value"].sum()
#result2 = df.groupby("group")["value"].agg(["sum", "mean", "max"])
#print(result1)
#print(result2)

'''
result1 = df.groupby("group").agg({
    "value1" : "sum",
    "value2" : ["mean", "sum"]
})

result2 = df.groupby("group").filter(lambda x : x["value1"].sum() > 30) 
print(result2)
'''