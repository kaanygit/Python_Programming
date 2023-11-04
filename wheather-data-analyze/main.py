

# with open("./weather_data.csv") as wheather_data:
#     wheather=wheather_data.readlines()
#     for datas in wheather:
#         data=datas.strip()
#         wheather_list.append(data)

# print(wheather_list)

# import csv 

# with open("./weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temteratures=[]
#     for row in data:
#         if row[1]!="temp":
#             temteratures.append(int(row[1]))
#             print(row)
# print(temteratures)


import pandas,math

data=pandas.read_csv("./weather_data.csv")

print(type(data))  # DataFrame
print(type(data["temp"])) # Series



print(data["temp"])


data_dict=data.to_dict()
print(data_dict)

temp_list=data["temp"].to_list()
print(temp_list) 

# average tempatures 
#way -1
average_tempatures_sum=0
for temp in temp_list:
    average_tempatures_sum+=temp
average_temp=average_tempatures_sum/len(temp_list)
print(math.floor(average_temp))

#way-2
average_sum2=sum(temp_list)/len(temp_list)
print(math.floor(average_sum2))     

#way-3 (pandas-library-doc)
print(math.floor(data["temp"].mean()))

#max-value-temp (pandas)
print(data["temp"].max())
#min-value-temp (pandas)
print(data["temp"].min())

#Get Data in Columns  ##uppercase e duyarlı !!
print(data["condition"]) 
print (data.condition)
print (data.temp)

## Get Data in Row
print(data[data["day"]=="Monday"])
print(data[data.temp==data.temp.max()]) #max temp the day
monday=data[data.day=="Monday"]
print (monday.condition)

print(monday.temp)
monday_temp_fah=(monday.temp[0]*(9/5))+32
print(monday_temp_fah)


# Create a dataframe from scractch
data_dict={
    "students":["Amy","James","Angela"],
    "scores":[76,56,65]
}

datas=pandas.DataFrame(data_dict)
datas.to_csv("new_data.csv")
print(datas)