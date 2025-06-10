from flask import Flask, request, Response
import requests
import urllib.parse

app = Flask(__name__)

VOIDAPI_KEY = "VDX-SHA2X-NZ0RS-O7HAM"

@app.route('/stripechk')
def stripechk():
    card = request.args.get("card", "")
    card = urllib.parse.unquote(card)
    url = f"https://api.voidapi.xyz/v2/stripe_auth?key={VOIDAPI_KEY}&card={card}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    # Always return status 200, even if VoidAPI returns 400
    return Response(r.text, status=200, content_type="application/json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
