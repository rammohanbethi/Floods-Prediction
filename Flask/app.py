import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load
app = Flask(__name__)
model =load('floods.save')
sc=load('transform.save')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():

    x_test = [[float(x) for x in request.form.values()]]
    prediction = model.predict(sc.transform(x_test))
    print(prediction)
    output=prediction[0]
    if(output==0):
        pred="No floods"
    else:
        pred="There is a Chance of Floods"
    
    return render_template('portfolio.html', prediction_text='{}'.format(pred))

if __name__ == "__main__":
    app.run(debug=True)
