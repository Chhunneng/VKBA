import json
from django.utils.translation import pgettext, pgettext_lazy
from django import forms
from django.utils.encoding import smart_text
from django.core.validators import RegexValidator
from django_prices.templatetags.prices_i18n import amount
from captcha.fields import ReCaptchaField
from ..checkout.forms import AddToCheckoutForm
from ..core.utils.taxes import display_gross_prices
from .models import request
from django.forms import CheckboxInput

class VariantChoiceField(forms.ModelChoiceField):
    discounts = None
    taxes = None
    display_gross = True

    def label_from_instance(self, obj):
        variant_label = smart_text(obj)
        price = obj.get_price(self.discounts, self.taxes)
        price = price.gross if self.display_gross else price.net
        label = pgettext_lazy(
            "Variant choice field label", "%(variant_label)s - %(price)s"
        ) % {"variant_label": variant_label, "price": amount(price)}
        return label

    def update_field_data(self, variants, discounts, taxes):
        """Initialize variant picker metadata."""
        self.queryset = variants
        self.discounts = discounts
        self.taxes = taxes
        self.empty_label = None
        self.display_gross = display_gross_prices()
        images_map = {
            variant.pk: [vi.image.image.url for vi in variant.variant_images.all()]
            for variant in variants.all()
        }
        self.widget.attrs["data-images"] = json.dumps(images_map)
        # Don't display select input if there is only one variant.
        if self.queryset.count() == 1:
            self.widget = forms.HiddenInput({"value": variants.all()[0].pk})


class ProductForm(AddToCheckoutForm):
    variant = VariantChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        variant_field = self.fields["variant"]
        variant_field.update_field_data(
            self.product.variants.all(), self.discounts, self.taxes
        )

    def get_variant(self, cleaned_data):
        return cleaned_data.get("variant")
class FormWithReCaptcha(forms.BaseForm):
    def __new__(cls, *args, **kwargs):
        if settings.RECAPTCHA_PUBLIC_KEY and settings.RECAPTCHA_PRIVATE_KEY:
            # insert a Google reCaptcha field inside the form
            # note: label is empty, the reCaptcha is self-explanatory making
            #       the form simpler for the user.
            cls.base_fields["_captcha"] = ReCaptchaField(label="")
        return super(FormWithReCaptcha, cls).__new__(cls)
#<Add by chhunneng class RequestForm> 
class RequestForm(forms.ModelForm):
    image = forms.ImageField(label='Select Image File:',error_messages={'required':'Please put the Image'},required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Name'}),label='Product Name:',help_text='Example: Carrot Juice',error_messages={'required':'Please put the Product Name'},required=True)
    quantity= forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Product Quantity'}),label="Product Quantity:",help_text='Example : 10',error_messages={'required':'Please put the Product Quantity'},required=True)
    price=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Unit Price for product'}),label="Unit Price:",help_text='Example : 3.00$',error_messages={'required':'Please put the Product Price'},required=True)   
    attribute=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Attribute'}),label="Product Attribute:",help_text='Example : 500ML',error_messages={'required':'Please put the Product Attribute'},required=True)
    url=forms.URLField(widget=forms.URLInput(attrs={'placeholder':'URL of Reference for Product'}),label="Product URL:",help_text='Note: If you have URL for informations of product, you can drop URLs here.',required=False)
    description=forms.CharField(label="Product Description:",widget=forms.Textarea(attrs={'rows':3,'placeholder':'Describe about brand or more feature product'}),help_text='Describe about brand or more feature product',error_messages={'required':'Please put the shape,brand or more feature of product'},required=True)
    class Meta:
        model = request
        fields=('image','name','quantity','price','attribute','url','description')
#</Add by chhunneng class RequestForm> 