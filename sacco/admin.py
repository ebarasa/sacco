from django.contrib import admin
from .models import Comment
from .models import Owner
from .models import Matatu
from .models import Crew
from .models import Finance
from .models import Activity_log


admin.site.register(Comment)
admin.site.register(Owner)
admin.site.register(Matatu)
admin.site.register(Crew)
admin.site.register(Finance)
admin.site.register(Activity_log)