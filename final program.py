import seaborn as sns
from nltk.probability import FreqDist
import pandas as pd
#open file, ‘Border_Crossing_Entry_Data’
border_data = pd.read_csv('Border_Crossing_Entry_Data.csv')
print(border_data)

sns.get_dataset_names()
data = sns.load_dataset('border_data')

Border_Crossing_Entry_Data.data.shape()

#contrast state/port names
sns.histplot(x = 'state', hue = 'port names', data = border_data)
sns.lineplot(x = 'state', y = 'port names')

#compare border location
sns.distplot(x = 'border', data = border_data)
#frequency of border location usage
border1 = FreqDist('US-Mexico Border')
border2 = FreqDist('US-Canada Border')

#compare date
sns.histplot(x = 'date', hue = 'month', data = border_data)
sns.lineplot(x = 'date', hue = 'month', data = border_data)

#analyze measure(type of transportation crossing)
sns.distplot(x = 'measure', data = border_data)
#frequency of measure(type of transportation crossing)
trucks = FreqDist('trucks')
trains = FreqDist('trains')
bus_passengers = FreqDist('bus passengers')
buses = FreqDist('buses')
train_passengers = FreqDist('train passengers')
pedestrians = FreqDist('pedestrians')

#analyze value 
sns.displot(x = 'value', data = border_data)


