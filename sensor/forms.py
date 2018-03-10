from django import forms


class FiltersForm(forms.Form):
    date_from = forms.DateTimeField(label='Start date', widget=forms.TextInput(attrs={'class': 'datepicker'}))
    date_to = forms.DateTimeField(label='End date', widget=forms.TextInput(attrs={'class': 'datepicker'}))
