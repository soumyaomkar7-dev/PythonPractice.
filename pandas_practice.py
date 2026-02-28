import pandas as pd  
pd.DataFrame()
df = pd.DataFrame()
df['color'] = ['blue' ,'red' ,'yellow','green']
df['radius'] = [2,4,3,5,]
print(df) #show result
df['diameter'] = df['radius']*2
print(df) 
print(df['radius'].min())
print(df['radius'].sum())
print(df['radius'].mean())
print(df.iloc[0]) # iloc stands for integer location 
print(df.shape)
print(df.shape[0])
print(df.shape[1])
print(df)