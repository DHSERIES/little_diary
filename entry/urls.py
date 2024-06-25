from django.urls import path
from .views import EntryListView, EntryDetailView, EntryCreateView, EntryUpdateView, EntryDeleteView

urlpatterns = [
    path('', EntryListView.as_view(), name='home'),
    path('entry/<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
    path('entry/new/', EntryCreateView.as_view(), name='entry_create'),
    path('entry/<int:pk>/update/', EntryUpdateView.as_view(), name='entry_update'),
    path('entry/<int:pk>/delete/', EntryDeleteView.as_view(), name='entry_delete'),
]