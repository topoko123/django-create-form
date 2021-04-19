from django import forms
from django.forms.formsets import formset_factory

class ChrFieldForm(forms.Form):
    login = forms.CharField(
        label='',
        required=False,
        max_length=20,
        min_length=4,
        widget=forms.TextInput(attrs= {
            'placeholder': 'ล็อกอิน',
            'size': '20'
        })
    )

    pswd = forms.CharField(
        label='',
        required=False,
        max_length=10,
        min_length=4,
        widget=forms.PasswordInput(attrs= {
            'placeholder': 'รหัสผ่าน',
            'size': '20'
        })
    )

    memo = forms.CharField(
        label='',
        required=False,
        max_length=150,
        widget=forms.Textarea(attrs= {
            'placeholder': 'บันทึก',
            'cols': '30',
            'rows': '3'
        })
    )

class NumberForm(forms.Form):
    quantity = forms.IntegerField(
        label='',
        required=False,
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={
          'placeholder': 'จำนวน',
          'value': '1'  
        })
    )

    price = forms.FloatField(
        label='',
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'ราคา'})
    )

class EmailURLForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        required=False
    )

    website = forms.URLField(
        label='endpoint',
        required=False,
        widget=forms.URLInput(attrs={'sieze': 40})
    )

class BooleanForm(forms.Form):
    save = forms.BooleanField(
        label='จัดเก็บข้อมูล',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'value': 'Save',
            'checked': False            
        })
    )

class ChoiceForm(forms.Form):
    ch_colors = [('#ff0000', 'Red'), ('#00ff00', 'Green'), ('#0000ff', 'Blue')]

    color = forms.ChoiceField(
        choices=ch_colors,
        label='Color',
        required=False,
        widget=forms.RadioSelect
    )

    ch_style = [('<b>', 'Bold'), ('<i>', 'Italic'), ('<u>', 'Underline')]

    font_style = forms.MultipleChoiceField(
        choices=ch_style,
        label='Font Style',
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    ch_sizes = [('14px', 'Small'), ('16px', 'Medium'), ('20px', 'Large')]

    font_size = forms.ChoiceField(
        choices=ch_sizes,
        label='Font Size',
        required=False,
        widget=forms.Select
    )

    ch_families = [('Tahoma', 'Tahoma'), ('Arial', 'Arial'),
                   ('Times new Roman', 'Times new Roman'),
                   ('Microsoft Sans Serif', 'Microsoft Sans Serif')]

    font_family = forms.MultipleChoiceField(
        choices=ch_families,
        label='Font Family',
        required=False,
        widget=forms.SelectMultiple
    )