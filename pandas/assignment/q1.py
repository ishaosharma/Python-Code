#create a DataFrame and set a custom index that starts from 10 and increment by 2 . Then,access the data of the second row .
import pandas as pd
data = {
    'student':["Amit","John","Ankit"],
    'rank': [1,3,2]
}
index = pd.RangeIndex(start=10,step=2,stop=10+2*len(data['student']))
df = pd.DataFrame(data, index=index)
second_row = df.iloc[2]
print("DataFrame:\n",df)
print("Second Row:\n",second_row)