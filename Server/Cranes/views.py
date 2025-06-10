from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.paginator import Paginator

from .forms import CraneRequestForm

from .models  import Crane, CraneRequest





class CranesListView(View):

    def get(self, request):
        queryset = Crane.objects.all()
        page_number = request.GET.get('page')
        paginator = Paginator(queryset, 6)
        queryset = paginator.get_page(page_number)

        return render(request, 'Cranes/cranes-list.html', {'cranes': queryset})




class CraneDetailView(View):

    def get(self, request, slug):
        form = CraneRequestForm()
        crane = get_object_or_404(Crane, slug=slug)
        other_cranes = Crane.objects.all().order_by('?')
        return render(request, 'Cranes/crane-detail.html', {'crane': crane, 'other_cranes': other_cranes, 'form': form})
    
    def post(self, request, slug):
        form = CraneRequestForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            crane = get_object_or_404(Crane, slug=slug)
            
            instance = CraneRequest.objects.create(
                crane=crane,
                f_name=cd['f_name'],
                l_name=cd['l_name'],
                title=cd['title'],
                phone=cd['phone'],
                email=cd['email'],
                content=cd['content']
            )
            instance.save()

            return redirect('cranes:crane-detail', slug)
        
        return render(request, 'cranes/crane-detail.html', {'crane': instance, 'form': form})