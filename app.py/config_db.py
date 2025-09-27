import sqlite3

# conecta no banco que você já criou
con = sqlite3.connect("meubanco.db")
cur = con.cursor()

# cria tabela de usuários
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# adiciona um usuário de teste
try:
    cur.execute("INSERT INTO users (nome, email, senha) VALUES (?, ?, ?)", 
                ("Rodrigo", "teste@email.com", "1234"))
    print("Usuário de teste criado com sucesso!")
except sqlite3.IntegrityError:
    print("Usuário já existe!")

con.commit()
con.close()
