from django import forms

class orderDetails(forms.Form):
    rollNo = forms.IntegerField(required=True)
    rollNo.widget = forms.NumberInput(attrs={" "})
    itemName = forms.CharField(max_length = 200, required=True)
    itemName.widget = forms.TextInput(attrs={'placeholder':'what food did you ordered',})
    company = forms.CharField(label="Who iz gonna deliver:")
    company.widget = forms.Select(choices=[
        'zomato':'Zomato',
        'swiggy' : 'Swiggy',
        'other' : 'other',
    ])
    deliveryGuyContact = forms.IntegerField(required = True)
    deliveryGuyContact.widget = forms.NumberInput(attrs={})
