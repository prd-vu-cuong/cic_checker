from django.http.response import Http404
from django.views import generic

# Create your views here.
from apps.cic_cms.views import BaseCmsView


class SingleView(BaseCmsView, generic.TemplateView):
    template_name = "cic_tool/single.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        return response

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            pass

        return Http404()
