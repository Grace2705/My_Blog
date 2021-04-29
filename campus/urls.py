from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomePageView, AboutPageView, BlogView
from .views import Blogdeleteview, Blogcreateview, Blogupdateview, RegisterView, LoginView, Blogdetailview, LogoutView, AddCommentview



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginView, name = 'registration/login'),
    path('logout/', LogoutView, name = 'registration/logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='registration/password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('register/', RegisterView, name = 'register'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/',BlogView.as_view(), name = 'blog'),
    path('post_new/', Blogcreateview.as_view(), name='post_new'),
    path('<int:pk>/detail',Blogdetailview.as_view(), name = 'post_detail'),
    path('<int:pk>/edit/', Blogupdateview.as_view(), name='post_edit'),
    path('<int:pk>/delete/', Blogdeleteview.as_view(), name='post_delete'),
    path('<int:pk>/add_comment/', AddCommentview.as_view(), name='add_comment'),
]