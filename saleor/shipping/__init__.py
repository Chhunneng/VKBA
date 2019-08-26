from django.utils.translation import pgettext_lazy


class ShippingMethodType:
    PRICE_BASED = "price"
    WEIGHT_BASED = "weight"
    # <ADD PERCENTAGE_BASED
    PERCENTAGE_BASED = "percentage"
    CHOICES = [
        (PRICE_BASED, pgettext_lazy("Type of shipping", "Price based shipping")),
        (WEIGHT_BASED, pgettext_lazy("Type of shipping", "Weight based shipping")),
        (PERCENTAGE_BASED, pgettext_lazy("Type of shipping", "Percentage based shipping")),
    ]
    # ADD PERCENTAGE_BASED >
