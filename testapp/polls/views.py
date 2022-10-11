# from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # output = ', '.join([question.question_text for question in latest_question_list])
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})
    # return HttpResponse("You are looking at question {}".format(question_id))

def results(request, question_id):
    response = "You are looking at the results of question{}".format(question_id)
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("Your are voting on question {}".format(question_id))