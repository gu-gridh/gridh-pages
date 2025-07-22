from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.template.loader import select_template
from .models import Page


class PageView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        self.page = get_object_or_404(Page, slug=self.kwargs["slug"])
        return super().dispatch(request, *args, **kwargs)

    def get_template_names(self):
        template_candidates = [
            f"pages/{self.page.slug}.html",  # e.g. pages/about.html
            "pages/default.html",            # fallback
        ]
        return [select_template(template_candidates).template.name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = self.page
        return context
