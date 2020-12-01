from django import forms


class RecordForm(forms.Form):
    time = forms.DateField(label='日期', widget=forms.DateInput(attrs={'type': 'date', 'style':'width:100%'}))
    place = forms.CharField(label="地点", max_length=128,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    note = forms.CharField(label="笔记", max_length=1000,
                           widget=forms.Textarea(attrs={'class': 'form-control'}))
