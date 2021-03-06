import pandas as pd
from collections import defaultdict
import numpy as np
import time

# Read data from csv file 
data = pd.read_csv("/ay1.csv")
# Locate all indexes with null values in the account number column
nulls = data.loc[data['account_nbr'].isnull()].index.values
# Delete the null values
#data = data.dropna() 

# Function to compare elememnts in a container
def compare(a, b):
        return (a > b) - (a < b)

# Convert the relevant columns to list for easy handling 
acct_ids = data['account_id'].unique().tolist()

# create an empty dictionary 
my_dict = {}
# process items in both lists to create dictionary of keys and values
for item in acct_ids:
    mylist  = data[data['account_id'] == item]['account_nbr']
    my_dict.setdefault(item, []).extend(mylist.tolist())

# Function that does x,y,z
def group(x):
        tools = []
        # Loop through the items in the list 
        for values in x.values():
                for e in values:
                        if compare(values[0],e) != 0:
                                tools.append(e)
        return tools

def fd(alist):
        truth = data[data['account_nbr'].isin(alist)].index.get_values()
        truth = np.sort(np.append(truth,nulls))
        print("There are",len(truth), " violations in the dataset")
        '''for i in truth:                
                print("Violation at index", i+2, "in excel sheet")'''
        # Delete the violations and write to excel
        cleaneddata = data.drop(data.index[truth])
        cleaneddata.to_csv("C:\\Users\\Ajibola Vincent\\Documents\\Udacity\\ay2.csv", encoding='utf-8', index=False)
 
                            

if __name__ == "__main__":
        start = time.time()
        fd(group(my_dict))
        end = time.time()
        print(end - start)

