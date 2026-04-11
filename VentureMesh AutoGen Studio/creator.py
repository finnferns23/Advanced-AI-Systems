import os
from agent import generate_idea
from config import GENERATED_DIR

def create_agent_file(index: int):
    filename = os.path.join(GENERATED_DIR, f"agent_{index}.py")
    code = f'''
def run():
    return "Generated idea from agent {index}"
'''
    with open(filename, "w") as f:
        f.write(code)
    return filename

def create_agents(n=3):
    files = []
    for i in range(1, n+1):
        files.append(create_agent_file(i))
    return files
