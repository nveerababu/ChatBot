from django.contrib import admin
from django.contrib import admin
from testapp.models import Chatbot
class ChatbotAdmin(admin.ModelAdmin):
    list_display = ['Ask_A_Question'] 
admin.site.register(Chatbot, ChatbotAdmin)    

