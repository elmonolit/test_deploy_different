from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages import get_messages
from .forms import UserProfileForm
from .models import UserProfile


class SignUpView(CreateView):
    form_class = UserCreationForm
    # profile = UserProfileForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'
    # def get_context_data(self, **kwargs):
    #     context = super(SignUpView,self).get_context_data()
    #     context.update({
    #         'profile': UserProfileForm
    #     })
    #     return context
    #
    # def form_valid(self, form):
    #     view = super(SignUpView, self).form_valid(form)
    #     username = form.cleaned_data.get('username')
    #     password = form.cleaned_data.get('password1')
    #     user = authenticate(username=username,password=password)
    #     login(self.request,user)
    #     print(self.request.POST)
    #     UserProfile.objects.get_or_create(user=user,email=email,pic=pic)
    #     return view





