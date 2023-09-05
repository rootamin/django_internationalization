from django.shortcuts import render
from .models import Post
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


def index(request):

    if request.user.is_authenticated:
        messages.success(request, _("authmessage {first} {last}").format(first=request.user.first_name, last=request.user.last_name), extra_tags="alert alert-success")
    else:
        messages.warning(request, _("anonmessage"), extra_tags="alert alert-danger")

    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'index.html', context)