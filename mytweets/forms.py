from django import forms


class TweetForm(forms.Form):
    """
    Form to submit a tweet
    """

    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 85}), max_length=160)
    country = forms.CharField(widget=forms.HiddenInput())
