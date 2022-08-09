from django.urls import path
from.views import ZapatoListView, ZapatoDetailView, ZapatoCreateView, ZapatoUpdateView, ZapatoDeleteView

urlpatterns = [
    path('', ZapatoListView.as_view(), name='listarzapatos'),
    path('<int:pk>/', ZapatoDetailView.as_view(), name='detallarzapato'),
    path('crear/', ZapatoCreateView.as_view(), name='crearzapato'),
    path('actualizar/<int:pk>/', ZapatoUpdateView.as_view(), name='actualizarzapato'),
    path('eliminar/<int:pk>/', ZapatoDeleteView.as_view(), name='eliminarzapato'),

    
]