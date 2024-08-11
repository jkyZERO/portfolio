from django import forms
from .models import Skill, Project

#определяет форму через django forms

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name','description']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','image','url','skills']
