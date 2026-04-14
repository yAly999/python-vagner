import sqlite3

# conecta ao banco de dados
conn = sqlite3.connect("bd_senai.db")
cursor = conn.cursor()

# criar a tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nota INTEGER                  
    )
""")

print("\n --- Adicionar novo aluno ---")
nome_novo_aluno = input("Digite o nome do novo aluno: ")

while True:
    try:
        nota_novo_aluno = int(input("Digite a nota do novo aluno: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor digite um número inteiro!")

cursor.execute(
    "INSERT INTO alunos (nome, nota) VALUES (?, ?)",
    (nome_novo_aluno, nota_novo_aluno)
)

conn.commit()

print(f"Aluno {nome_novo_aluno} com a nota {nota_novo_aluno} adicionado com sucesso!\n")

print("=== dados da tabela (sem ordem) ===\n")

cursor.execute("SELECT * FROM alunos")
alunos = cursor.fetchall()

for aluno in alunos:
    print(aluno)

print("\n" + "="*20)