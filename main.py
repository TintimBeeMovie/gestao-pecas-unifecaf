# ============================================
# SISTEMA DE GESTÃO DE PEÇAS - UNIFECAF
# ============================================

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box

console = Console()

# Listas que guardam os dados do sistema
pecas_aprovadas = []
pecas_reprovadas = []
caixa_atual = []
caixas_fechadas = []

# ============================================
# FUNÇÃO: Avaliar se a peça está aprovada
# ============================================

def avaliar_peca(id, peso, cor, comprimento):
    motivos = []

    if peso < 95 or peso > 105:
        motivos.append("Peso fora do padrão")

    if cor not in ["azul", "verde"]:
        motivos.append("Cor inválida")

    if comprimento < 10 or comprimento > 20:
        motivos.append("Comprimento fora do padrão")

    if len(motivos) == 0:
        return True, []
    else:
        return False, motivos

# ============================================
# FUNÇÃO: Cadastrar nova peça
# ============================================

def cadastrar_peca():
    console.print(Panel("📦 CADASTRAR NOVA PEÇA", style="bold cyan"))

    id = Prompt.ask("[cyan]ID da peça[/cyan]")
    peso = float(Prompt.ask("[cyan]Peso (g)[/cyan]"))
    cor = Prompt.ask("[cyan]Cor[/cyan]").strip().lower()
    comprimento = float(Prompt.ask("[cyan]Comprimento (cm)[/cyan]"))

    peca = {
        "id": id,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento
    }

    aprovada, motivos = avaliar_peca(id, peso, cor, comprimento)

    if aprovada:
        pecas_aprovadas.append(peca)
        caixa_atual.append(peca)
        console.print(f"\n✅ [bold green]Peça {id} APROVADA![/bold green]")

        if len(caixa_atual) == 10:
            caixas_fechadas.append(list(caixa_atual))
            caixa_atual.clear()
            console.print(f"📦 [bold yellow]Caixa cheia! Caixa {len(caixas_fechadas)} fechada.[/bold yellow]")
    else:
        peca["motivos"] = motivos
        pecas_reprovadas.append(peca)
        console.print(f"\n❌ [bold red]Peça {id} REPROVADA![/bold red]")
        console.print(f"[red]Motivos: {', '.join(motivos)}[/red]")

# ============================================
# FUNÇÃO: Listar peças aprovadas e reprovadas
# ============================================

def listar_pecas():
    console.print(Panel("📋 LISTA DE PEÇAS", style="bold cyan"))

    if len(pecas_aprovadas) == 0:
        console.print("[yellow]Nenhuma peça aprovada ainda.[/yellow]")
    else:
        tabela = Table(title="✅ Peças Aprovadas", box=box.ROUNDED, style="green")
        tabela.add_column("ID", style="bold")
        tabela.add_column("Peso (g)")
        tabela.add_column("Cor")
        tabela.add_column("Comprimento (cm)")

        for peca in pecas_aprovadas:
            tabela.add_row(peca["id"], str(peca["peso"]), peca["cor"], str(peca["comprimento"]))

        console.print(tabela)

    if len(pecas_reprovadas) == 0:
        console.print("[yellow]Nenhuma peça reprovada ainda.[/yellow]")
    else:
        tabela2 = Table(title="❌ Peças Reprovadas", box=box.ROUNDED, style="red")
        tabela2.add_column("ID", style="bold")
        tabela2.add_column("Motivos")

        for peca in pecas_reprovadas:
            tabela2.add_row(peca["id"], ', '.join(peca["motivos"]))

        console.print(tabela2)

# ============================================
# FUNÇÃO: Remover peça cadastrada
# ============================================

def remover_peca():
    console.print(Panel("🗑️  REMOVER PEÇA", style="bold red"))
    id_busca = Prompt.ask("[red]Digite o ID da peça para remover[/red]")

    for peca in pecas_aprovadas:
        if peca["id"] == id_busca:
            pecas_aprovadas.remove(peca)
            console.print(f"✅ [green]Peça {id_busca} removida das aprovadas.[/green]")
            return

    for peca in pecas_reprovadas:
        if peca["id"] == id_busca:
            pecas_reprovadas.remove(peca)
            console.print(f"✅ [green]Peça {id_busca} removida das reprovadas.[/green]")
            return

    console.print(f"[yellow]⚠️  Peça com ID {id_busca} não encontrada.[/yellow]")

# ============================================
# FUNÇÃO: Listar caixas fechadas
# ============================================

def listar_caixas():
    console.print(Panel("📦 CAIXAS FECHADAS", style="bold cyan"))

    if len(caixas_fechadas) == 0:
        console.print("[yellow]Nenhuma caixa fechada ainda.[/yellow]")
    else:
        for i, caixa in enumerate(caixas_fechadas):
            tabela = Table(title=f"📦 Caixa {i + 1} ({len(caixa)} peças)", box=box.ROUNDED, style="cyan")
            tabela.add_column("ID", style="bold")
            tabela.add_column("Peso (g)")
            tabela.add_column("Cor")
            tabela.add_column("Comprimento (cm)")

            for peca in caixa:
                tabela.add_row(peca["id"], str(peca["peso"]), peca["cor"], str(peca["comprimento"]))

            console.print(tabela)

# ============================================
# FUNÇÃO: Gerar relatório final
# ============================================

def gerar_relatorio():
    console.print(Panel("📊 RELATÓRIO FINAL DO SISTEMA", style="bold magenta"))

    tabela = Table(box=box.ROUNDED, style="magenta")
    tabela.add_column("Indicador", style="bold")
    tabela.add_column("Quantidade", justify="center")

    tabela.add_row("✅ Peças Aprovadas", str(len(pecas_aprovadas)))
    tabela.add_row("❌ Peças Reprovadas", str(len(pecas_reprovadas)))
    tabela.add_row("📦 Caixas Fechadas", str(len(caixas_fechadas)))
    tabela.add_row("📂 Caixa Atual (aberta)", str(len(caixa_atual)))

    console.print(tabela)

    if len(pecas_reprovadas) > 0:
        tabela2 = Table(title="Motivos de Reprovação", box=box.ROUNDED, style="red")
        tabela2.add_column("ID", style="bold")
        tabela2.add_column("Motivos")

        for peca in pecas_reprovadas:
            tabela2.add_row(peca["id"], ', '.join(peca["motivos"]))

        console.print(tabela2)

# ============================================
# MENU PRINCIPAL
# ============================================

def menu():
    while True:
        console.print(Panel(
            "[bold cyan]1.[/bold cyan] Cadastrar nova peça\n"
            "[bold cyan]2.[/bold cyan] Listar peças aprovadas/reprovadas\n"
            "[bold cyan]3.[/bold cyan] Remover peça cadastrada\n"
            "[bold cyan]4.[/bold cyan] Listar caixas fechadas\n"
            "[bold cyan]5.[/bold cyan] Gerar relatório final\n"
            "[bold red]0.[/bold red] Sair",
            title="⚙️  SISTEMA DE GESTÃO DE PEÇAS",
            style="bold white"
        ))

        opcao = Prompt.ask("[bold]Escolha uma opção[/bold]")

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            console.print(Panel("👋 Sistema encerrado. Até logo!", style="bold green"))
            break
        else:
            console.print("[red]⚠️  Opção inválida! Tente novamente.[/red]")

# ============================================
# INICIAR O SISTEMA
# ============================================

menu()