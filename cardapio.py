from conexao import get_conexao
from psycopg2.extras import RealDictCursor
from flask import jsonify


def get_cardapio():
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM cardapio;")
    cardapio = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(cardapio)