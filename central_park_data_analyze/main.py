import pandas 

data=pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231104.csv")


grey_squrirrel_count=len(data[data["Primary Fur Color"]=="Gray"])
red_squrirrel_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squrirrel_count=len(data[data["Primary Fur Color"]=="Black"])


print(grey_squrirrel_count)
print(red_squrirrel_count)
print(black_squrirrel_count)

data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squrirrel_count,red_squrirrel_count,black_squrirrel_count]
}

df=pandas.DataFrame(data_dict)
df.to_csv("squirrel.count.csv")