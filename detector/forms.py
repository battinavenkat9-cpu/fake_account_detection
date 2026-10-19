from django import forms

class AccountAnalysisForm(forms.Form):
    username = forms.CharField(max_length=80, label="Username", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. sample_user"}))
    followers = forms.IntegerField(min_value=0, max_value=100_000_000, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "e.g. 250"}))
    following = forms.IntegerField(min_value=0, max_value=100_000_000, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "e.g. 300"}))
    posts = forms.IntegerField(min_value=0, max_value=10_000_000, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "e.g. 120"}))
    account_age_days = forms.IntegerField(min_value=0, max_value=36500, label="Account age (days)", widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "e.g. 900"}))
    bio_length = forms.IntegerField(min_value=0, max_value=10000, label="Bio length (characters)", required=False, initial=0, widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "e.g. 80"}))
    has_profile_picture = forms.ChoiceField(label="Has profile picture?", choices=[("yes", "Yes"), ("no", "No")], widget=forms.Select(attrs={"class": "form-select"}))

    def clean_username(self):
        username = self.cleaned_data["username"].strip().lstrip("@")
        if not username:
            raise forms.ValidationError("Enter a username.")
        return username
