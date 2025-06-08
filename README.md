# Atividade_02
Atividade pratica para a Disciplina Programação para Ciência de Dados

Inicialmente foram submetidos dois arquivos Python e um arquivo compactado.
O Gerenciador tem por finalidade de gerenciar os documentos da Biblioteca.
O Principal fornece inteface en linha de comando para adicionar, remover ou renomear os arquivos da pasta documentos.

Dentro dele existem quatro arquivos: “Gerenciador.py”, “Principal.py”, “LEIA-ME.md” e a pasta “documentos.zip”
A seguir será detalhado cada um:

Este módulo tem a função de gerenciar os arquivos contidos na pasta “documentos”, arquivos digitais em um sistema de diretório. Permite listar, adicionar, remover e renomear documentos desta pasta. 
	A função listar documentos percorre o diretório da pasta documentos (lista base), e categoriza-os por ano (contido no nome) e tipo (extensão do arquivo). 
	Adicionar, copia um arquivo existente de um lugar de origem e o encaminha para o “destino”. Caso ele já exista, o arquivo é substituído. O documento encaminhado sempre manterá o nome original.
	Renomear, renomeia o arquivo localizado no caminho atual recebendo novo nome, mantido na pasta, porém com novo nome. 
	Remover, trata-se da exclusão do arquivo, esta ação é irreversível.
Esta estrutura adotada assume que os arquivos sejam organizados por ano.
•	A interface é realizada pelo programa “Principal”, cuja função é apresentar um menu interativo no terminal (que no nosso caso foi utilizado o Visual Studio Code), permitindo ao usuário selecionar opções entre: listar, adicionar, remover ou renomear arquivos de uma biblioteca, tudo isso de forma simples.

A estrutura do menu:

[1] Listar documentos
[2] Adicionar
[3] Renomear
[4] Remover
[5] Sair

Opção “1”, listar documentos executa ação de listar os documentos por tipo e ano. Agrupa os arquivos encontrados em pastas por ano e tipo. Caso o usuário informe algo que não “exista”, informa ao usuário que o documento não está cadastrado;

Opção “2”, adicionar documento de um arquivo original para um destino, incluído numa pasta. É necessário que o usuário informe o documento a origem e posteriormente o destino do arquivo que deseja adicionar. A confirmação se dá através da mensagem de “sucesso” ou “erro”, garantindo que o perceba o que aconteceu com o arquivo em questão;

Opção “3”, renomear é executado pela ação em que o usuário informa o nome (incluindo a extensão) e o endereço do arquivo. A confirmações se dá através de mensagem de “sucesso” ou “erro”.

Opção “4”, informando o endereço completo do arquivo, o usuário garante a remoção do documento da pasta. A confirmações se dá através de mensagem de “sucesso” ou “erro”.

Opção “5”, encerra o laço e finaliza a execução do programa, “encerrando o programa”.

	Posteriormente foi incluído ao programa o tratamento de erros, como, caminho inválido, arquivo inexistente, destino inválido.

•	O documento “LEIA-ME.md” é utilizado como uma página de anotações sobre o programa, onde os incrementos ou modificações são registrados.
•	A pasta compactada “documentos.zip” é um conjunto de arquivos aleatórios para execução de teste do programa, contempla diferentes extensões.


Guia de contribuição explicando como realizar commits, pushes e pull requests.
•	Primeiramente o GitHub foi instalado na máquina, logado e foi criado o repositório chamado “Atividade_02”. O repositório foi sincronizado com o Visual Studio Code.
•	Pelo website o repositório foi acessado e clonado.
•	Pelo aplicativo GitHub Desktop o aplicativo “Principal.py” foi acessado e alterado.
•	O programa foi modificado, acrescentado mensagem a explicação da alteração. Realizando assim um commit.
•	Enviando a alteração (Push origin).
•	As alterações realizadas no VSCode foram convertidas em modificações no programa  do projeto “Atividade_02” 
