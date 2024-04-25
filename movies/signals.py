from django.core.signals import request_finished
from django.dispatch import receiver
from movies.models import SearchTerm
from movies.tasks import notify_of_new_search_term

@receiver(post_save, sender=SearchTerm, dispatch_uid="search_term_saved")
def search_term_saved(sender, instance, created, **kwargs):
    if created:
        # new SearchTerm was created
        print(f"A new SearchTerm was created: '{instance.term}'")