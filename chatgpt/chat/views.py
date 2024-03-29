from django.http import JsonResponse
from django.shortcuts import render
import openai


# Create your views here.

openai_api_key = ''
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"You are a mental health assistant. Write a report about the mental health status"},
            {"role":"user","content":message}
        ]
    )
    answer = response.choices[0].message.content.strip()
    return answer

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message':message,'response':response})
    return render(request, 'chatbot.html')
