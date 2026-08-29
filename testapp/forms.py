from django import forms
from testapp.models import Chatbot
class ChatbotForm(forms.ModelForm):
    class Meta:
        model = Chatbot
        fields = '__all__'
        widgets = {
            'Ask_A_Question': forms.TextInput(attrs={
                'placeholder': 'Type your question here...',
                'class': 'form-control',  
            }),
        }

        