from django import forms
from .models import Todo
from django.core.exceptions import ValidationError

    # def clean_text(self,*args,**kwargs):
    #     text=self.cleaned_data.get("text")
    #     todo_items=Todo.objects.all()
    #     if text in todo_items:
    #         raise forms.ValidationError("you already enter that message")




class SearchForm(forms.ModelForm):
    text=forms.CharField( label="")
    class Meta:
        model = Todo
        fields=[
               'text'
        ]


    def clean_text(self):
        text=self.cleaned_data.get("text")
        print(text)
        todo_items=Todo.objects.all()
        # a=[]
        # for i in todo_items:
        #     a.append(i)
        # print(a.split(",")[])

        if text in todo_items:
            raise forms.ValidationError("you already enter that message")
        else:
            print("kllls")
            return text
