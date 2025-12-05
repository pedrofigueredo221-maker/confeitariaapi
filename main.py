import os

from flask import Flask
from cardapio import get_cardapio

app = Flask(__name__)

@app.route("/")
def hello_world():
  """Example Hello World route."""
  name = os.environ.get("NAME", "World")
  return f"Hello {name}!"

@app.route("/cardapio")
def cardapio_route():
  cardapio = get_cardapio()
  return cardapio

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))