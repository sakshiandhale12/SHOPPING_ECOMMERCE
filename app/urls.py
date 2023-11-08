from django.urls import path
from app import views
from .views import ProductView, ProductDetailView  # Import ProductDetailView

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm,PasswordResetForm

urlpatterns = [
    path('', ProductView.as_view(), name='product-view'),
    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  # Use as_view() here
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='app/passwordreset.html',form_class=PasswordResetForm), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/passwordresetdone.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_done'),
    path('mobile/<slug:data>/', views.mobile, name='mobile'),
    path('laptop/<slug:data>/', views.laptop, name='laptop'),
    path('topwear/<slug:data>/', views.topwear, name='topwear'),
    path('bottomwear/<slug:data>/', views.bottomwear, name='bottomwear'),
    path('traditional/<slug:data>/', views.traditional, name='traditional'),
    path('western/<slug:data>/', views.western, name='western'),
    path('account/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),    
    path('checkout/', views.checkout, name='checkout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),  # Use CustomerRegistrationView
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
