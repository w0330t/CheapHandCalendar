from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

weeks = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
directions = ["北方", "东北方", "东方", "东南方", "南方", "西南方", "西方", "西北方"]
activities = [
    {'name': "买入", 'good': '地位抄底，老板大赚。', 'bad': '你以为买得很低了，其实会更低'},
    {'name': "卖出", 'good': '高抛低吸，等待时机', 'bad': '今天卖明天就会涨了'},
]
# 开始日期。用于计算种子。
start_day = date(2018, 4, 9)


@app.route('/')
def main():
    data = {}

    today = date.today()
    today_day = today.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
    today_week = weeks[today.weekday()]

    seed = (today - start_day).days
    seed = str(seed)

    data['today'] =  today_day + " " + today_week
    return render_template('main.html', data=data)


if __name__ == '__main__':
    app.debug = True
    app.run()