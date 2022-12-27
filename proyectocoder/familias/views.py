from django.shortcuts import render, redirect, get_object_or_404
from .models import Familia
from .forms import MiembroForm

def familias_lista(request):
    familias = Familia.objects.all()
    return render(request, 'familias_lista.html', {'familias': familias})


def miembro_agregar(request, pk):
    familia = get_object_or_404(Familia, pk=pk)
    if request.method == 'POST':
        form = MiembroForm(request.POST)
        if form.is_valid():
            miembro = form.save(commit=False)
            miembro.familias.add(familia)
            miembro.save()
            return redirect('familias_lista')
    else:
        form = MiembroForm()
    return render(request, 'miembro_agregar.html', {'form': form, 'familia': familia})




