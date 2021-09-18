from django.contrib import admin

# Own
from main_app.models import Tasks


class TasksAdmin(admin.ModelAdmin):
    list_display = (
        "task_id",
        "task_title",
        "amount_tests_cases",
    )


admin.site.register(Tasks, TasksAdmin)
