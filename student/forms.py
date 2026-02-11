from django import forms

from .models import Search

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = '__all__'

        labels = {
                'student_name': 'Student Name :',
                'student_phonenumber' : 'Student Phone Number :',
                'student_email': 'Student Email :',
                'student_image': 'Student Image :',
        }
