from django.contrib import admin
from django.urls import path, include
from .views import index, MenuItemView, SingleMenuItemView, BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('menu', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('bookings/', include(router.urls))
]


