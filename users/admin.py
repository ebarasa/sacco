from django.contrib import admin
from .models import Profile
from .models import Details
from .models import Activities
from .models import Report


admin.site.register(Profile)
admin.site.register(Details)
admin.site.register(Activities)
admin.site.register(Report)