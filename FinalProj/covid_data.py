import pandas as pd
import matplotlib.pyplot as plt

#Reading in the csv data 
data = pd.read_csv('time_series_covid19_confirmed_US.csv')

#Grouping the data by Island 
data = data.groupby('Province_State').sum()

#Cleaning up - dropping columns that isn't needed 
data = data.drop(columns = ['UID', 'code3', 'FIPS', 'Lat', 'Long_'])

#Transpose of the dataframe
#Used the big 8 states 
data_transposed = data.T
data_transposed.plot(y = ['California', 'Texas', 'Florida', 'New York', 
                          'Pennsylvania', 'Illinois', 'Ohio', 'Michigan'], 
                     use_index = True, 
                     figsize = (7,7))

#Adding labels to the graph 
plt.title('Total Confirmed COVID Cases in the Big 8 States', fontsize = 15)
plt.ylabel('Reported', fontsize = 15)
plt.xlabel('Date', fontsize = 15)
plt.xticks(rotation = 'vertical')
plt.show()