from django.shortcuts import render

from .forms import MyForm


def my_view(request):
    if request.method == 'POST':
        form = MyForm(data=request.POST)
    else:
        form = MyForm()

    context = {'form': form}

    return render(request, 'bar/form.html', context)
