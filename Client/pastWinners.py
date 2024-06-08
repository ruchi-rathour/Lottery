from flask import Flask, render_template, request, jsonify
import requests
from Downloads.Models import *
from Downloads.helper import *


app = Flask(__name__)
@app.route('/pastWinners/', methods=['GET'])
def getWinners():
    if request.method == 'GET':
        winners = getWin()
        return jsonify({
            'statusCode': 200,
            'data':winners}
        )

if __name__=='__main__':
    app.run(host='127.0.0.1',port = '5055')
