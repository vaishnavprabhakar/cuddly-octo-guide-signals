import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import Poll
from django.db import transaction


def check(func):
    def inner(**kwargs):
        poll_instance = kwargs['instance']
        last_obj = Poll.objects.last()
        if poll_instance.name == last_obj.name:
            print(f"Poll :{last_obj} object got before the signal handler.")
        func()
    return inner


@receiver(post_save, sender=Poll)
@check
def poll_handler(**kwargs):
    print(f"Signal Running Thread Id : {threading.current_thread().ident}")
    print(f"Same Trx In signal ===: {transaction.get_connection().in_atomic_block}") # This retturn True ,if the same transaction as the caller  working in the signal
    print('1. Same') # got the object before the signal handler working
    print('2. Same') # Has the same Id
    print('3. Same') # transaction.get_connection().in_atomic_block this returns True


