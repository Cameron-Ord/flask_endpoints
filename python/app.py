#importing
import json
from flask import Flask, request
import dbhelper

app = Flask(__name__)

@app.get('/api/clients')
def select_dogs():
   #function that returns the results from run_proceedure when using respective arguments as JSON
   results = dbhelper.run_proceedure('CALL return_all', [])
   if(type(results)==list):
    return json.dumps(results, default=str)
   else:
     return "something has gone wrong"
 

#running @app



@app.get('/api/loyal_clients')
def loyal_clients():
   #function that returns the results from run_proceedure when using respective arguments as JSON
   max_points = request.args.get('max_points')
   results = dbhelper.run_proceedure('CALL loyal_clients(?)', [max_points])
   if(type(results)==list):
    return json.dumps(results, default=str)
   else:
      return "something has gone wrong"



app.run(debug=True)