from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.password_validation import password_changed
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView, View
from user.forms import RegistrationForm, LoginUserForm



class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        messages.success(self.request, 'Регистрация прошла успешно!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Исправьте ошибки в форме')
        return super().form_invalid(form)


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user and user.is_active:
                login(request,user)
                return redirect('index')
        else:
            form = LoginUserForm()
        return render(request, 'login.html', {'form':form})


def logout_user(request):
    logout(request)
    return redirect('index')

