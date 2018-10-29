from django import forms 
from .models import Aktiviti
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div,Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText,PrependedText, FormActions



# Jemputan Aktiviti form
class AktivitiForm(forms.ModelForm):

	class Meta:
		model = Aktiviti
		fields = ('tajuk','tempat','penceramah','hadpeserta',)

