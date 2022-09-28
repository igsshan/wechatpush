import math
import random
from datetime import datetime

import requests

today = datetime.today()
str_p = str(today)
# todayTime = datetime.strptime(str_p, "%Y年%m月%d日")
print(today)
print(str_p)
year = today.strftime("%Y")
month = today.strftime("%m")
day = today.strftime("%d")
print(month + "月" + day + "日")

week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
week = week_list[today.weekday()]
print(week)

dayTime = today.strftime("%Y") + "年" + today.strftime("%m") + "月" + today.strftime("%d") + "日"
print(dayTime)

dayWeek = dayTime + " " + week
print(dayWeek)


def get_weather():
    url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + "深圳"
    res = requests.get(url).json()
    weather = res['data']['list'][0]
    return weather['airQuality'], weather['weather'], math.floor(weather['temp'])


ari, wea, templ = get_weather()

print(ari, wea, templ)


def get_words():
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return get_words()
    return words.json()['data']['text']


textChp = get_words()

print(textChp)


def get_zao():
    url = "http://api.tianapi.com/zaoan/index" + "?key=191681c57e8c23f8ac66b9d035b1ed23"
    zao = requests.get(url)
    if zao.status_code != 200:
        return get_words()
    return zao.json()['newslist'][0]['content']


zaoan = get_zao()

print(zaoan)


def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


print(get_random_color())
