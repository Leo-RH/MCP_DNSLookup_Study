# MCP Server Setup with Claude Code

## 🚀 How to Install Claude Code

### Prerequisites
- Node.js 18 or higher

### Installation

```bash
npm install -g @anthropic/claude-code
```

After installation, verify it's working:

```bash
claude --version
```

You'll need to authenticate on first run:

```bash
claude
```

Follow the prompts to log in with your Anthropic account.

---

## 🔧 Setting Up the MCP Server

This MCP server was created and registered using the built-in `claude mcp add` command, which makes it simple to connect external tools and services to Claude.

### Step 2 — Run the MCP Server

```bash
python3 path/to/server/dnslookupmcp.py
```

### Step 2 — Add the MCP Server

```bash
claude mcp add --transport http my-server http://localhost:8000/mcp
```


### Step 3 — Verify the Server is Registered

```bash
claude mcp list
```

This shows all currently configured MCP servers along with their status.

---

## ▶️ Execution Process in Claude Code

Once the MCP server is registered, it becomes available automatically when you start a Claude Code session.

### Starting Claude Code

```bash
claude
```

Claude Code will automatically attempt to connect to all registered MCP servers at startup. You'll see a confirmation in the terminal when a server connects successfully.

### Using the MCP Server in a Session

Once connected, the tools exposed by your MCP server are available directly to Claude. You can ask Claude to use them naturally in conversation:

```
> Use my-mcp-server to fetch the latest records from the database
```
Claude will identify the appropriate tool from your MCP server and invoke it.
