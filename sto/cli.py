import os
import subprocess
import click

@click.group()
def cli():
    """Smart Test Orchestrator CLI"""
    pass

@cli.command()
@click.option('--dir', default='tests', help='Directory with tests')
def run(dir):
    """Discover and run tests with pytest"""
    if not os.path.exists(dir):
        click.echo(f"Test directory '{dir}' not found.")
        return
    click.echo(f"Running tests in '{dir}'...")
    subprocess.run(['pytest', dir])