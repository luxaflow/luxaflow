from django.contrib import admin

from .models import Profile, Experience, Education, Skill

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'mobile')


@admin.register(Experience)
class ExperienceModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'from_date', 'till_date_value')

    def till_date_value(self, obj):
        if not obj.till_date:
            return 'Current'
        else:
            return obj.till_date


@admin.register(Education)
class EducationModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'from_date', 'till_date_value', 'completed')
    list_editable = ['completed',]

    def till_date_value(self, obj):
        if not obj.till_date:
            return 'Current'
        else:
            return obj.till_date


@admin.register(Skill)
class SkillModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'scale', 'soft_skill', 'language', 'framework', 'other', 'learning')
    list_editable = ['scale', 'soft_skill', 'language', 'framework', 'other', 'learning']

    list_per_page = 15
