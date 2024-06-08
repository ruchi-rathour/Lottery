from flask import Flask, render_template, request, jsonify
import requests
from Downloads.Models import *
from Downloads.helper import *


app = Flask(__name__)
@app.route('/addContest/', methods=['GET','POST'])
def addContest():
    if request.method == 'POST':
        details = request.form
        contestID = details['contest_id'] #contest id
        name = details['contest_name']  # contest name
        prize = details['prize']   # contest prize
        deadline = details['deadline']  # contest deadline
        
        contest = Contest(contestID, name, prize, deadline)
        addCon(contest)
        return "success"
            
    return render_template("addContest.html")

if __name__=='__main__':
    app.run(host='127.0.0.1',port = '5050')

if __name__=='__main__':
    app.run(host='127.0.0.1',port = '5050')
