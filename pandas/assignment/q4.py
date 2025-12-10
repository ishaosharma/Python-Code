import pandas as pd
data={'Name':["Ankit","Bhavna","Chirag"],'Age':[23,24,22],'City':['Delhi','Mumbai','Bangalore']}
df=pd.DataFrame(data)
print(df)
df.index=['a','b','c']
print(df)