# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from .models import Project
from forms import UserRegisterForm, UserLoginForm, AddProjectForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect


class IndexView(generic.ListView):
    template_name = 'dev/index.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_queryset(self):
        return Project.objects.get_queryset().order_by('-id')


class AddUser(generic.View):
    form_class = UserRegisterForm
    template_name = 'dev/register-form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.username = username
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
        return redirect('home')


class UserLogin(generic.View):
    form_class = UserLoginForm
    template_name = 'dev/login-form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')


class AddProject(generic.CreateView):
    form_class = AddProjectForm
    template_name = 'dev/add-project.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(AddProject, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('home')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(AddProject, self).form_valid(form)


def logout_user(request):
    logout(request)
    return redirect('/')


class ViewUser(generic.DetailView):
    model = User
    template_name = 'dev/UserDetail.html'
    context_object_name = 'user'


class ProjectDelete(generic.DeleteView):
    model = Project
    success_url = reverse_lazy('home')

