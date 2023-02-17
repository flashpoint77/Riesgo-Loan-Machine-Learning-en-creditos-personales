from distutils.log import debug
from flask import Flask, escape, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method ==  'POST':
          income= float(request.form['income'])
          age=request.form['age']
          married= request.form['married']
          House_Ownership = request.form['House_Ownership']
          Car_Ownership= request.form['Car_Ownership']
          CURRENT_JOB_YRS = request.form['CURRENT_JOB_YRS']
          CURRENT_HOUSE_YRS = request.form['CURRENT_HOUSE_YRS']
        

          # married
          if(married=="Si"):
           married_yes = 1
          else:
               married_yes=0
	 
          # casa propia
          if(House_Ownership=="Si"):
            House_Ownership_yes=1
          else:
               House_Ownership_yes=0
	   
          # vehiculo propio
          if(Car_Ownership== "Si"):
            Car_Ownership_yes=1
          else:
               Car_Ownership_yes=0        


        

          prediction = model.predict([[income, age, married_yes, House_Ownership_yes, Car_Ownership_yes, CURRENT_JOB_YRS, CURRENT_HOUSE_YRS]])

          # print(prediction)

          if(prediction==0):
             prediction="BAJO RIESGO"
          else:
            prediction="ALTO RIESGO"


          return render_template("predict_form.html", prediction_text="Morosidad con {}".format(prediction))




    else:
        return render_template("predict_form.html")



if __name__ == "__main__":
    app.run(debug=True)