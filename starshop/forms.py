from django import forms
from .models import Star


class Shop(forms.ModelForm):
    class Meta:
        model = Star
        fields = '__all__'
        
#class TagForm(forms.Form):
    #name = forms.CharField(max_length=40, help_text='A label for URL')
    
   # def save(self):
           # newTag = Tag.objects.create(
           #  name= self.cleaned_data['name'])
           # return newTag
        

        
        