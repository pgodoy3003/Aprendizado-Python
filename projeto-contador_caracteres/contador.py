import sys  # Importa o módulo que permite interagir com o sistema (ler argumentos e sair do script)
import os   # Importa o módulo que permite verificar caminhos e arquivos no sistema operacional

def contar_caracteres(caminho_arquivo):
    # Verifica se o arquivo informado existe no diretório
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: arquivo '{caminho_arquivo}' não encontrado.")
        sys.exit(1)  # Finaliza o script com erro (código 1) caso o arquivo não exista

    # Verifica se o arquivo termina com a extensão .txt, apenas por convenção
    if not caminho_arquivo.lower().endswith(".txt"):
        print("Aviso: o arquivo fornecido não possui extensão .txt")

    # Abre o arquivo em modo leitura ("r") e define a codificação como UTF-8
    # O 'with' garante que o arquivo seja fechado automaticamente após o uso
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()  # Lê todo o conteúdo do arquivo e armazena na variável 'conteudo'

    # Calcula o tamanho total da string (contando tudo)
    total = len(conteudo)
    
    # Substitui todos os espaços (" ") por vazio ("") e calcula o tamanho
    sem_espacos = len(conteudo.replace(" ", ""))
    
    # Remove espaços, quebras de linha (\n) e retornos de carro (\r), e calcula o tamanho
    sem_espacos_e_quebras = len(conteudo.replace(" ", "").replace("\n", "").replace("\r", ""))
    
    # Conta o número de quebras de linha (\n). 
    # Adiciona 1 caso o arquivo não termine com uma quebra de linha (para contar a última linha)
    linhas = conteudo.count("\n") + (1 if conteudo and not conteudo.endswith("\n") else 0)

    # Exibe os resultados formatados na tela
    print(f"\n📄 Arquivo: {caminho_arquivo}")
    print(f"{'─' * 40}")  # Desenha uma linha decorativa
    print(f"  Total de caracteres (com espaços):     {total}")
    print(f"  Total de caracteres (sem espaços):     {sem_espacos}")
    print(f"  Total (sem espaços e quebras de linha): {sem_espacos_e_quebras}")
    print(f"  Número de linhas:                      {linhas}")
    print(f"{'─' * 40}\n")


# Este bloco verifica se o script está sendo executado diretamente (não importado por outro)
if __name__ == "__main__":
    # Verifica se o usuário passou o caminho do arquivo como argumento no terminal
    if len(sys.argv) < 2:
        print("Uso: python contar_caracteres.py <caminho_do_arquivo.txt>")
        sys.exit(1)  # Finaliza se não houver argumento suficiente

    # Chama a função principal passando o primeiro argumento (o caminho do arquivo)
    contar_caracteres(sys.argv[1])