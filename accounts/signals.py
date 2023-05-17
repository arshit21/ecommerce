from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from .models import Customer

@receiver(user_signed_up)
def do_stuff_after_sign_up(sender, **kwargs):
    request = kwargs['request']
    user = kwargs['user']
    user.is_customer = True
    # customer = Customer.objects.create(user_id=user.id, first_name=user.first_name, last_name=user.last_name, username = user.username,
    #                                     email=user.email, password=user.password)
    # customer.save()
    user.save()