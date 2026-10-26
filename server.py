from fastmcp import FastMCP
import random

mcp=FastMCP("Basic remote server")

@mcp.tool()
def random_number():
    """Returns a random number between 1 and 100."""
    return random.randint(1, 100)

@mcp.tool()
def add(a:int,b:int)->int:
    """Returns the sum of two numbers."""
    return a + b

if __name__=="__main__":
    mcp.run(transport="http",port=8000,host="127.0.0.1")
