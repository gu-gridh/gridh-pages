from django import template
from gridh_pages.models import NavigationItem
from django.conf import settings

register = template.Library()

@register.inclusion_tag('pages/navigation.html')
def render_navigation():
    return {
        "navigation_items": NavigationItem.objects.all().order_by('order')
    }


@register.inclusion_tag('pages/footer.html')
def render_footer():
    project_info = getattr(settings, 'PAGES_PROJECT_INFO', {})
    return {
        'links': project_info.get('LINKS', []),
        'partners': project_info.get('PARTNERS', []),
    }


@register.simple_tag
def project_name():
    project_info = getattr(settings, 'PAGES_PROJECT_INFO', {})
    return project_info.get('PROJECT_NAME', 'Default Project')


@register.inclusion_tag('pages/matomo.html')
def matomo():
    matomo = getattr(settings, 'MATOMO', {})
    return {
        'url': matomo.get('MATOMO_URL', ''),
        'site_id': matomo.get('MATOMO_SITE_ID', ''),
    }
