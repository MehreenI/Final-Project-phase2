from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index,name="index"),
    path('about-us/',views.about),
    path('products/',views.products),
    path('products/<int:id>',views.category_product_list_view),
    path('productDetail/<int:id>',views.productDetail),
    path('faq/',views.faq),
    path('contact/', views.contact,  name='contact'),
    path('submit_review/<int:id>',views.submit_review),
    path('registration/',views.registration),
    path('register-account/', views.register_user),
    path('login-account/', views.login_user,name='login'),
    path("logOut/",views.logout_user),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
