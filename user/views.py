import threading
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from user.forms import PollForm
from user.models import Poll
from django.db import transaction

def index(request:HttpRequest):
    form = PollForm()
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            cleaned_name = form.cleaned_data.get('name')
            print(f"Caller Thread Id : {threading.current_thread().ident}")
            try:
                with transaction.atomic():
                    poll_object = Poll.objects.create(name=cleaned_name)
            except Exception as e:
                print(f"Error {e}")
        return HttpResponse('<h1 style="background-color:grey; text-align:center;">Hello world</h1>')
    return render(request, './index.html', {'form': form})

