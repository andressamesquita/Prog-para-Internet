from django.shortcuts import render
from pools.models import Question1

def index (request):
	return render(request, 'index.html', { 'pools':Question1.objects.all()})

def exibir(request, question_id):
	question = Question1.objects.get(id=question_id)
	return render(request, 'question.html', {"question":question})

