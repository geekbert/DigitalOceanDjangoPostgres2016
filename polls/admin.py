from django.contrib import admin

# Register your models here.

from .models import Question, Choice

from django.http import HttpResponse

# ... export functions will go here ...
def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    # mimetype replaced wth content_type
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # optional...Excel needs it to ope$
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"question_text"),
        smart_str(u"qty"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(u"ID"),
            smart_str(u"question_text"),
            smart_str(u"qty"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.question_text),
            smart_str(obj.qty),
        ])
    return response
export_csv.short_description = u"Export CSV"





class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'total')
    actions = [export_csv]

#class Choice(admin.ModelAdmin):
#    model = Choice



admin.site.register(Question, QuestionAdmin)
