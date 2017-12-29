# encoding:utf-8
import hashlib

import ImageGrab
import Image
import tkinter as tk
import pytesseract
import requests
import json


def translate(text):
    url='https://fanyi-api.baidu.com/api/trans/vip/translate'
    # 这三个属性自己设置 appid和密码可以去百度翻译申请 当月翻译字符数≤2百万，当月免费
    appid='' #appid
    salt=123456 #随机数可以自己设置
    pass='' # 密码
    md5=hashlib.md5()
    raw=appid+text+str(salt)+pass
    print(raw)
    md5.update(raw.encode('utf-8'))
    sign=md5.hexdigest()
    data={
        'q':text,
        'from':'en',
        'to':'zh',
        'appid':appid,
        'salt':salt,
        'sign':sign
    }
    r=requests.get(url,data)
    return r.text

def getText(text):
    text=translate(text)
    text=json.loads(text)
    return text['trans_result'][0].get('dst')

window = tk.Tk()
window.title('Translate')
window.geometry('200x400')


def beginTranslate():
    im = ImageGrab.grabclipboard()
    if isinstance(im, Image.Image):
        im = im.convert("L")
        text = pytesseract.image_to_string(im)
        text = text.replace('\n', ' ')
        text = text.replace('’r', 't')
        print(text)
        t1.delete(1.0, tk.END)
        t1.insert('insert', text)
        t2.delete(1.0, tk.END)
        t2.insert('insert', getText(text))
    else:
        print("文件不存在")


def reTranslate():
    text = t1.get("0.0", "end")
    t2.delete(1.0, tk.END)
    t2.insert('insert', getText(text))


# 这里是窗口的内容
b1 = tk.Button(window, text="Translate", width=15, height=2, command=beginTranslate)
b1.pack()
t1 = tk.Text(window, height=10)
t1.pack()
b2 = tk.Button(window, text="ReTranslate", width=15, height=2, command=reTranslate)
b2.pack()
t2 = tk.Text(window, height=10)
t2.pack()

window.mainloop()
