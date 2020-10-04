from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from people.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'email', 'problem_name',
                  'phone_number', 'problem_img')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))
