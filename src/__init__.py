import os 
import sys 
from src.mathmind_mcp_server import server

def main():
    server.main()

# Optionally expose other important items at package level
__all__ = ["main", "server"]