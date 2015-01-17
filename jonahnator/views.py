from django.http import JsonResponse

from django.views.generic import (
    View,
    TemplateView
)

from language.generator import random_markov_phrase as random_phrase


class JSONResponseMixin(object):
    """
    A mixin that can render a JSON response
    """

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload
        """

        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps()
        """
        return context


class HomeView(TemplateView):
    """
    An extremely simple view to load the homepage
    """
    template_name = "index.html"


class QuoteView(JSONResponseMixin, View):
    """
    Returns a random quote as a JSON object
    """
    def get(self, request, *args, **kwargs):
        rand_quote = random_phrase()
        while len(rand_quote) not in range(15, 120):
            rand_quote = random_phrase()
        context = {'quote': rand_quote}
        return self.render_to_json_response(context)
