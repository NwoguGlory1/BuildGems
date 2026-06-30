from rest_framework.renderers import JSONRenderer
# handles renderer logic for re-usability


class CustomRenderer(JSONRenderer):
    # Using a custom renderer class, inheiritng JSONRenderer because output is still in JSON

    def render(self, data, accepted_media_type=None, renderer_context=None):
        # extracts the DRF Response object from Response class returned in response.py.
        response = renderer_context['response']
        # reads status code
        status_code = response.status_code
        success = True if status_code < 400 else False

        # makes sure data is correctly counted;
        if isinstance(data, list):
            count = len(data)
        elif data is None:
            count = 0
        else:
            count = 1

        # custom wrapper function wraps data
        wrapped_response = {
            "success": success,
            "message": "Request successful" if success else "Request failed",
            "response": {
                "count": count,
                "data": data
            },
            "errors": None if success else data
        }

    # super() calls the parent: JSONRenderer, going to the original render() method in JSONRenderer that converts it to JSON 
        return super().render(wrapped_response, accepted_media_type, renderer_context)