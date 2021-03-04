from django import forms
from app.models import Labreport


# class DocumentForm(forms.Form):
#     Name = forms.CharField(max_length=40)
#     Phone = forms.IntegerField()
#     Lab_Number = forms.IntegerField()
#     report = forms.FileField()


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Labreport
        fields = ('Name', 'Phone','Lab_Number','report' )
