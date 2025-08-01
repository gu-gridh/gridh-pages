from django import template
from gridh_pages.models import Page
from django.conf import settings

register = template.Library()


@register.inclusion_tag('pages/navigation.html')
def render_navigation():
    pages = Page.objects.all().order_by('order')
    project_info = getattr(settings, 'PAGES_PROJECT_INFO', {})
    return {'pages': pages,
            'extra_nav_urls': project_info.get('EXTRA_NAV_URLS', [])}


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


@register.simple_tag
def matomo():
    matomo = getattr(settings, 'MATOMO', {})
    return {
        'url': matomo.get('MATOMO_URL', ''),
        'site_id': matomo.get('MATOMO_SITE_ID', ''),
    }
