# encoding:utf-8
import ImageGrab
import Image
import tkinter as tk
import pytesseract
import requests
import json


def translate(text):
    values = {'from': 'en', 'to': 'zh',
              'query': text,
              'transtype': 'translang', 'simple_means_flag': 3}
    r = requests.post('https://fanyi.baidu.com/v2transapi', values, timeout=30)
    return r.text


def getText(text):
    text = translate(text)
    text = json.loads(text)
    return text['trans_result'].get('data')[0].get('dst')


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
