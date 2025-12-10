import pandas as pd
data={'Name':['Ankit','Bhavna','Chirag'],'Age':[23,24,22],'City':['Delhi','Mumbai','Bangalore']}
df=pd.DataFrame(data)
df=df.set_index("Name")
print("DataFrame with 'Name' as index:\n",df)
df=df.reset_index()
print("DataFrame after resetting index:\n",df)