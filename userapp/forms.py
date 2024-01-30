from django import forms
from .models import usertable

class signupform(forms.ModelForm):
    gender = forms.ChoiceField(choices=usertable.Maleorfemale, widget=forms.RadioSelect)
    class Meta:
        model= usertable
        fields = ('firstname','lastname','username','email','phone','gender','password','confirm_password','pimage')
        
        widgets={
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'confirm_password':forms.TextInput(attrs={'class':'form-control'}),
            'pimage':forms.FileInput(attrs={'class':'form-control'}),
        }
    # def clean(self):
    #     cleaned_data=super
    #     password = cleaned_data.get('password')
    #     confirm_password = cleaned_data.get('confirm_password')

    #     if password != confirm_password:
    #         raise forms.ValidationError("Passwords do not match.")
        
    #     return confirm_password