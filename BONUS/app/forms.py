def GNI_per_capita_calculator(health_index, poverty, malnourished_children):
    standardised_health_index = (int(health_index) - 0.814472222)/0.038261154
    standardised_poverty = (int(poverty) - 67.04166666)/10.80841686
    standardised_malnourished_children = (int(malnourished_children) - 8.063888889)/3.053973075
    
    return 9.4017284 + (0.0004079491360041523*standardised_health_index) + (0.4443462953972071*standardised_poverty) + (-0.0065212938429014666*standardised_malnourished_children)

from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

#form, found in predictor.html
class DataForm(FlaskForm):
    dataSize = FloatField('Training Data Size', validators=[
        DataRequired(),
        NumberRange(min=0, max=1, message='Value must be between 0 and 1')])
    health_index = FloatField('Health Index: Takes in a value BETWEEN 0 and 1', validators=[
        DataRequired(),
        NumberRange(min=0, max=1, message='Value must be between 0 and 1')])
    poverty = FloatField('Poverty: Takes in a percentage BETWEEN 0 and 100', validators=[
        DataRequired(),
        NumberRange(min=0, max=100, message='Value must be between 0 and 100')])
    malnourished_children = FloatField('Malnourished Children: Takes in a percentage BETWEEN 0 and 100', validators=[
        DataRequired(),
        NumberRange(min=0, max=100, message='Value must be between 0 and 100')])
    submit = SubmitField('Predict GNI')