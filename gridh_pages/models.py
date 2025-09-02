from django.db import models
from django_prose_editor.fields import ProseEditorField
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = ProseEditorField(blank=True,
        extensions={"Bold": True, "Italic": True, "Underline": True,
                    "Heading": {"levels": [2, 3, 4]}, # Only allow h2, h3, h4
                    "BulletList": True, "OrderedList": True, "ListItem": True, "Blockquote": True, "Link": {"enableTarget": True, "protocols": ["http", "https"], },
        },
        sanitize=True)
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pages', kwargs={'slug': self.slug})
