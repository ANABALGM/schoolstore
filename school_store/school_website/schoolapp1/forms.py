from django import forms
from .models import Department, Course, User, Material
from datetime import date

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['department', 'name']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'dob',
            'age',
            'gender',
            'phone_number',
            'email',
            'address',
            'department',
            'course',
            'purpose',
            'materials_provide',
        ]

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

        materials_provide = forms.ModelMultipleChoiceField(
            queryset=Material.objects.all(),
            widget=forms.CheckboxSelectMultiple,
        )


    def save(self, commit=True):
        instance = super().save(commit=False)
        dob = instance.dob
        if dob:
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            instance.age = age

        if commit:
            instance.save()

        return instance
