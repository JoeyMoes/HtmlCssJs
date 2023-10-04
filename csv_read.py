print('Start csv read application')

import pandas as pd

df = pd.read_csv("pokemon.csv")
#print(df["Name"])


for index,rij in df.iterrows():
    if rij["Legendary"] == True:
        print(rij["Name"])

        
    
    
