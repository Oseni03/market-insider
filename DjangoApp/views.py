from django.shortcuts import render

def page_not_found_view(request, exception):
    context = {
        "handler": True, 
        "title": "Page Not Found"
    }
    return render(request, '404.html', context, status=404)


def server_error_view(request):
    context = {
        "handler": True, 
        "title": "Server Error"
    }
    return render(request, '500.html', context, status=500)