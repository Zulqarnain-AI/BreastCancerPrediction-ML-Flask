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
        data = pd.DataFrame([{
            'radius_mean': forms.radius_mean.data,
            'texture_mean': forms.texture_mean.data,
            'perimeter_mean': forms.perimeter_mean.data,
            'area_mean': forms.area_mean.data,
            'smoothness_mean': forms.smoothness_mean.data,
            'compactness_mean': forms.compactness_mean.data,
            'concavity_mean': forms.concavity_mean.data,
            'concave points_mean': forms.concave_points_mean.data,
            'symmetry_mean': forms.symmetry_mean.data,
            'fractal_dimension_mean': forms.fractal_dimension_mean.data,
            'radius_se': forms.radius_se.data,
            'texture_se': forms.texture_se.data,
            'perimeter_se': forms.perimeter_se.data,
            'area_se': forms.area_se.data,
            'smoothness_se': forms.smoothness_se.data,
            'compactness_se': forms.compactness_se.data,
            'concavity_se': forms.concavity_se.data,
            'concave points_se': forms.concave_points_se.data,
            'symmetry_se': forms.symmetry_se.data,
            'fractal_dimension_se': forms.fractal_dimension_se.data,
            'radius_worst': forms.radius_worst.data,
            'texture_worst': forms.texture_worst.data,
            'perimeter_worst': forms.perimeter_worst.data,
            'area_worst': forms.area_worst.data,
            'smoothness_worst': forms.smoothness_worst.data,
            'compactness_worst': forms.compactness_worst.data,
            'concavity_worst': forms.concavity_worst.data,
            'concave points_worst': forms.concave_points_worst.data,
            'symmetry_worst': forms.symmetry_worst.data,
            'fractal_dimension_worst': forms.fractal_dimension_worst.data}])


        prediction = model.predict(data)
        if prediction[0] == "B":
            message ="<h2>based on your input data<h2> <h1>the model predict: Benign<h1>" 

        else:
            message="<h2>based on your input data<h2> <h1>the model predict:<bold > Malignant <bold><h1>"
        return render_template('predict.html',message=message,form=forms)

    return render_template('predict.html',message=message,form=forms)


if __name__ == "__main__":
    app.run(debug=True)
