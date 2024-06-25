from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Entry
from .forms import EntryForm  

class EntryListView(ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = 'entries'  # Default is 'object_list'
    ordering = ['-date_created']  

class EntryDetailView(DetailView):
    model = Entry
    template_name = 'entries/entry_detail.html'

class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'entries/create_entry.html'
    success_url = '/'  # Redirect to home after successful creation

class EntryUpdateView(UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'entries/update_entry.html'
    success_url = '/' 

class EntryDeleteView(DeleteView):
    model = Entry
    template_name = 'entries/delete_entry.html' 
    success_url = '/' 
