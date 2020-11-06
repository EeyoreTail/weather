import requests
import json

def get_weather_json(filename, url):
    '''生成天气的json文件'''
    try:
        f = open(filename, 'w')
        r = requests.get(url)
    except FileNotFoundError:
        print('File not found.')
    except requests.RequestException:
        print('URL not found.')
    else:
        try:
            contents = json.loads(r.text)
            json.dump(contents, f, ensure_ascii=False)
        except ValueError:
            print('Dump error.')
        else:
            f.close()
