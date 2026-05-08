import secrets
import string
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt, Confirm
from rich.table import Table

console = Console()

def gerar_senha_customizada(tamanho: int, usar_maiusculas: bool, usar_numeros: bool, usar_simbolos: bool) -> str:
    # Base: sempre começa com letras minúsculas
    caracteres = string.ascii_lowercase
    
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))

def executar_gerador():
    while True:
        console.clear()
        console.print(Panel.fit(
            "[bold cyan]  GERADOR DE SENHAS  [/bold cyan]", 
            border_style="bright_blue",
            padding=(1, 2)
        ))

        # 1. Configurações
        tamanho = IntPrompt.ask("[bright_blue]Qual o tamanho da senha que você deseja?, Tamanho Recomendado[/bright_blue]",default=16)
        
        console.print("\n[bold white]Configurações de Caracteres:[/bold white]")
        maiusculas = Confirm.ask(" Incluir letras [bold]MAIÚSCULAS[/bold]?", default=True)
        numeros = Confirm.ask(" Incluir [bold]NÚMEROS[/bold]?", default=True)
        simbolos = Confirm.ask(" Incluir [bold]SÍMBOLOS[/bold]?", default=True)

        # 2. Geração com "charme" visual
        with console.status("[bold green]Calculando entropia...[/bold green]", spinner="dots"):
            time.sleep(0.6)  # Pequena pausa dramática
            senha = gerar_senha_customizada(tamanho, maiusculas, numeros, simbolos)

        # 3. Exibição do Resultado
        console.print("\n")
        console.print(Panel(
            f"[bold magenta]{senha}[/bold magenta]",
            title="[green]Senha Gerada com Sucesso[/green]",
            border_style="green",
            expand=False
        ))

        # 4. Opção de Repetir ou Sair
        print("\n")
        if not Confirm.ask("[bold cyan]Deseja gerar outra senha?[/bold cyan]", default=True):
            console.print("\n[bold red]Encerrando... Até a próxima! 👋[/bold red]\n")
            break

if __name__ == "__main__":
    try:
        executar_gerador()
    except KeyboardInterrupt:
        # Permite sair elegantemente com Ctrl+C
        console.print("\n\n[bold red]Programa interrompido pelo usuário.[/bold red]")