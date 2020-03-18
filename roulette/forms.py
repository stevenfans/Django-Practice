from django import forms

class FormName(forms.Form):
    
    test_choice = [('question','Question'), ('other','Other'), ('test','Test')]

    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField(choices=test_choice, 
                                 widget=forms.Select(attrs={'class':'form-control'})
                                 )

class Filter(forms.Form):
    rating_choices=[('1 star','1 Star'),
                    ('2 star','2 Star'),
                    ('3 star','3 Star'),
                    ('4 star','4 Star'),
                    ('5 star','5 Star')]

    price_choices=[('$','$'),
                   ('$$','$$'),
                   ('$$$','$$$')]

    radius_choices=[('5 mi', '5 mi'),
                    ('10 mi', '10 mi'),
                    ('15  mi', '15 mi')]

    rating = forms.ChoiceField(choices=rating_choices,
                               widget=forms.Select(attrs={'class':'form-control'})
                               )

    price = forms.ChoiceField(choices=price_choices,
                              widget=forms.Select(attrs={'class':'form-control'})
                              )

    radius = forms.ChoiceField(choices=radius_choices,
                               widget=forms.Select(attrs={'class':'form-control'})
                               )