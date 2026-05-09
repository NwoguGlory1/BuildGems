from rest_framework.response import Response

def api_response(success, message, data=None, errors=None):
    return Response(
        {
            "success": True,
            "message" : "Top Students retrieved successfully",
            "response":
                {
                    "count": len(data),
                    "data": data #data ia the output. After creating a serializer, you get serializer.data

                },
            "errors": errors
                    }
                    )
