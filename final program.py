import seaborn as sns
from nltk.probability import FreqDist
import pandas as pd
#open file, ‘Border_Crossing_Entry_Data’
border_data = pd.read_csv('Border_Crossing_Entry_Data.csv')
print(border_data)

sns.get_dataset_names()
data = sns.load_dataset('border_data')

Border_Crossing_Entry_Data.data.shape()

#contrast border crossings/border
sns.countplot(x='Border', data=border_data)
plt.title('Number of Border Crossings by Border'

#contrast border crossings/port name
plt.figure(figsize=(20, 10))
sns.barplot(x='Port_Name', y='Value', data=border_data)
plt.title('Number of Crossings by Port')
plt.xlabel('Port Name')
plt.ylabel('Crossings')
plt.xticks(rotation=90)
plt.show()

#distribution of border crossing by measure
fig, ax = plt.subplots(figsize=(15, 10))
sns.boxplot(x='Measure', y='Value', data=border_data, ax=ax)
plt.title('Distribution of Border Crossing Values by Measure')
plt.xlabel('Measure')
plt.ylabel('Value')
plt.xticks(rotation=45) 
plt.show()

#compare border crossing over time
fig, ax = plt.subplots(figsize=(15, 10))
sns.lineplot(x='Date', y='Value', data=border_data, ax=ax) 
plt.title('Border Crossings Over Time')
plt.xticks(rotation=90)
plt.show()
