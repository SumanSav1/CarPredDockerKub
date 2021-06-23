from django import forms

FUEL_TYPE_CHOICES = [
    ('Petrol', 'Petrol'),
    ('Diesel', 'Diesel'),
    ('CNG', 'CNG'),
]
DEALER_CHOICES = [
    ('Dealer', 'Dealer'),
    ('Individual', 'Individual'),
]
TRANSMISSION_CHOICES = [
    ('Mannual', 'Manual Car'),
    ('Automatic', 'Automatic Car'),
]

class CarPredictionForm(forms.Form):
    year = forms.IntegerField()
    price = forms.IntegerField()
    kilometers = forms.IntegerField()
    owners = forms.IntegerField()
    fueltype = forms.ChoiceField(choices=FUEL_TYPE_CHOICES)
    dealer = forms.ChoiceField(choices=DEALER_CHOICES)
    transmissiontype = forms.ChoiceField(choices=TRANSMISSION_CHOICES)
