#2 Given a DataFrame d f where the index is the Name column, rename the
# index name to "Person"
import pandas as pd
data={'Name':["Ankit","Bhavna","Chirag"],'Age':[23,24,22],'City':['Delhi','Mumbai','Bangalore']}
df=pd.DataFrame(data)
print("original DataFrame \n",df)
df=df.set_index("Name")
print("DataFrame with 'name' as index:\n",df)
df=df.rename_axis(index={"Name":"Person"})
print("DataFrame with renamed index:\n",df)