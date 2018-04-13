from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import ExperimentForm
from django.http import JsonResponse
import numpy as np
import pandas as pd
from logic.task import run_calc


@login_required(login_url=reverse_lazy('login'))
def index(request):
    return render(request, 'home.html')


def add_exp(request):
    if request.method == 'POST':
        form = ExperimentForm(request.POST, request.FILES)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.user = request.user
            exp_data = request.FILES['data']
            df = pd.read_excel(exp_data, sheet_name='Sheet1')
            exp.experimental_data = [list(df.as_matrix().T[0]), list(df.as_matrix().T[1])]
            let = request.FILES['let']
            exp.spectre = np.loadtxt(let, skiprows=23).tolist()
            exp.save()
            run_calc.delay(exp.pk)
            return redirect('home')
    else:
        form = ExperimentForm()
    return render(request, 'add_file.html', {'form': form})


# class ExpFormView(FormView):
#     form_class = ExpForm
#     success_url = "/"
#     template_name = "add_exp.html"
#
#     def form_valid(self, form):
#         exp = form.save(commit=False)
#         exp.user = self.request.user
#         exp.save()
#         return super(ExpFormView, self).form_valid(form)


# def add_exp(request):
#     if request.method == 'POST':
#         if request.is_ajax():
#             doc_form = DocumentForm(request.POST, request.FILES)
#             if doc_form.is_valid():
#                 doc = doc_form.save(commit=False)
#                 doc.user = request.user
#                 doc.save()
#                 data = {'is_valid': True, 'id': doc.id, 'name': doc.document.name}
#             else:
#                 data = {'is_valid': False}
#             return JsonResponse(data)
#         else:
#             form = ExpForm1(request.POST)
#             context = {'form': form}
#             if form.is_valid():
#                 print('pi')
#                 exp = form.save(commit=False)
#                 exp.user = request.user
#                 exp.save()
#                 return redirect('home')
#     else:
#         form = ExpForm1()
#         form.fields['doc'] = \
#             forms.ModelChoiceField(queryset=request.user.documents.all())
#         context = {'form': form, }
#     return render(request, 'add_exp.html', context)
#
#
# def check_exp(request):
#     user = request.user
#     exp = user.experiments.all()
#     return render(request, "check_exp.html", {'exp': exp})


# def add_file(request):
#     if request.method == 'POST' and request.is_ajax():
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             doc = form.save(commit=False)
#             doc.user = request.user
#             doc.save()
#             data = {'is_valid': True, 'id': doc.id, 'name': doc.document.name}
#         else:
#             data = {'is_valid': False}
#         return JsonResponse(data)
