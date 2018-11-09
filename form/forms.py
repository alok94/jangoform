from django import forms

class myform (forms.Form):
 First_Name=forms.CharField(max_length=50)
 Last_Name=forms.CharField(max_length=50)
 Email=forms.EmailField(max_length=50)
 password=forms.CharField(max_length=50)
