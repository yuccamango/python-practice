import pandas as pd # this is for loading, cleaning, and analyzing data as well as pd.read_csv(file) or pd.read_excel(file) or pd.read_json('data.json') 
import matplotlib # this is for graphing and visualizing the results 
# you would use matplotlib to create a bar char, scatter plot, or line graph
  
df = pd.read_csv('shopping.csv') # df is for dataframe abbreviation you inport csv and excel as dataframes which are rows, indexes the rows, and columns

price = df.iloc[0,0]
# storing the first cell as price

def calculate_tax(price):
    return price * 0.08 #this returns only the tax amount
    # return price * 1.08 would return the price and the tax amount
