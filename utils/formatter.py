"""
Output Formatter — Renders the final morning brief in a clean format.
Uses Rich for colorful, structured terminal output.
"""

from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()


def format_output(
    topic: str,
    summaries: list[dict],
    brief: str,
    why_it_matters: str,
) -> None:
    """
    Render the full morning brief to terminal.

    Args:
        topic: The news topic.
        summaries: List of article summary dicts.
        brief: The combined morning brief.
        why_it_matters: The "Why It Matters" text.
    """
    console.print()

    # ── Header ──
    console.print(
        Panel(
            f"[bold white]🗞️  AI Morning News Brief[/bold white]\n"
            f"[dim]Topic: {topic}[/dim]",
            border_style="cyan",
            box=box.DOUBLE,
            padding=(1, 2),
        )
    )
    console.print()

    # ── 🔥 Top Stories ──
    console.print("[bold yellow]🔥 Top Stories[/bold yellow]")
    console.print("─" * 50, style="dim")
    for i, s in enumerate(summaries, 1):
        console.print(f"\n  [bold cyan]{i}. {s['title']}[/bold cyan]")
        console.print(f"     [dim]— {s['source']}[/dim]")
    console.print()

    # ── ⚡ Quick Summary ──
    console.print(
        Panel(
            "\n".join(f"• {s['summary']}" for s in summaries),
            title="[bold magenta]⚡ Quick Summary[/bold magenta]",
            border_style="magenta",
            box=box.ROUNDED,
            padding=(1, 2),
        )
    )
    console.print()

    # ── 📰 Morning Brief ──
    console.print(
        Panel(
            brief,
            title="[bold green]📰 Morning Brief[/bold green]",
            border_style="green",
            box=box.ROUNDED,
            padding=(1, 2),
        )
    )
    console.print()

    # ── 🧠 Why It Matters ──
    console.print(
        Panel(
            why_it_matters,
            title="[bold red]🧠 Why It Matters[/bold red]",
            border_style="bright_red",
            box=box.HEAVY,
            padding=(1, 2),
        )
    )
    console.print()
    console.rule("[dim]End of Brief[/dim]", style="cyan")
    console.print()
