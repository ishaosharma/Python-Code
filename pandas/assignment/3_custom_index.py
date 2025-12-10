#creating a dataframe with custom index
import pandas as pd
data={'A':[1,2,3],'B':[4,5,6]}
df=pd.DataFrame(data,index=['x','y','z'])
print(df)
 
data={'x':'first','y':'second','z':'third'}
df=df.rename(index=data)
print(df)
 
 
#load the data
import pandas as pd
df=pd.read_csv('data.csv')
#display oriinal colm
print(df.columns)
#rename columns Duration,Pulse,Maxpulse,Calories
df=df.rename(columns={'Duration':'duration','Pulse':'pulse','Maxpulse':'max_pulse','Calories':'calories'})
print(df.columns)