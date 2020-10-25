from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashpage/dashboard.html', {})
