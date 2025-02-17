from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Configuração do banco de dados
DB_HOST = "dpg-cup8loa3esus738bml70-a:5432"
DB_NAME = "testerender_ljin"
DB_USER = "testerender_ljin_user"
DB_PASSWORD = "sP0yKHPUT17J4h8qJvckvVihwn6gCuQz"

def conectar_bd():
    """ Conecta ao PostgreSQL e retorna a conexão """
    return psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)

@app.route("/", methods=["GET", "POST"])
def index():
    mensagem = ""
    
    if request.method == "POST":
        nome = request.form["nome"]
        idade = request.form["idade"]
        cidade = request.form["cidade"]

        if nome and idade and cidade:
            try:
                conn = conectar_bd()
                cur = conn.cursor()
                cur.execute("INSERT INTO usuarios (nome, idade, cidade) VALUES (%s, %s, %s)", (nome, idade, cidade))
                conn.commit()
                cur.close()
                conn.close()
                mensagem = "Usuário cadastrado com sucesso!"
            except Exception as e:
                mensagem = f"Erro ao cadastrar usuário: {e}"
        else:
            mensagem = "Todos os campos são obrigatórios!"

    return render_template("index.html", mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)
