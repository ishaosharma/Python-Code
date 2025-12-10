# - Create a dataframe.
# 'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
# 'Age': [24, 27, 22, 32, 29].
# 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
# -Creating a simple DataFrame with columns 'Name', 'Age', and 'city'
# Set the 'Name' column as the new index.
# Reset the index back to the default integer indeх
 
import pandas as pd
data={'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
      'Age': [24, 27, 22, 32, 29],
      'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
      }
df=pd.DataFrame(data)
print("Original DataFrame:\n",df)
df=df.set_index('Name')
print('DataFrame with "Name" as index:\n',df)
df=df.reset_index()
print("DataFrame after resetting index:\n",df)
 
