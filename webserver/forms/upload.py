from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    """
    Class that defines the file_upload form used in the homepage of the visualizer

    Inherits from FlaskForm"""

    json = FileField(validators=[DataRequired()])
    submit = SubmitField("Submit")
