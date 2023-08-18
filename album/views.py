from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from album.models import Selection, Player
from django.db.models import Value
from django.db.models.functions import Concat

# Create your views here.

## Selection

class SelectionListView(ListView):
    model = Selection

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get the value of the 'query' query parameter
        query = self.request.GET.get('query')

        # Filter the queryset based on the 'query' parameter if provided
        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset

class SelectionDetailView(DetailView):
    model = Selection


class SelectionCreate(CreateView):
    model = Selection
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add additional data to the context dictionary
        additional_data = {
            'type': 'create',
        }
        
        context.update(additional_data)
        return context


class SelectionUpdate(UpdateView):
    model = Selection
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add additional data to the context dictionary
        additional_data = {
            'type': 'update',
        }
        
        context.update(additional_data)
        return context


class SelectionDelete(DeleteView):
    model = Selection
    success_url = reverse_lazy('selection-list')


## Player

class PlayerListView(ListView):
    model = Player
    
    def get_queryset(self):
        queryset = super().get_queryset()

        # Get the value of the 'query' query parameter
        query = self.request.GET.get('query')

        # Filter the queryset based on the 'query' parameter if provided
        if query:
            queryset = queryset.annotate(
                full_name=Concat('first_name', Value(' '), 'last_name')
                ).filter(full_name__icontains=query)
        
        return queryset


class PlayerDetailView(DetailView):
    model = Player


class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add additional data to the context dictionary
        additional_data = {
            'type': 'update',
        }
        
        context.update(additional_data)
        return context


class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add additional data to the context dictionary
        additional_data = {
            'type': 'create',
        }
        
        context.update(additional_data)
        return context


class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('player-list')

