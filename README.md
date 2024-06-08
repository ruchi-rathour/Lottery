# Lucky Draw Gaming Service
This is an attempt to develop a Lucky Draw gaming Service that allows 
users to participate in a Lucky draw and win exciting prizes.

## Features

- User can request for a lucky draw token to participate in an event
- A user can participate with only one token in one event
- User can request the list of previous winners
- Also, the list of various contests and their rewards can be fetched.

## How to use this project
First you would need to install flask by running the following commands:
```
pip3 install Flask
```

Then you would need to create a copy of this repo on your local machine. 
To use any api you would need to run the corresponding python script.
For example, if you want to run the allottToken API, then you need to run
the allottToken.py file.

Then you would need to open this url - http://127.0.0.1:5055/allottToken/
> Note - the resource would change with the API you want to run

As soon as you open that web page in browser, you can see a simplistic interface
of a form that requires you to fill some details to allott you a token.

Refer to this image:
![Alt text](example.png?raw=true "allottToken")

Similarly you can run any of the other APIs as well.

## Design

> The project has been built using **User centric** and **Admin centric APIs**

> User centric APIs include the following : 
- API to get token for participating in a contest
- API to fetch the list of past winners
- API to fetch the contest information - rewards and timings

> Admin centric APIs include the following
- API to add new contests for the users to participate
- API to reschedule a contest
- API to cancel an ongoing contest

> Along with that the result of lottery contest would be determined by running 
the script on the server as a **CRON job** which would be scheduled to run everyday
on a fixed time e.g. at 8:00 am.
This script would also update the winners_table that keeps the record of winners
of past contests.

**The figure demonstrates the structure of the service**

![Alt text](flowchart.png?raw=true "Flowchart")

## Techstack

The project has been built using the following :

- [Python](https://www.python.org/) - an interpreted high-level general-purpose programming language
- [SQLite3](https://docs.python.org/3/library/sqlite3.html) - A lightweight replica of MySQL database 
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - To develop the web framework

## API Documentation
- ### To get a token to participate in a contest
    This API returns a hexadecimal equivalent of a unique SHA256 code generated using
    the userID, contest_name and current date.
    This hexadecimal code is used as the token to participate in the Lucky Draw contest
    #### Request
    `POST /allottToken/`
    #### Parameters
    ```sh
    userID
    contestID
    ```
    #### Response
    ```
    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: application/json
    Body: {
            token : f6071725e7ddeb434fb6b32b8ec4a2b14dd7db0d785347b2fb48f9975126178f
          }
    ```

- ### To get the list of past contest winners
    This API returns the list of winners of contests in the last 1 week along with the corresponding
    contests and their dates
    #### Request
    `GET /pastWinners/`
    #### Response
    ```
    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: application/json
    Body: {
           [contest_id1, winner_user_id1],
           [contest_id2, winner_user_id2],
           ....
          }
    ```

- ### To get the details of contests
    This API returns the list of contests along with their rewards and schedules
    #### Request
    `GET /contestDetails/`
    #### Response
    ```
    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: application/json
    Body: {
           [contest_id1, reward1, schedule1, contest_name1],
           [contest_id2, reward2, schedule2, contest_name2],
           ....
          }
    ```

- ### To add a new contest for the users to participate
    This API lets the admin to add new contest for the users to participate
    #### Request
    `POST /addContest/`
    #### Parameters
    ```sh
    contestID
    Reward
    Deadline
    ContestName
    ```
    #### Response
    ```
    HTTP/1.1 200 OK
    Status: 200 OK
    ```

- ### To modify the deadline of a contest
    This API lets the admin to extend the deadline of a contest
    #### Request
    `POST /extendDeadline/`
    #### Parameters
    ```sh
    contestID
    Deadline
    ```
    #### Response
    ```
    HTTP/1.1 200 OK
    Status: 200 OK
    ```

- ### To remove a contest
    This API lets the admin to remove of an upcoming contest
    #### Request
    `POST /removeContest/`
    #### Parameters
    ```sh
    contestID
    Deadline
    ```
    #### Response
    ```
    HTTP/1.1 200 OK
    Status: 200 OK
    ```

## Database Schema
In this project I am currently using SQLite3 as the database due to ease of use 
and demonstration but it can be very easily extended to MySQL. I have created 4 tables
in the database, namely:
- token_tb : stores the token_number, UserID and ContestID
- contest_tb : stores the ContestID, Contest_reward, Contest_date, Contest_name and expired (whether the contest is active or not)
- winners_tb : stores the ContestID, UserID and Rank
- users_tb : stores the UserID and User_name

**The figure demonstrates the database schema of the service**

![Alt text](db_schema.png?raw=true "database")


Please Note: I did not know a lot about frontend and thus the frontend of the project might not be upto the mark.
But I assure you that I like learning about new stuff and would be working on the frontend aspect soon.
