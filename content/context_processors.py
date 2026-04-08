from .models import SiteMessage

def site_messages(request):
    return {
        "site_messages": SiteMessage.objects.filter(active=True).order_by("-created_at")
    }