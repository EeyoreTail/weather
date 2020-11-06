import json
import time

def forecast(filename):
    '''预报当天的天气'''
    f_obj = open(filename, 'r')
    datas = json.load(f_obj)
    weather = datas['data']['forecast']
    today = time.strftime('%Y-%m-%d', time.localtime())
    for daily_weather in weather:
        if daily_weather['ymd'] == today:
            print('Here is the weather report today:')
            for key, value in daily_weather.items():
                print(key, ':', value)


    
