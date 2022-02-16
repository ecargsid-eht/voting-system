from tkinter.messagebox import QUESTION
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404
from .models import *
from django.urls import reverse
# Create your views here.
from django.views import generic

class IndexView(generic.ListView):
    template_name = "home.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


# def index(r):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_question_list" :latest_question_list
#     }
#     return render(r,"home.html",context)

class DetailsView(generic.DetailView):
    model = Question
    template_name = "details.html"


# def details(r,question_id):
#     question = get_object_or_404(Question,pk=question_id)
    
#     return render(r,"details.html",{"question":question})

class ResultView(generic.DetailView):
    model = Question
    template_name = "results.html"
    
# def results(r,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(r,"results.html",{"question":question})


def vote(r,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=r.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(r,"details.html",{
            'question':question,
            'error_message':"you did not select choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("results", args=(question.id,)))

    
