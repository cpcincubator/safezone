from django import forms

from models import Report

class Addreportform(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['report_type','date','time','location','report_title','description']
