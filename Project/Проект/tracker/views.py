from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import HabitCreate
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from datetime import datetime, timedelta, date
from django.db.models import Count
from .models import Habit

class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            date = datetime.now()
            time_delta = (date - request.last_date).days - request.frequency

            habits_list = Habit.objects.filter(user=request.user, )

            
            
            # time_delta = (date - (date - timedelta(5))).days

            context = {'habits_list':habits_list,
                    #    'time_delta':time_delta,
                       }

            return render(request, 'tracker/index.html', context)
        else:
            return redirect('/login')
    
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/signup.html', {'form': form})
    
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно вошли в систему')
                return redirect('index')
        messages.error(request, 'Неверные учётные данные.')
        return render(request, 'tracker/login.html', {'login_form': form})
    form = AuthenticationForm()
    return render(request, 'tracker/login.html', {'login_form': form})


def logout_user(request):
   logout(request)
   return redirect('index')

@login_required
def profile_user(request):
    return render(request, 'tracker/profile.html')

class HabitCreateView(LoginRequiredMixin, CreateView):
    model = Habit
    form_class = HabitCreate
    template_name = 'tracker/habit_maker.html'
    success_url = '/'

    def form_valid(self, form):
        # Устанавливаем автора и дату создания перед сохранением
        form.instance.user = self.request.user
        form.instance.created_at = timezone.now()
        return super().form_valid(form)