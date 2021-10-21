from django.urls import path
from offers.views import *
from django.contrib.auth.decorators import login_required






urlpatterns = [
    path('crud/',  login_required(CrudView.as_view()), name='crud_ajax'),
    path('create/', CreateCrudParcel.as_view(), name='crud_ajax_parcel'),
    path('delete/', DeleteParcel.as_view(), name='delete_ajax_parcel'),
    path('update/',  UpdateParcel.as_view(), name='update_ajax_parcel'),
]