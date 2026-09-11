import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


# ✏️ YOUR CODE HERE — set seaborn style to "whitegrid"
# (This adds subtle horizontal grid lines that make charts easier to read in presentations)
sns.set_theme(style="whitegrid")



# ✏️ YOUR CODE HERE — load "ecommerce_orders_exercise.csv" into a variable called df
df=pd.read_csv("ecommerce_orders_exercise.csv")


# ✏️ YOUR CODE HERE — display the first 5 rows to verify the data loaded correctly
print(df.head())

df.info()
