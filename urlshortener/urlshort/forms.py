from django import forms


class ShortenURLForm(forms.Form):
    long_url = forms.URLField(
        label='Enter a long URL',
        widget=forms.URLInput(attrs={'placeholder': 'https://example.com/very/long/url'}),
        required=True
    )
