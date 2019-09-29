from flask import Flask
from flask import render_template
from flask import request
from googletrans import Translator
import os
import socket

app = Flask(__name__)

# 初始化，加载模型部分，需要把模型提前加载入内存

translator = Translator()


def my_func(query):
    # Coding Here .....
    print(query)
    result = translator.translate(query, dest="en").text
    return result


@app.route('/')
def seg():
    return render_template('demo.html')  # demo页面布局展示用的


# 下面这个是真正数据交互的接口
@app.route('/demo_api', methods=['GET', 'POST'])
def demo_api():
    send_data = request.form['query'].replace('\n', '').strip()
    return my_func(send_data)


if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0', port=10002)
