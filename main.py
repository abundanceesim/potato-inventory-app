# main.py by Abundance Esim
from presentation.potato_console_view import PotatoConsoleView
""" Main execution module."""

def main():
    """
    This is the entry point into the appliction. It makes use of all other layers in 
    the system to provide an interactive menu for the users.
    """
    potato_application = PotatoConsoleView()
    potato_application.startup()

main()