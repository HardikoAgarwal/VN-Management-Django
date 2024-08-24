from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login, name='login'),
    path('logout/', views.logout),
    path('sales-representative/', views.sales_rep),
    path('head-manager/', views.head_mng),
    path('packaging-manager/', views.packng_mng),
    path('production-manager/', views.prdctn_mng),
    path('dispatcher/', views.dispatcher, name='dispatcher'),
    path('create-order/', views.create_order, name="create_order"),
    path('delete-order/', views.delete_order, name='delete_order'),
    path('complete-order/<int:id>/', views.complete_order, name='complete-order'),
    path('confirm-order/', views.confirm_order, name='confirm-order'),
    path('change-schedule/', views.change_schedule),
    path('submit-data/', views.submit_data, name='submit_data'),
    path('customers/',views.show_customers, name='show_customers'),
    path('add-customer',views.add_customer, name= 'add_customer'),
    path('create-customer/',views.create_customer, name='create_customer'),
    path('customers/details/<int:id>/',views.customer_detail, name='customer_detail'),
]