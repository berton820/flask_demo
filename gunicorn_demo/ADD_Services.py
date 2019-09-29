# coding=utf-8


from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        en = request.args.get('en', '')
        zh = request.args.get('zh', '')
    else:
        content = request.get_json(silent=True)
        en = content['en']
        zh = content['zh']
    if not en or not zh:
        return jsonify({'succ': 'error'})


    total_add = int(en)+int(zh)
    context = {
        'en': en,
        'zh': zh,
        'total': total_add,
        'succ': 'ok'
    }
    return jsonify(context)
#    return (111) 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=16384)
