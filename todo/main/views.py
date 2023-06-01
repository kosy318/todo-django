from django.shortcuts import render
from django.views import generic


class Todo_main(generic.TemplateView):
    # get 방식으로 받았을 때, index.html로 이동
    def get(self, request, *args, **kwargs):
        template_name = 'main/index.html'
        return render(request, template_name)