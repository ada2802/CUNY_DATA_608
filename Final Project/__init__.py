
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta
from dateutil.parser import parse

##import validators
##from pymongo import MongoClient
import asyncio
#import websockets
import urllib.request as web
import json 

import warnings
warnings.filterwarnings("ignore")

from flask import Flask, render_template
 
app = Flask(__name__)


#webscripting historical data for analysis at last 1 years(360 days) 
def hist_price(tick):
    start_date = '20180101'
    end_date = '20181221'
    ndays = abs((datetime.strptime(end_date, "%Y%m%d") - datetime.strptime(start_date, "%Y%m%d")).days) +1
    
    #contruct URL by tick and date and webscripting history data
    url = "https://coinmarketcap.com/currencies/" + tick +"/historical-data/?start=" + start_date +"&end=" + end_date  
    soup = BeautifulSoup(requests.get(url, "lxml").content)
    header = list(i.get_text() for i in soup.find_all('th'))
    values = list(v.get_text().replace(",","") for v in soup.find_all('td'))

    #dataframe for 730-days price
    hist = []
    for i in range(0,ndays):
        hist.append(values[i*7:7*i+7])     
    hist_df = pd.DataFrame(hist[:],columns=header)
    hist_df .insert(0, 'Tick', tick)
    
    #conver data if it is number or date
    hist_df = hist_df.apply(pd.to_numeric, errors='ignore')
    hist_df['Date'] = [parse(d).strftime('%m/%d/%y') for d in hist_df['Date']]
    hist_df = hist_df.sort_values(by='Date', ascending=True) 

    return hist_df[['Tick','Date','Open*','High','Low','Close**']]


if __name__ == "__main__":

    #Top expensive Cryptocurrencies
    tickers = ['bitcoin','ethereum','bitcoin-cash','maker']
    
    col_names1 = ['Tick','Date','Open*','High','Low','Close**']
    data = pd.DataFrame(columns=col_names1)
    data_mav20 = pd.DataFrame()
    data_px = pd.DataFrame()
    weekly_return = pd.DataFrame()
    
    for i in tickers : 
        df = hist_price(i)      
        df.set_index('Date')
        data = data.append(df)
        
        
        #calculate 20-day Close MAV
        #save data to _MAV20.csv file to local drive
        df['MAV20'] = df['Close**'].rolling(20).mean()
        df_mav20 = df[['Date','Close**','MAV20']]
    
        fileName = i +'_MAV20.csv'
        df_mav20.to_csv(fileName, sep=',',index=False)
        
        
        #calculate Close weekly return
        index = 0
        wr = []
        weeks = []
        
        
        
        for index in range(int((len(df)+2)/7)-1) :        
            rate = ((df['Close**'][index*7])/(df['Close**'][(index+1)*7-1]) -1)*100
            wr.append(rate)
            index = index + 1 
            weeks.append(index)
      
        data_px['Weeks'] = weeks        
        data_px['Tick'] = i
        data_px['Weekly_rate'] = wr
        weekly_return = weekly_return.append(data_px)
        
    
    #save data to .csv file to local drive
    data.to_csv('data.csv', sep=',',columns=None, header=True, index=False, index_label=None)
    weekly_return.to_csv('weekly_return.csv', sep=',',columns=None, header=True, index=False, index_label=None)
    
    
