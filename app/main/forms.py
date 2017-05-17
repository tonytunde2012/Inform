from app import db
from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class PremiseForm(FlaskForm):
    name = StringField('Premise Name', validators=[DataRequired(), Length(1, 64)])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Register')

class PatientForm(FlaskForm):
    patientName = StringField('Patient Name', validators=[DataRequired(), Length(1, 64)])
    patientID = IntegerField('PatientID')
    patientState = SelectField('State', choices=[('Uyo', 'Uyo'), ('Delta', 'Asaba')])
    patientLGA = SelectField('LGA', choices=[('Uyo', 'Uyo'), ('Abak', 'Abak')])


class Drug(FlaskForm):
    drugName = StringField('Drug Name', validators=[DataRequired(), Length(1, 64)])
    drugRoute = StringField('Route of Administration', validators=[DataRequired()])
    drugDose = IntegerField('Drug Dosage', validators=[DataRequired()])
    drugStrenght = IntegerField('Dosage Available', validators=[DataRequired()])
    drugDuration = StringField('Duration of Use', validators=[DataRequired()])
    submit = SubmitField('Dispensed')


# class GroupedForm(FlaskForm):
#     """A form for one or more addresses"""
#     drugs = FormField(Drug)
