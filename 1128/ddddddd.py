electiricity_usage = [
    {"date" : "2024-11-01", "usage" : 12.5},
    {"date" : "2024-11-02", "usage" : 15.3},
    {"date" : "2024-11-03", "usage" : 10.8},
    {"date" : "2024-11-04", "usage" : 14.2},
    {"date" : "2024-11-05", "usage" : 13.6}
]


def remove_usage(date) :
    date = date
    for i in electiricity_usage:
        if i.get("date") == date :
            electiricity_usage.remove(i)
    print(electiricity_usage)

a = input("날짜")
print(remove_usage(a))