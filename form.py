from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField 
from wtforms.validators import DataRequired, NumberRange

class InputForm(FlaskForm):
    
    # All fields below are now FloatField to accept decimal inputs
    radius_mean=FloatField("radius_mean",validators=[DataRequired(),NumberRange(3,30)])

    texture_mean=FloatField("texture_mean",validators=[DataRequired(),NumberRange(4,40)])

    perimeter_mean=FloatField("perimeter_mean",validators=[DataRequired(),NumberRange(20,200)])

    area_mean=FloatField("area_mean",validators=[DataRequired(),NumberRange(140,1000)])

    smoothness_mean=FloatField("smoothness_mean",validators=[DataRequired(),NumberRange(0,1.2)])

    compactness_mean=FloatField("compactness_mean",validators=[DataRequired(),NumberRange(0,0.5)])

    concavity_mean=FloatField("concavity_mean",validators=[DataRequired(),NumberRange(0,0.5)])

    concave_points_mean=FloatField("concave_points_mean",validators=[DataRequired(),NumberRange(0,0.5)])

    symmetry_mean=FloatField("symmetry_mean",validators=[DataRequired(),NumberRange(0,0.5)])

    fractal_dimension_mean=FloatField("fractal_dimension_mean",validators=[DataRequired(),NumberRange(0,0.1)])

    radius_se=FloatField("radius_se",validators=[DataRequired(),NumberRange(0,5)])

    texture_se=FloatField("texture_se",validators=[DataRequired(),NumberRange(0,5)])

    perimeter_se=FloatField("perimeter_se",validators=[DataRequired(),NumberRange(0,25)])

    area_se=FloatField("area_se",validators=[DataRequired(),NumberRange(0,500)])

    smoothness_se=FloatField("smoothness_se",validators=[DataRequired(),NumberRange(0,0.1)])

    compactness_se=FloatField("compactness_se",validators=[DataRequired(),NumberRange(0,0.5)])

    concavity_se=FloatField("concavity_se",validators=[DataRequired(),NumberRange(0,0.5)])

    concave_points_se=FloatField("concave_points_se",validators=[DataRequired(),NumberRange(0,0.1)])

    symmetry_se=FloatField("symmetry_se",validators=[DataRequired(),NumberRange(0,0.1)])

    fractal_dimension_se=FloatField("fractal_dimension_se",validators=[DataRequired(),NumberRange(0,0.1)])

    radius_worst=FloatField("radius_worst",validators=[DataRequired(),NumberRange(4,30)])

    texture_worst=FloatField("texture_worst",validators=[DataRequired(),NumberRange(6,50)])

    perimeter_worst=FloatField("perimeter_worst",validators=[DataRequired(),NumberRange(30,250)])

    area_worst=FloatField("area_worst",validators=[DataRequired(),NumberRange(180,1000)])

    smoothness_worst=FloatField("smoothness_worst",validators=[DataRequired(),NumberRange(0,0.5)])

    compactness_worst=FloatField("compactness_worst",validators=[DataRequired(),NumberRange(0,1)])
    
    concavity_worst=FloatField("concavity_worst",validators=[DataRequired(),NumberRange(0,1.5)])
    
    concave_points_worst=FloatField("concave_points_worst",validators=[DataRequired(),NumberRange(0,0.5)])
    
    symmetry_worst=FloatField("symmetry_worst",validators=[DataRequired(),NumberRange(0,0.5)])
    
    fractal_dimension_worst=FloatField("fractal_dimension_worst",validators=[DataRequired(),NumberRange(0,0.5)])

    submit = SubmitField('Predict')
