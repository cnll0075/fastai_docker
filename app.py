from flask import Flask, render_template, request
from fastai.vision import *

app = Flask('pet_predictor')

@app.route('/home')
@app.route('/')
def home_page():
    return '<h1>Pet Predictor'

@app.route('/try_post',methods = ['GET','POST'])
def try_post():
    res = ''
    if request.method =='POST':
        res = request.json['name']
    return f'hello {res}'

@app.route('/upload',methods = ['GET','POST'])
def upload_file():
    if request.method =='POST':
        f = request.files['file']
        f.save('uploaded_file')
    return 'file_uploaded'

@app.route('/predict',methods = ['GET','POST'])
def inference():
    if request.method == 'POST':
        f = request.files['file']
        f.save('requested_img')
        img = open_image('requested_img')
        model = load_learner('./',\
                            'export.pkl')
        res = model.predict(img)
        return str(res[0])
    
if __name__ == '__main__':
    app.run(debug=True)