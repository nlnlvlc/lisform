from django import forms
from .models import entry

class modelForm(forms.ModelForm):
    class Meta:
        model = entry
        fields = ['name', 'age', 'title', 'hometown']
        labels = {
            'name': "Name (required)",
            'age': "Age",
            'title': "Title (required)",
            'hometown': "Hometown"
                  }