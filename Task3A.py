#You are provided with insurance dataset on blackboard. Please logon on blackboard and download the
#dataset. Write a python code to:
# Read the dataset.
import pandas as pd
insurance_df = pd.read_csv("c:/Users/CC/Downloads/motor_insure.csv/motor_data11-14lats.csv")
# Inspects its column by displaying the first 10 records.
print("first 10 second")
print(insurance_df.head(10))

# Display records for make and usage for sets_num that are more than 40.
 
#print(insurance_df[insurance_df['sets_num']>40[['make','usage']]])

# Plot a basic graph showing effective_yr on y axes and carrying capacity on x-axes
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.scatter([1,2,3,4,5],[1,2,3,4,5])
plt.xlabel("EFFECTIVE_YR")
plt.ylabel("CARRYING_CAPACITY")
plt.title("EFFECTIVE_YR vs CARRYING_CAPACITY")
plt.show()

