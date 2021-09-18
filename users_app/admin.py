from django.contrib import admin

# Own
from users_app.models import UsersTasksSolutions


class UsersTasksSolutionsAdmin(admin.ModelAdmin):
    list_display = (
        "user_nickname",
        "task_title",
        "user_amounts_of_try",
        "amount_tests_cases_passed",
        "is_task_passed",
    )
    list_filter = (
        "task_title",
        "is_task_passed",
    )


admin.site.register(UsersTasksSolutions, UsersTasksSolutionsAdmin)
