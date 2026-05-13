from rest_framework.renderers import JSONRenderer
# handles renderer logic for re-usability


class CustomRenderer(JSONRenderer):
    # Using a custom renderer class, inheiritng JSONRenderer because output is still in JSON

    def render(self, data, accepted_media_type=None, renderer_context=None):
        # extracts the DRF Response object from Response class returned in response.py.
        response = renderer_context['response']

        status_code = response.status_code

        
        success = True if status_code < 400 else False

        # makes sure data is correctly counted;
        if isinstance(data, list):
            count = len(data)
        elif isinstance(data, dict):
            count = 1
        else:
            count = 0

        # custom wrapper function
        wrapped_response = {
            "success": success,
            "message": "Request successful" if success else "Request failed",
            "response": {
                "count": count,
                "data": data
            },
            "errors": None if success else data
        }

    # super() calls the parent: JSONRenderer
        return super().render(wrapped_response, accepted_media_type, renderer_context)