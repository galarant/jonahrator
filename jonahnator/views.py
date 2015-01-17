from django.http import JsonResponse

from django.views.generic import (
    View,
    TemplateView
)

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
        import random
        quotes = ["You can explain it in one sentence and get a little bit of a laugh in one sentence.",
                  "People see animals, and some of us are human and click the 'like' button.",
                  "Hate is a good way to build a community among a small group.",
                  "We don't have all this class resentment and swiping at all the frauds who are running everything in the US - that's more a British thing.",
                  "You don't want everyone to see a piece of content.",
                  "It is possible to build a tech company in New York that has really good snacks.",
                  "You can start to create content for humans, not for robots, and still have massive traffic.",
                  "Google can't find scoops because there's no cluster around it yet.",
                  "There are no tricks.",
                  "We're all teenage girls a little bit."]
        context = {'quote': random.choice(quotes)}
        return self.render_to_json_response(context)
