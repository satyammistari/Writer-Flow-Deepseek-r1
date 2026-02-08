# Documentation Writer Flow using CrewAI and Deepseek-R1

This project implements a documentation writing agentic workflow that can generate documentation for your code.

We use:
- CrewAI for multi-agent orchestration.
- Ollama for serving Deepseek-R1 locally.
- Cursor IDE as the MCP host.

---
## Step-by-step: How to run this project

### Step 1: Install Ollama (for the AI model)

- **Windows:** Download and install from [ollama.com](https://ollama.com).
- **Linux:** Run:
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```
- **macOS:** Install via [ollama.com](https://ollama.com) or Homebrew.

Then pull the Deepseek-R1 model:
```bash
ollama pull deepseek-r1
```

### Step 2: Install Python dependencies

Use **Python 3.12 or later**. From the project folder run:

```bash
pip install crewai crewai-tools ollama mcp
```

If you use **uv**:
```bash
uv sync
```

### Step 3: Configure the MCP server in Cursor

1. Open **Cursor** → **Settings** (gear icon or `Ctrl+,`).
2. Go to **MCP** (Model Context Protocol).
3. Add a **new global MCP server** (or edit the config file).
4. Add this to the MCP JSON config:
   ```json
   {
       "mcpServers": {
           "doc-writer": {
               "url": "http://127.0.0.1:8000/sse"
           }
       }
   }
   ```
5. Save. You should see **doc-writer** listed in MCP settings. **Do not turn it on yet** (the server must be running first).

### Step 4: Start the documentation writer server

1. Open a terminal.
2. Go to the project folder:
   ```bash
   cd "d:\Agents systems\documentation-writer-flow"
   ```
   (Use your actual path to the project.)
3. Start the server:
   ```bash
   python server.py
   ```
4. Leave this terminal open. You should see no errors; the server will listen on `http://127.0.0.1:8000`.

### Step 5: Connect the server in Cursor

1. In Cursor **Settings → MCP**, find **doc-writer**.
2. **Toggle the switch ON** to connect Cursor to your running server.

### Step 6: Use it

- In a Cursor chat, ask to generate documentation and provide a **GitHub repository URL**.
- The doc-writer tools will run the flow and produce documentation.
- You can also ask to **list** or **view** generated docs (e.g. files in `docs/`).

---

## Setup reference (short)

**Install Ollama**
```bash
# Linux
curl -fsSL https://ollama.com/install.sh | sh
ollama pull deepseek-r1
```

**Install Dependencies**
```bash
pip install crewai crewai-tools ollama mcp
# or: uv sync
```

**Run the server**
```bash
cd path/to/documentation-writer-flow
python server.py
```

Then add the MCP server URL `http://127.0.0.1:8000/sse` in Cursor MCP settings and toggle it on.

---

