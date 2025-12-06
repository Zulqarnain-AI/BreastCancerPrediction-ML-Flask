from flask import Flask,render_template
import pandas as pd
import joblib
from form import InputForm

app=Flask(__name__)
app.config['SECRET_KEY']='MY_KEY'

model=joblib.load('breast_cancer_predicter.joblib')


@app.route('/', methods=['GET', 'POST'])
def home():
    forms= InputForm()
    message=None
    if forms.validate_on_submit():
        list = pd.DataFrame([{
            'radius_mean':9.029,
            'texture_mean':17.33,
            'perimeter_mean':58.79,
            'area_mean':250.5,
            'smoothness_mean':0.10660,
            'compactness_mean':0.14130,
            'concavity_mean':0.31300,
            'concave points_mean':0.04375,
            'symmetry_mean':0.2111,
            'fractal_dimension_mean':0.08046,
            'radius_se':0.3274,
            'texture_se':1.1940,
            'perimeter_se':1.885,
            'area_se':17.67,
            'smoothness_se':0.009549,
            'compactness_se':0.08606,
            'concavity_se':0.303800,
            'concave points_se':0.033220,
            'symmetry_se':0.04197,
            'fractal_dimension_se':0.009559,
            'radius_worst':10.310,
            'texture_worst':22.65,
            'perimeter_worst':65.50	,
            'area_worst':324.7,
            'smoothness_worst':0.14820,
            'compactness_worst':0.43650,
            'concavity_worst':1.25200	,
            'concave points_worst':0.17500,
            'symmetry_worst':0.4228,
            'fractal_dimension_worst':0.11750}])

        prediction = model.predict(list)
        if prediction =="B":
            message ="Benign" 

        else:
            message="Malignant"
        return render_template('predict.html',message=message,form=forms)

    return render_template('predict.html',message=message,form=forms)


if __name__ == "__main__":
    app.run(debug=True)
