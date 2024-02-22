from django import forms
 


from .models import Person, Categories, Article

class PersonForm(forms.Form):
        username = forms.CharField()
        email = forms.EmailField()
        age = forms.IntegerField()

class Categories_Form(forms.Form):
    name = forms.CharField()
    typi = forms.CharField()


class article_Form(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField()
    publication_date = forms.DateField()
    category = forms.ModelMultipleChoiceField(
            label = 'articel_category',
            queryset= Categories.objects.all(),
            widget = forms.CheckboxSelectMultiple(attrs={
                  'class': 'from-check-input'
            })
      )
    
    
class ArticleForm(forms.ModelForm):
        class Meta:
            model = Categories
            fields = '__all__'
    

