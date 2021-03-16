from django.views.generic import TemplateView, CreateView, DeleteView
from . import forms
from django.urls import reverse_lazy
from . import models


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'book/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        search_by = self.request.GET.get('search_by')
        query = self.request.GET.get("query")
        search_message = 'All phones'
        if search_by in ['phone', 'name'] and query:
            if search_by == 'name':
                persones = models.Person.objects.filter(name__startswith=query)
                search_message = f'Поиск по имени - "{query}"'
            else:
                persones = models.Person.objects.filter(phones__phone__startswith=query)
                search_message = f'Поиск по номеру - "{query}"'
            context["persones"] = persones
            context["search_message"] = search_message
            return context

        context["persones"] = models.Person.objects.all()
        return context

class AddPhoneFormView(CreateView):
    template_name = 'book/add_person.html'
    form_class = forms.CreatePersonForm
    success_url = reverse_lazy('home')

    def get_success_url(self) -> str:
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            models.Phone.objects.create(phone=phone_number, contact=self.object)

        return super().get_success_url()


class DeletePhoneView(DeleteView):
    model = models.Person
    template_name = 'book/delete_person.html'
    success_url = reverse_lazy('home')
