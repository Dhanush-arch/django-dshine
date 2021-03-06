from django.urls import path
from . import views
from .views import (
    ItemDetailView,
    HomeView,
    add_to_cart,
    add_to_wish,
    remove_from_cart,
    remove_from_wish,
    ShopView,
    OrderSummaryView,
    WishView,
    remove_single_item_from_cart,
    CheckoutView,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    CategoryView,
    remove_single_item_from_wish,
    ContactView,
    login_view,
    logout_view,
    Register_user,
    Register,
    order_view,
    menu_view,
    ItemDetailsView,
	add_single_item,
    menu_view_collections,
    adminOrders_View,
    accept_order,
    decline_order,
    delivered_order,
    getOrders_Status,
    payment_status,
    clear_cart,
    clear_wish,
    add_wish_to_cart,
    pdfView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('addcomment/<int:id>/', views.addcomment, name='addcomment'),
    path('contactus/',ContactView.as_view(), name='contact-us'),
    path('addcontactus/', views.contactus, name='add-contact-us'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('get-details/<slug>/<value>', ItemDetailsView, name='product-details'),
    path('add-to-cart/<id>/<qt>/<value>/', add_to_cart, name='add-to-cart'),
    path('add-to-wish/<slug>/<qt>/<value>/', add_to_wish, name='add-to-wish'),
    path('add-pri-to-cart/<slug>/<qt>/', views.add_pri_to_cart, name='add-pri-to-cart'),
    path('post-form/<slug>/<cat>/<val>/', views.post_form, name='post_form'),
    path('add-pri-to-wish/<slug>/<qt>/', views.add_pri_to_wish, name='add-pri-to-wish'),
    path('add_coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<id>/', remove_from_cart, name='remove-from-cart'),
    path('remove-from-wish/<slug>/<id>/', remove_from_wish, name='remove-from-wish'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('wish-summary/', WishView.as_view(), name='wish-summary'),
    path('remove-item-from-cart/<id>/<value>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('add-item-to-cart/', add_single_item, name="add-item-to-cart"),
    path('remove-item-from-wish/<slug>/<value>/', remove_single_item_from_wish, name="remove-single-item-from-wish"),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),

    path('login', login_view, name="login_view"),
    path('logout', logout_view, name='logout_view'),
    path('register/register_user/', Register_user, name='register'),
    path('register/', Register, name='register_page'),
    path('orders', order_view, name='orders'),
    path("products_menu/<num>/", menu_view, name="menu_view"),
    path('collections_menu/<num>/', menu_view_collections, name="menu_view_collections"),
    path('admin-orders/', adminOrders_View, name='adminOrders_View'),
    path('accept-order/<int:id>/', accept_order, name='accept_order'),
    path('decline-order/<int:id>/', decline_order, name='decline_order'),
    path('delivered-order/<int:id>/', delivered_order, name='delivered_order'),
    path('order_status/', getOrders_Status, name='getOrders_Status'),
    path('payment_status/', payment_status, name = 'payment_status'),
    path('clear-cart', clear_cart, name="clear_cart"),
    path('clear-wish', clear_wish, name="clear_wish"),
    path('add_wish_to_cart/<id>', add_wish_to_cart, name="add_wish_to_cart"),
    path('generate-invoice/<id>', pdfView, name="pdfView")
]
