from django.contrib import admin

admin.site.site_header = "{{cookiecutter.project_name}} Admin"
admin.site.site_title = "{{cookiecutter.project_name}} Admin"
admin.site.index_title = "Home"
admin.site.enable_nav_sidebar = False
