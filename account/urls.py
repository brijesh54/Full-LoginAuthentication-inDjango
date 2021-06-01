from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .forms import MyPasswordChangeForm, MypasswordResetForm, MySetPasswordForm
from django.contrib.auth.decorators import login_required

urlpatterns = [ 
    # path('login/',views.user_login,name='login'),
    path('',views.dashboard,name='dashboard'),
    # path('login/',auth_views.LoginView.as_view(),name='login'),
    # path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    # path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html',
    #                                                               form_class=MyPasswordChangeForm, success_url='/account/passwordchangedone/'), name='changepassword'),
    # path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
    #     template_name='registration/password_change_done.html'), name='passwordchangedone'),


    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',
    #                                                              form_class=MypasswordResetForm), name='password_reset'),
    # path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
    #     template_name='registration/password_reset_done.html'), name='password_reset_done'),
    # path('password-reset/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
    #     template_name='registration/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    # path('password-reset/complete',auth_views.PasswordResetCompleteView.as_view(
    #     template_name='registration/password_reset_complete.html'), name='password_reset_complete'),    
    path('',include('django.contrib.auth.urls')),
    path('register/',views.register,name='register'),
    path('edit/',views.edit,name='edit'),
]