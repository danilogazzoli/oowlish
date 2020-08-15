import django
from django import forms
from customers.models import Customer


class InsertCustomersForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "first_name", "last_name", "email", "gender", "company", "city", "title", "latitude", "longitude"
        ]