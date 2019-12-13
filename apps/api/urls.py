from django.urls import path
from rest_framework import routers
from .views import BookAPIView, CategoryAPIView

router = routers.SimpleRouter()
router.register('book', BookAPIView)

urlpatterns = [
    # path('product/', ProductAPIView.as_view({'get': 'list', 'post': 'create'}), name='product'),
    # path('product/<pk>/', ProductAPIView.as_view({
    #     'get': 'retrieve',
    #     'put': 'partial_update',
    #     'delete': 'destroy'
    #     }), name='product-detail'),
    path('category/', CategoryAPIView.as_view(), name='category'),
]

urlpatterns += router.urls
