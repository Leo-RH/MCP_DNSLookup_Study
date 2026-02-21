from mcp.server.fastmcp import FastMCP
import subprocess

mcp = FastMCP("Teste", json_response=True)

@mcp.tool()
def look_up_A_record(domain: str) -> str:
    """Look up a record of A type, that means it will search for a ipv4 record"""
    try:
        p = subprocess.run(["nslookup", "-type=a", domain, "8.8.8.8"], capture_output=True, text=True)
        if p.returncode == 0:
            return str(p.stdout).replace("\n", " ")
        else:
            return {"status": "error", "output": p.stderr}
    except:
        return {"status": "error", "output": "Unknown error"}


@mcp.tool()
def look_up_AAAA_record(domain: str) -> str:
    """Look up a record of AAAA type, that means it will search for a ipv6 record"""
    try:
        p = subprocess.run(["nslookup", "-type=aaaa", domain, "8.8.8.8"], capture_output=True, text=True)
        if p.returncode == 0:
            return str(p.stdout).replace("\n", " ")
        else:
            return {"status": "error", "output": p.stderr}
    except:
        return {"status": "error", "output": "Unknown error"}


@mcp.tool()
def look_up_MX_record(domain: str) -> str:
    """Look up a record of MX type, that means it will search for a mail record"""
    try:
        p = subprocess.run(["nslookup", "-type=mx", domain, "8.8.8.8"], capture_output=True, text=True)
        if p.returncode == 0:
            return str(p.stdout).replace("\n", " ")
        else:
            return {"status": "error", "output": p.stderr}
    except:
        return {"status": "error", "output": "Unknown error"}


mcp.run(transport="streamable-http")