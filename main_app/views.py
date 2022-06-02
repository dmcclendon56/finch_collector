from django.shortcuts import render
from django.views import View
from .models import dogs 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
# after our other imports 
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"       



class DogList(TemplateView):
    template_name = "dog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dogs"] = dogs.objects.all() 
        return context

class DogCreate(CreateView):
    model = dogs
    fields = ['name', 'img', 'type', 'AKC', 'CKC']
    template_name = "dog_create.html"
    success_url = "/doglist/"   

    # def get_success_url(self):
    #     return reverse('dog_detail', kwargs={'pk': self.object.pk})     


# class DogCreate(View):

#     def post(self, request, pk):
#         breed = request.POST.get("breed")
#         type = request.POST.get("description")
#         dog = dogs.objects.get(pk=pk)
#         dogs.objects.create(breed=breed, type=type, dog = dog)
#         return redirect('dog_list', pk=pk)

class DogDetail(DetailView):
    model = dogs
    template_name = "dog_detail.html"   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breeds"] = dogs.objects.all()
        return context 

class DogDelete(DeleteView):
    model = dogs
    template_name = "dog_delete_confirm.html"
    success_url = "/dog/"

class DogUpdate(UpdateView):
    model = dogs
    fields = ['breed', 'img', 'description', 'AKC/CKC']
    template_name = "dog_create.html"
    

    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})

# class DogDelete(DeleteView):
#     model = dogs
#     template_name = "dog_delete.html"
#     success_url = "/dog/"    