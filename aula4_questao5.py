# aula4_questao5.py

livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["Dom Casmurro", "Machado de Assis", 1899, 256],
    ["1984", "George Orwell", 1949, 328],
    ["A Revolução dos Bichos", "George Orwell", 1945, 152],
    ["Grande Sertão: Veredas", "Guimarães Rosa", 1956, 608],
    ["Ensaio sobre a Cegueira", "José Saramago", 1995, 312],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 309],
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1216],
    ["O Hobbit", "J.R.R. Tolkien", 1937, 310],
]

with open("meus_livros.csv", "w", encoding="utf-8") as f:
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        f.write(",".join(map(str, livro)) + "\n")

print("Arquivo 'meus_livros.csv' criado com sucesso!")
