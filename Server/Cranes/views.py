from django.shortcuts import render, get_object_or_404
from django.views import View

from .models  import Crane, CraneContent, CraneImages, CraneRequest





class CranesListView(View):

    def get(self, request):
        cranes = Crane.objects.filter(status="P")
        return render(request, 'Cranes/crane-list.html', {'cranes': cranes})




class CraneDetailView(View):

    def get(self, request, slug):
        crane = get_object_or_404(Crane, slug=slug)
        return render(request, 'Cranes/crane-detail.html', {'crane': crane})