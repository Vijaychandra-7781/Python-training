import pandas as pd

# making data frame from the csv file
dataframe = pd.read_csv("data1.csv")

# using the replace() method
dataframe.replace(to_replace="empname",
                  value="name",
                  inplace=True)
dataframe.replace(to_replace="empage",
                  value="age",
                  inplace=True)
dataframe.replace(to_replace="sex",
                  value="gender",
                  inplace=True)

# writing  the dataframe to another csv file
dataframe.to_csv('outputfile.csv',
                 index=False)

# importing pandas as pd
import pandas as pd

# Making data frame from the csv file
df = pd.read_csv("data1.csv")

df.replace(to_replace =22,
                 value ="Omega Warrior")
