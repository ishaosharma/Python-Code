# 6.Create a DataFrame with columns Name, Age, and City. Set the Name
# column as the index. Access the age of the person named "Amit".
 
import pandas as pd
data={'Name':["Amit","Bhavna","Chirag"],'Age':[23,24,22],'City':['Delhi','Mumbai','Bangalore']}
df=pd.DataFrame(data)
df=df.set_index("Name")
print("dataframe with 'Name' as index:\n",df)
age_of_amit=df.loc['Amit','Age']
print("Age of Amit:\n",age_of_amit)