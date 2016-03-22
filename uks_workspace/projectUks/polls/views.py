from audioop import reverse

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# from .models import User
#
# def index(request):
#     users = User.objects.all().order_by('-email')[:5]
#     context = {'users': users}
#     return render(request, 'polls/user/index.html', context)


