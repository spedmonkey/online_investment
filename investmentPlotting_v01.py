import pandas.io.data as web
from datetime import datetime
import matplotlib.pyplot as plt    
end = datetime.now()
start = datetime(end.year - 2, end.month, end.day)

asx = web.DataReader('VAS.AX', 'yahoo', start, end)
msci=web.DataReader("MSCI", 'google', start, end)
     
asx['msci']=msci['Close']
asx['asx300']=asx['Close']

plots = asx[['asx300', 'msci']].plot(subplots=False, figsize=(10, 10) )
plt.plot(msci['Close'], label = 'msci')
plt.show()