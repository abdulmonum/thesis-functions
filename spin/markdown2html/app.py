from spin_sdk.http import IncomingHandler, Request, Response
from json import dumps, loads
import markdown
import base64



class IncomingHandler(IncomingHandler):
    def handle_request(self, request: Request) -> Response:
        params = loads(request.body)
        print(params)
        try:
            text = params["markdown"]
        except:
            return {'Error' : 'Possibly lacking markdown parameter in request.'}

        decoded_text = base64.b64decode(text.encode()).decode()

        html = markdown.markdown(decoded_text)

        response =  {"html_response": html}

        return Response(200,
                        {"content-type": "text/plain"},
                        bytes(dumps(response), "utf-8"))

