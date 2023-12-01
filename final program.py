import seaborn as sns
from nltk.probability import FreqDist
#open file, ‘Border_Crossing_Entry_Data’

open('Border_Crossing_Entry_Data', 'r')

sns.get_dataset_names()
data = sns.load_dataset('Border_Crossing_Entry_Data')

Border_Crossing_Entry_Data.data.shape()

#contrast state/port names
sns.histplot(x = 'state', hue = 'port names', data = Border_Crossing_Entry_Data)
sns.lineplot(x = 'state', y = 'port names')

#compare border location
sns.distplot(x = 'border', data = Border_Crossing_Entry_Data)
#frequency of border location usage
border1 = FreqDist('US-Mexico Border')
border2 = FreqDist('US-Canada Border')

#compare date
sns.histplot(x = 'date', hue = 'month', data = Border_Crossing_Entry_Data)
sns.lineplot(x = 'date', hue = 'month', data = Border_Crossing_Entry_Data)

#analyze measure(type of transportation crossing)
sns.distplot(x = 'measure', data = Border_Crossing_Entry_Data)
#frequency of measure(type of transportation crossing)
trucks = FreqDist('trucks')
trains = FreqDist('trains')
bus_passengers = FreqDist('bus passengers')
buses = FreqDist('buses')
train_passengers = FreqDist('train passengers')
pedestrians = FreqDist('pedestrians')

#analyze value 
sns.displot(x = 'value', data = Border_Crossing_Entry_Data)


