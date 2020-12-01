from django.shortcuts import render, redirect
from mytext import models
from .forms import RecordForm
from login.models import User


def index(request):
    return render(request, 'mytext/index.html')


def create(request):
    if request.method == 'POST':
        record_form = RecordForm(request.POST)
        if record_form.is_valid():

            user = User.objects.get(id=request.session['user_id'])
            # print("WHO")
            # print(user)

            new_record = models.Record()
            new_record.user = user
            new_record.time = record_form.cleaned_data['time']
            new_record.place = record_form.cleaned_data['place']
            new_record.note = record_form.cleaned_data['note']

            new_record.save()
            return redirect('/index')
    record_form = RecordForm()
    return render(request, 'mytext/create.html', locals())


def record(request):
    return render(request, 'mytext/record.html')


def search(request):
    # key = request.GET.get('key')
    user = User.objects.get(id=request.session['user_id'])
    post_list = user.record_set.all()
    return render(request, 'mytext/search.html', {'post_list': post_list})
