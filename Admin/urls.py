from django.urls import path
from .views import *

urlpatterns = [
    path('create_officestaff/', OfficeStaffCreateView.as_view(), name='office-staff-rcreate'),
    path('create_librarian/',LibrarianCreateView.as_view(), name='create-librarian'),
    path('office-staff-update/', OfficeStaffUpdateView.as_view(), name='office-staff-update'),
    path('librarian-update/', LibrarianUpdateView.as_view(), name='librarian-update'),
    path('office-staff-delete/', OfficeStaffDeleteView.as_view(), name='office-staff-delete'),
    path('librarian-delete/', LibrarianDeleteView.as_view(), name='librarian-delete'),
    path('students-create/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/detail/', StudentDetailView.as_view(), name='student-detail'),
    path('office-staff/list/', OfficeStaffListView.as_view(), name='office-staff-list'),
    path('librarian/list/', LibrarianListView.as_view(), name='librarian-list'),
    

    
]