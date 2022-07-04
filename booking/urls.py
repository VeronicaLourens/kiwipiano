from django.urls import path
from . import views
from booking.views import(
    BookingDetailView,
    BookingUpdateView,
    AdminPanelView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login, name='login'),
    path('admin/', views.admin_login, name='admin'),
    path('feedback/', views.feedback, name='feedback'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('booking_login/', views.booking_login, name='booking_login'),
    path('booking_form/', views.booking_form, name='booking_form'),
    path('booking_not_available/', views.booking_not_available, name='booking_not_available'),
    path('booking_detail/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('booking_update/<int:pk>/', views.BookingUpdateView.as_view(), name='booking_update'),
    path('booking_cancel/<int:pk>/', views.booking_cancel, name='booking_cancel'),
    path('admin_panel/', AdminPanelView.as_view(), name='admin_panel'),
    path('admin_panel/approve/<int:id>/', views.approve_booking, name='approve_booking'),
    

]
