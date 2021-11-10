from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from store.models import Product


batch_choices = [(i, i) for i in range(2012, 2021)]
department_choices = [
    ('chem', 'Department of Chemical Science and Engineering'),
    ('civil', 'Department of Civil Engineering'),
    ('comp', 'Department of Computer Science and Engineering'),
    ('mech', 'Department of Mechanical Engineering'),
    ('elec', 'Department of Electrical and Electronics Engineering'),
    ('geo', 'Department of Geomatics Engineering'),
]
semester_choices = [
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (7, 'VII'),
    (8, 'VIII'),
]

category_choices = [
    ('Electronics', 'Electronics'),
    ('Homes and Furnitures', 'Furnitures'),
    ('Sports', 'Sports'),
    ('Education Materials', 'Education Materials'),
    ('Other Accessories', 'Other Accessories'),
]

subcategory1_choices = [
    ('1st Year', '1st Year'),
    ('2nd Year', '2nd Year'),
    ('3rd Year', '3rd Year'),
    ('4th Year', '4th Year'),
    ('Labcoats', 'Labcoats'),
    ('Drafters', 'Drafters'),
]

subcategory2_choices = [
    ('Books', 'Books'),
    ('Notes', 'Notes'),
]

negotiation_choices = [
    (True, "Yes"),
    (False, "No")
]

urgent_choices = [
    (True, 'Yes'),
    (False, 'No')
]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(help_text='First name')
    last_name = forms.CharField(help_text='Last name')
    email = forms.EmailField(help_text='Email address')
    dob = forms.DateField(help_text='Date of birth', widget=forms.TextInput(
        attrs={'placeholder': 'Format: YYYY-MM-DD'}))
    batch = forms.IntegerField(widget=forms.Select(choices=batch_choices))
    department = forms.CharField(
        widget=forms.Select(choices=department_choices))
    group = forms.CharField()
    semester = forms.CharField(widget=forms.Select(choices=semester_choices))
    phone_no = forms.CharField()

    class meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',
                  'dob', 'batch', 'department', 'group', 'semester', 'phone_no')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            "username": forms.TextInput(attrs={'class': 'input-field', 'help_text': 'Your Username'},),
            "email": forms.EmailInput(attrs={'class': 'input-field'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_no', 'image']


class ProductForm(forms.ModelForm):
    name = forms.CharField()
    category = forms.CharField(widget=forms.Select(choices=category_choices))
    sub_category1 = forms.CharField(
        widget=forms.Select(choices=subcategory1_choices))
    sub_category2 = forms.CharField(
        widget=forms.Select(choices=subcategory2_choices))
    price = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    negotiation = forms.ChoiceField(choices=negotiation_choices,
                                    widget=forms.Select())

    img = forms.ImageField()
    contact_info = forms.CharField()
    urgent = forms.ChoiceField(choices=urgent_choices, widget=forms.Select(
    ))

    class Meta:
        model = Product
        fields = ['name', 'category', 'sub_category1', 'sub_category2', 'price',
                  'description', 'negotiation', 'img', 'contact_info', 'urgent']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'Hello', 'help_text': 'Your Username'}),
        }
