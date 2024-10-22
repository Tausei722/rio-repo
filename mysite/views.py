from django.shortcuts import render

def my_custom_page_not_found_view(request, exception):
    return render(request, '404.html')

def my_custom_error_view(request):
    return render(request, '500.html')

def my_custom_permission_denied_view(request):
    return render(request, '403.html')

def my_custom_bad_request_view(request):
    return render(request, '400.html')