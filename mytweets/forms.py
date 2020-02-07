from django import forms


class TweetForm(forms.Form):
    """
    Form to submit a tweet
    """

    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 85}), max_length=160)
    country = forms.CharField(widget=forms.HiddenInput())


class SearchForm(forms.Form):
    """
    Form to search tweets
    """

    query = forms.CharField(label="Enter a keyword to search for")
    widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control'})
