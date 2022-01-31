from django import forms


class FilterForm(forms.Form):
    FILTER_CHOICES = (
        ('some', '------------------'),
        ('askstories', 'askstories'),
        ('jobstories', 'jobstories'),
        ('showstories', 'showstories'),
    )

    choose_your_category = forms.ChoiceField(choices=FILTER_CHOICES)
