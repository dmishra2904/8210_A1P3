from django import forms
from .models import Customer, Service, Product
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_name', 'organization', 'role', 'bldgroom', 'account_number', 'address', 'city', 'state',
                  'zipcode', 'email','phone_number')


class ServiceForm(forms.ModelForm):
   class Meta:
       model = Service
       fields = ('cust_name', 'service_category', 'description', 'location', 'setup_time', 'cleanup_time', 'service_charge' )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('cust_name', 'product', 'p_description', 'quantity', 'pickup_time', 'charge')