from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator

from .models  import Crane, CraneContent, CraneImages, CraneRequest





class CranesListView(View):

    def get(self, request):
        queryset = Crane.objects.all()
        page_number = request.GET.get('page')
        paginator = Paginator(queryset, 6)
        queryset = paginator.get_page(page_number)

        return render(request, 'Cranes/cranes-list.html', {'cranes': queryset})




class CraneDetailView(View):

    def get(self, request, slug):
        crane = get_object_or_404(Crane, slug=slug)
        other_cranes = Crane.objects.all().order_by('?')
        return render(request, 'Cranes/crane-detail.html', {'crane': crane, 'other_cranes': other_cranes})