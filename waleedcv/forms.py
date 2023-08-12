from django import forms 

from .models import contact_user

class Detail(forms.ModelForm):
    #class Meta :
        #model = contact_user
        #fields = "__all__"
    Name = forms.CharField(max_length=100)
    Subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    Message = forms.Textarea()