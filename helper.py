import sqlite3
import random
import datetime
from datetime import date

# to check if a particular user has already participated in the contest or not
def checkUser(userID, contest_id):
    with sqlite3.connect("test.db") as con:  
        cur = con.cursor()
        qr = f"select * from token_tb where userID='{userID}' and contest_id='{contest_id}'"
        cur.execute(qr)
        con.commit()
        rows = cur.fetchall()
        if len(rows)!=0:
            return False
        else:
            return True

# to insert token to token_tb       
def insertToDB(token):
    with sqlite3.connect("test.db") as con:
        cur = con.cursor()
        qr = f"insert into token_tb values('{token.Number}','{token.UserID}','{token.ContestID}')"
        cur.execute(qr)
        con.commit()
    return


# to get the list of upcoming contests
def getContests():
    with sqlite3.connect("test.db") as con:
        cur = con.cursor()
        qr = f"select * from contest_tb where expired='NO' order by deadline DESC"
        cur.execute(qr)
        con.commit()
        rows = cur.fetchall()
        contests = []
        for row in rows:
            contests.append(row)
        return contests


# to get the winners of past contests
def getWin():
    with sqlite3.connect("test.db") as con:  
        cur = con.cursor()
        d = datetime.timedelta(days = 8)
        qr = f"select contest_id, user_id from winners_tb where deadline>='{date.today()-d}'"
        cur.execute(qr)
        con.commit()
        rows = cur.fetchall()
        winners = []
        for row in rows:
            winners.append(row)
    return winners


# to add new contests in the contest_tb
def addCon(contest):
    with sqlite3.connect("test.db") as con:
        cur = con.cursor()
        qr = f"insert into contest_tb values('{contest.ContestID}','{contest.Reward}','{contest.Deadline}','{contest.Name}','NO')"
        cur.execute(qr)
        con.commit()
    return


# to extend deadline of a contest
def extendDead(contestID, deadline):
    with sqlite3.connect("test.db") as con:
        cur = con.cursor()
        qr = f"UPDATE contest_tb SET deadline = '{deadline}' WHERE contest_id = '{contestID}'"
        cur.execute(qr)
        con.commit()
    return


# to remove a contest
def remContest(contestID):
    with sqlite3.connect("test.db") as con:
        cur = con.cursor()
        qr = f"DELETE from contest_tb WHERE contest_id ={contestID}"
        cur.execute(qr)
        qr = f"DELETE from token_tb WHERE contest_id={contestID}"
        cur.execute(qr)
        con.commit()
    return


# to insert the credentials of a winner in the winner_tb
def insertWinner(winner, cid):
    with sqlite3.connect("test.db") as con:
        cur = con.cursor()
        qr = f"insert into winners_tb values('{cid}','{winner[1]}',1,'{date.today()}')"
        cur.execute(qr)
        con.commit()
    return


# to find the winner of the contest that has reached its deadline
def predictWinner():
    with sqlite3.connect("test.db") as con:
        cur = con.cursor()
        qr = f"select contest_id from contest_tb where expired='NO' and deadline='{date.today()}' "
        cur.execute(qr)
        con.commit()
        contests = []
        rows = cur.fetchall()
        for row in rows:
            contests.append(row[0])
            qr = f"update contest_tb set expired='YES' where contest_id='{row[0]}'"
            cur.execute(qr)
            con.commit()
        winners = dict()
        for cid in contests:
            qr = f"select token_number, userID from token_tb where contest_id='{cid}'"
            cur.execute(qr)
            con.commit()
            participants = cur.fetchall()
            winner = random.choice(participants)
            insertWinner(winner,cid)
            winners[cid] = winner[1]
        
    return winners
