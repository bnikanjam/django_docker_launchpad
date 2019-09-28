from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField()
    email_to = forms.EmailField()
    email_from = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
