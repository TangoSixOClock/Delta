from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.About,name='about'),
    path('course/<str:slug>/',views.Courses,name='course'),
    path('contact/',views.Contact,name='contact'),
    path('support/',views.Help,name='help'),
    path('blog/',views.Articles,name='newsletter'),
    path('news/',views.News,name='news'),
    path('profile/',views.Profile,name='profile'),
    path('update-profile/<int:pk>/',views.UpdateProfile,name='update-profile'),
    
    path('payment/<str:slug>/',views.PaymentPage,name='payment'),
    path('verify_payment/', views.verifyPayment , name = 'verify_payment'),
    path('adminPage/',views.adminPage,name='adminPage'),
  
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="reset_password.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_done.html"),name="password_reset_complete"),

    path('login/',views.LoginPage,name='loginpage'),
    path('register/',views.Register,name='register'),
    path('logout/',views.LogoutPage,name='logoutpage'),

    path('terms_and_conditions/',views.TermsCondition,name='term_condition'),
    path('return_policy/',views.ReturnPolicy,name='return_policy'),
    path('privacy_policy/',views.PrivacyPolicy,name='privacy_policy'),
    path('testimonial_policy/',views.TestimonialPolicy,name='testimonial_policy'),

    # path('playlist/<str:slug>/',views.playlist,name='playlist'),
    path('watch/<str:slug>/<int:pk>/',views.watch,name='watch'),
]
