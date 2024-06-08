from flask import Flask, render_template, request, jsonify
import requests
from Downloads.Models import *
from Downloads.helper import *


app = Flask(__name__)
@app.route('/allottToken/', methods=['GET','POST'])
def fetch():
    if request.method == 'POST':
        details = request.form
        userID = details['user_id']  # userid
        contestID = details['contest_id']    # contest ID
        er = Error()
        if (not checkUser(userID, contestID)):
            er.userExists()
        if er.errorCode is not None:
            return render_template("getToken.html",msg = er.error)
        else:
            token = Token()
            token.createToken(contestID,userID)
            insertToDB(token)
            return token.Number
    return render_template("getToken.html")

if __name__=='__main__':
    app.run(host='127.0.0.1',port = '5055')
