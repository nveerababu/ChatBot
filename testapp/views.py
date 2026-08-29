import os
from pathlib import Path
from dotenv import load_dotenv
from django.shortcuts import render
from testapp.models import Chatbot
from testapp.forms import ChatbotForm
from django.conf import settings
def chatbot_view(request):
        return render(request,'index.html',{'chatbot_view':chatbot_view})    
def history_view(request):
    history_list = Chatbot.objects.all()
    return render(request,'history.html',{'history_list':history_list})
from django.shortcuts import render
from django.conf import settings
import google.generativeai as genai
from testapp.forms import ChatbotForm

genai.configure(api_key=settings.GEMINI_API_KEY)
def index_view(request):
    form = ChatbotForm()
    response_text = ""

    if request.method == 'POST':
        form = ChatbotForm(request.POST)
        if form.is_valid():
            chatbot_instance = form.save()
            user_question = chatbot_instance.Ask_A_Question  

            try:
                model = genai.GenerativeModel('gemini-3.6-flash')
                response = model.generate_content(user_question)
                response_text = response.text
            except Exception as e:
                response_text = f"Error: {e}"

    context = {
        'form': form,
        'response': response_text
    }
    return render(request, 'index.html', context)