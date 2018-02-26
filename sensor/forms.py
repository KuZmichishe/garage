from django import forms


class FiltersForm(forms.Form):
    date_from = forms.DateTimeField(label='Start date')
    date_to = forms.DateTimeField(label='End date')
