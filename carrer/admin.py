from django.contrib import admin
from django.db import models
from carrer import models

# Register your models here.
admin.site.register(models.Jobs)
admin.site.register(models.Application)

admin.site.register(models.Testimonial)
admin.site.register(models.CaseStudy)

admin.site.register(models.Article)





