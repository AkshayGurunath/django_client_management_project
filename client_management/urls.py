from django.urls import path
from .views import ClientListCreateView, ClientDetailView, ProjectCreateView, UserProjectsListView

urlpatterns = [
    path('clients/<int:pk>/', ClientListCreateView.as_view(), name='client-list'),
    path('clients/<int:id>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/', ClientListCreateView.as_view(), name='client-list'),
    path('clients/<int:client_id>/projects/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/', UserProjectsListView.as_view(), name='user-projects'),
]
