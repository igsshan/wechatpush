import os
import random

import requests
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["WATER_TEMPLATE_ID"]


def get_words():
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return get_words()
    return words.json()['data']['text']


def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


chp = get_words()

client = WeChatClient(app_id, app_secret)

data = {
    "content": {"value": chp, "color": get_random_color()}
}

wm = WeChatMessage(client)
res = wm.send_template(user_id, template_id, data)
print(res)
