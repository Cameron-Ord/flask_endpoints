#importing
import json
from flask import Flask
import dbhelper

app = Flask(__name__)

@app.get('/api/clients')
def select_dogs():
   #function that returns the results from run_proceedure when using respective arguments as JSON
   results = dbhelper.run_proceedure('CALL return_all', [])
   if(type(results)==list):
    results_json = json.dumps(results, default=str)
   else:
      print('error')
   return results_json

#running @app
app.run(debug=True)
