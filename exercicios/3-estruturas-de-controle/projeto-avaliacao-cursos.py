# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning

# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

cursos_linkedin = ["introducao a agile", "Python para dummys", "Python para a Ciencia de dados", "algoritmos", "excell para dummys"]

curso_python = "Python para dummys"
curso_git = "Git e Github: formacao baasica"
curso_agile = "Introducao a agile"

avaliacoes = { }

if curso_python in cursos_linkedin:
  print(f" o curso { curso_python } esta no catalago. Por gentileza, avalie o curso.")
  avaliacoes [ curso_python  ] = int(input("qual eh a nota que vc da para o curso ( 0 a 5)?"))
  
  
