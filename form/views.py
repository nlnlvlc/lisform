from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import modelForm
from .models import entry

def home(request):
    if request.method == "POST":
        form = modelForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('form/success.html')
    else:
        form = modelForm()

    return render(request, "form/home.html", {"form": form})

def display_saved_data(request):
    all_data = entry.objects.all()
    submitted = entry.objects.last()
    context = {"data": all_data, "last": submitted}
    template = loader.get_template("form/success.html")
    return HttpResponse(template.render(context))