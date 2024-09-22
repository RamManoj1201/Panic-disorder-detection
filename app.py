import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

import warnings
warnings.filterwarnings("ignore")

# Load the model
model = pickle.load(open("knn (1).pkl", "rb"))

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Index route
@app.route('/input')
def input():
    return render_template('input.html')

# Submit route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    print('in submit')
    # Get form data with default values if keys are missing
    Coping_Mechanisms = request.form.get("Coping_Mechanisms", "0")
    Current_Stressors = request.form.get("Current_Stressors", "0")
    Demographics = request.form.get("Demographics", "0")
    Family_History = request.form.get("Family_History", "0")
    Gender = request.form.get("Gender", "0")
    Impact_on_Life = request.form.get("Impact_on_Life", "0")
    Symptoms = request.form.get("Symptoms", "0")

    # Print received data for debugging
    print([[Coping_Mechanisms, Current_Stressors, Demographics, Family_History, Gender, Impact_on_Life, Symptoms]])

    preds = None
    try:
        preds = model.predict([[Coping_Mechanisms, Current_Stressors, Demographics, Family_History, Gender, Impact_on_Life, Symptoms]])
        print(preds)
    except Exception as e:
        print(e)
    
    if preds == 0:
        return render_template("output.html", result='Patient might face panic disorder')
    else:
        return render_template("output.html", result='Patient is normal')
# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=4000)
