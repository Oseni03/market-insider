from django.contrib import admin
from django.urls import path
from django.contrib import messages
from django.template.response import TemplateResponse

from .models import Post, Category, Account, ContactMessage
from .forms import AdminMailer

# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls() 
        my_urls = [
            path("mailer/", 
                self.admin_site.admin_view(
                    self.message_mailer, 
                    cacheable=True), name="mailer"),
        ]
        return my_urls + urls 
    
    def message_mailer(self, request):
        form = AdminMailer()
        if request.POST:
            form = AdminMailer(request.POST)
            if form.is_valid():
                contact = form.cleaned_data["user"]
                name = contact.name 
                email = contact.email 
                subject = f"Market Insider: Reply to [{contact.subject}]" 
                message = form.cleaned_data["message"]
                send_mail(
                    subject, message, "marketinsider@zohomail.com",
                    [email], fail_silently=False)
                messages.success(request, "Mail reply sent successfully!")
        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
            # Anything else you want in the context...
            form=form,
        )
        return TemplateResponse(request, "blog/admin/mailer.html", context)


admin.AdminSite.site_header = "Market Insider"
admin.AdminSite.site_title = "Market Insider Admin"

admin.site.register(Category)
admin.site.register(Account)

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_filter = ['published_at', 'category']
    list_display = ('__str__', 'title', 'published_at', 'category')
    list_select_related = ('category',)
    list_per_page = 20

@admin.register(ContactMessage)
class AdminContactMessage(MyModelAdmin):
    list_filter = ['created_at']
    list_display = ('__str__', "subject", 'created_at')
    list_per_page = 20