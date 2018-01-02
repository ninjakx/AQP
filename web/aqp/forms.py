'''from .models import Data
from django import forms

class DataForms(forms.ModelForm):
    class Meta:
        model = Data
        fields = ["year","RPS","Tdeath","tw","ar","bs","tx","gv","tv","pop"]
'''
#from .models import User
from django.forms import Form,ModelForm
from django.forms import ChoiceField,Select
'''
{% load staticfiles %}

  



<img src="{% static "media/map_delhi.jpg" %}" />

class Detail(ModelForm):

    class Meta:
        model = Data
        fields = ['Year','RPD_deaths','Total_deaths','Four_wheelers','Two_wheelers','Auto_rickshaw','Buses','Taxis',
'Good_vehicles','Total_vehicles','Population']
'''

class Form1(Form):
    From = ChoiceField(widget=Select(attrs={'class': 'form-control col-xs-1'}),label='',choices=[(x, x) for x in ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']])
    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        # Default value
        self.initial['From'] = '2001'
class Form2(Form):
    To = ChoiceField(widget=Select(attrs={'class': 'form-control col-xs-1'}),label='',choices=[(x, x) for x in ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']])

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        self.initial['To'] = '2015'

