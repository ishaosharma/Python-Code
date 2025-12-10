# 3. Change the index label Ashish to Ankit in the DataFrame df
#  that already has a Name column as its index.
import pandas as pd
data={'Name':['Ashish','Bhavna','Chirag'],'Age':[23,24,22],'City':['Delhi','Mumbai','Bangalore']}
df=pd.DataFrame(data)
df=df.set_index("Name")
print("original DataFrame with 'Name' as index:\n",df)
df=df.rename(index={'Ashish':'Ankit'})
print("DataFrame after renaming index label:",df)