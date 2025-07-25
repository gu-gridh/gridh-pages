============
gridh-pages
============

WORK_IN_PROGRESS

gridh-pages is a Django app to create simple static pages for django projects. It offers to add pages with a title, slug and content which is a Richtextfield by using the django_prose_editor. It was created with gridh projects in mind but can be used in other contexts, too.

Quick start
-----------

1. Add "pages" and the required "django_prose_editor" for richtext fields to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "django_prose_editor",
        "gridh_pages",
    ]

2. In settings also add the following to add project information for a project::

    PAGES_PROJECT_INFO = {
        "PROJECT_NAME": "Great project name",
        "LINKS": [
            {"label": "My cool link", "url": "https://example.com/example1", "type": "site-link"},
            {"label": "Another cool link", "url": "https://example.com/example2", "type": "download-link"},
            ...
        ],
        "PARTNERS": [
            {"label": "partner", "url": "https://example.com/partner1"},
            {"label": "another partner", "url": "https://example.com/partner2"},
            ...
        ],
        "EXTRA_NAV_URLS": {"label": "Contact", "url": "https://example.com/contact"},
    }

3. Include the pages URLconf in your project urls.py like this::

    path("pages/", include("gridh_pages.urls")),

4. Run ``python manage.py migrate`` to create the models.

5. Start the development server and visit the admin to create a static pages.

6. You can create static pages with a title, a slug and a content block with dfferent options. Currently, the django app ``django_prose_editor`` is used for this richtext field which you have to include in your INSTALLED_APPS setting.

7. For each static page it looks for a .html file with the same name as the slug (e.g. ``about.html``). So you can overwrite it for each project in ``templates/pages/...`` if needed. Otherwise it falls back to a ``default.html`` which you can also overwrite. It also contains a ``base.html`` template with a basic navigation, main content block and footer that can be overwritten. It looks in that case for a ``minified.css`` in your project's static folder to load your css.

8. Visit the ``/pages/...`` URL to see your created pages.
