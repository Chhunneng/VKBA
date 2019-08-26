from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r"^(?P<slug>[a-z0-9-_]+?)-(?P<product_id>[0-9]+)/$",
        views.product_details,
        name="details",
    ),
    url(
        r"^digital-download/(?P<token>[0-9A-Za-z_\-]+)/$",
        views.digital_product,
        name="digital-product",
    ),
    url(
        r"^category/(?P<slug>[a-z0-9-_]+?)-(?P<category_id>[0-9]+)/$",
        views.category_index,
        name="category",
    ),
    url(
        r"(?P<slug>[a-z0-9-_]+?)-(?P<product_id>[0-9]+)/add/$",
        views.product_add_to_checkout,
        name="add-to-checkout",
    ),
    url(
        r"^collection/(?P<slug>[a-z0-9-_/]+?)-(?P<pk>[0-9]+)/$",
        views.collection_index,
        name="collection",
    ),
    #<add by chhunneng url>
    url(r"^requests/$",views.requests,name="requests"),#add
    url(r"^requests/",views.added_requests,name="added_requests"),
    #</add by chhunneng url>
]
