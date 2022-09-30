from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now() + timedelta(days=1)
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]

name = os.environ['NAME']

yuandanTime = "01-01"
chunjieTime = "01-22"


def get_weather():
    url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
    res = requests.get(url).json()
    weather = res['data']['list'][0]
    return weather['weather'], math.floor(weather['high']), math.floor(weather['low']), weather['wind'], weather[
        'airQuality']


def get_count():
    delta = today - datetime.strptime(start_date, "%Y-%m-%d")
    return delta.days


def get_birthday():
    next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days


def get_words():
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return get_words()
    return words.json()['data']['text']


def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


def get_zao():
    url = "http://api.tianapi.com/zaoan/index" + "?key=191681c57e8c23f8ac66b9d035b1ed23"
    zao = requests.get(url)
    if zao.status_code != 200:
        return get_words()
    return zao.json()['newslist'][0]['content']


def get_yuandan():
    next = datetime.strptime(str(datetime.today().strftime("%Y")) + "-" + yuandanTime, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days


def get_chunjie():
    next = datetime.strptime(str(datetime.today().strftime("%Y")) + "-" + chunjieTime, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days


yuandan = get_yuandan()
chunjie = get_chunjie()
zaoan = get_zao()

dayTime = today.strftime("%m") + "月" + today.strftime("%d") + "日"
week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
week = week_list[today.weekday()]
dayWeek = dayTime + " " + week

client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperatureH, temperatureL, wind, air = get_weather()
data = {"today": {"value": dayWeek, "color": get_random_color()},
        "name": {"value": name, "color": get_random_color()},
        "weather": {"value": wea, "color": get_random_color()},
        "temperatureH": {"value": temperatureH, "color": get_random_color()},
        "temperatureL": {"value": temperatureL, "color": get_random_color()},
        "wind": {"value": wind, "color": get_random_color()},
        "airQuality": {"value": air, "color": get_random_color()},
        "content": {"value": zaoan, "color": get_random_color()},
        "yuandan": {"value": yuandan, "color": get_random_color()},
        "chunjie": {"value": chunjie, "color": get_random_color()}
        }
res = wm.send_template(user_id, template_id, data)
print(res)

# data = {"name": {"value": name}, "today": {"value": dayWeek},
#         "weather": {"value": wea},
#         "temperature": {"value": temperature},
#         "airQuality": {"value": air},
#         "love_days": {"value": get_count()},
#         "birthday_left": {"value": get_birthday()}, "words": {"value": get_words(), "color": get_random_color()}}
