from flask import Flask, render_template, request, jsonify
import requests
from Downloads.Models import *
from Downloads.helper import *


app = Flask(__name__)
@app.route('/extendDeadline/', methods=['GET','POST'])
def extendDeadline():
    if request.method == 'POST':
        details = request.form
        contestID = details['contest_id']  # contest ID
        deadline = details['deadline']  # contest deadline
        extendDead(contestID,deadline)
        return "success"
            
    return render_template("extendDeadline.html")

if __name__=='__main__':
    app.run(host='127.0.0.1',port = '5050')
