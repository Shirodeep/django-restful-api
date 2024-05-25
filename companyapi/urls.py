from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups',views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('company/users/', views.company_user_list, name='allorcreate'),
    path('company/users/<int:pk>', views.company_user_detail, name='detailapi'),
    
]

