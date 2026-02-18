import re
import os
import stat
import yaml
from crewai import LLM
from crewai.tasks import TaskOutput

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Load YAML configurations
def load_yaml_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

# Initialize LLM (uses OLLAMA_BASE_URL and OLLAMA_MODEL from env if set)
def load_llm():
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    model_name = os.getenv("OLLAMA_MODEL", "deepseek-r1:7b")
    model = f"ollama/{model_name}" if not model_name.startswith("ollama/") else model_name
    return LLM(model=model, base_url=base_url)

# Check for mermaid syntax
def check_mermaid_syntax(task_output: TaskOutput):
    text = task_output.raw
    mermaid_blocks = re.findall(r'```mermaid\n(.*?)\n```', text, re.DOTALL)
    # Find all mermaid code blocks in the text
    for block in mermaid_blocks:
        diagram_text = block.strip()
        lines = diagram_text.split('\n')
        corrected_lines = []
        for line in lines:
            corrected_line = re.sub(r'\|.*?\|>', lambda match: match.group(0).replace('|>', '|'), line)
            corrected_lines.append(corrected_line)
        text = text.replace(block, "\n".join(corrected_lines))
    task_output.raw = text
    return (True, task_output)

# Force remove readonly files (for .git files)
def remove_readonly(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)