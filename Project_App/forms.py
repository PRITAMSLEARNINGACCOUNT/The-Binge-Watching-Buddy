from .models import ReviewModel, User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class ReviewFrom(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ["ReviewTitle", "ReviewMessage", "ReviewImageURL", "Type"]

    def __init__(self, *args, **kwargs):
        super(ReviewFrom, self).__init__(*args, **kwargs)
        self.fields['ReviewTitle'].widget.attrs.update({'class': 'h-10 w-40'})
        self.fields['ReviewMessage'].widget.attrs.update()
        self.fields['ReviewImageURL'].widget.attrs.update(
            {'class': 'border-l-amber-900 flex text-black gap-2 justify-center items-center text-center'})
        self.fields['Type'].widget.attrs.update()
        # Follow The Below Syntax To Add Custom Tailwind CSS Classes To A Django HTML Element
        # self.fields['Type'].widget.attrs.update(
        #     {'class': 'form-select mt-1 block w-full text-white'})


class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", 'password1', "password2")

    def __init__(self, *args, **kwargs):
        super(UserRegister, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'text-black'})
        self.fields['email'].widget.attrs.update({'class': 'text-black'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'text-black '})
        self.fields['password2'].widget.attrs.update({'class': 'text-black'})


class SearchForm(forms.Form):
    Search_Value = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields["Search_Value"].widget.attrs.update({
            "class": "text-black p-2 rounded-md"
        })
