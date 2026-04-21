import os
import nbformat as nbf

nb = nbf.v4.new_notebook()

# Files in order of dependencies stringing them together
files = [
    "config.py",
    "utils/prompts.py",
    "data/sample_articles.py",
    "services/llm_service.py",
    "services/news_fetcher.py",
    "agents/summarizer.py",
    "agents/brief_generator.py",
    "utils/formatter.py",
    "main.py"
]

cells = []
cells.append(nbf.v4.new_markdown_cell("# 🗞️ AI Morning News Brief Notebook\nThis is a standalone notebook compiling the entire `AI Morning News Brief` project so you can run the pipeline directly here."))

cells.append(nbf.v4.new_markdown_cell("### 1. Install Dependencies & Setup Environment"))
cells.append(nbf.v4.new_code_cell('!pip install groq requests python-dotenv rich nbformat'))

setup_code = """import os
from dotenv import load_dotenv

# Load existing .env if present
load_dotenv()

# Set API Keys here if not using .env
if not os.getenv("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = "YOUR_GROQ_API_KEY_HERE"
    
if not os.getenv("NEWSAPI_KEY"):
    os.environ["NEWSAPI_KEY"] = ""  # Optional
"""
cells.append(nbf.v4.new_code_cell(setup_code))

def clean_content(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    lines = content.split("\n")
    new_lines = []
    
    # Internal project modules to strip imports for
    internal_mods = ["config", "utils.prompts", "data.sample_articles", "services.llm_service", 
                     "services.news_fetcher", "agents.summarizer", "agents.brief_generator", "utils.formatter"]
                     
    for line in lines:
        is_import = False
        for mod in internal_mods:
            if line.startswith(f"from {mod} import") or line.startswith(f"import {mod}"):
                is_import = True
                break
        
        # Don't execute main block in the notebook automatically
        if "if __name__ == " in line:
            break
            
        if not is_import:
            new_lines.append(line)
            
    return "\n".join(new_lines).strip()

for file in files:
    if os.path.exists(file):
        cells.append(nbf.v4.new_markdown_cell(f"### `{file}`"))
        code = f"# Source: {file}\n\n" + clean_content(file)
        cells.append(nbf.v4.new_code_cell(code))

cells.append(nbf.v4.new_markdown_cell("### 🎉 Run the Pipeline\nYou can now run the pipeline by executing the `run()` function below!"))
cells.append(nbf.v4.new_code_cell('run("AI in Healthcare", use_api=False)'))

nb.cells = cells

output_path = "AI_Morning_News_Brief.ipynb"
with open(output_path, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"✅ Created Notebook: {output_path}")
