from creator import create_agents
import importlib
import os

def run():
    agent_files = create_agents(3)

    for file in agent_files:
        module_name = os.path.splitext(os.path.basename(file))[0]
        module = importlib.import_module(f"generated_agents.{module_name}")
        print(module.run())

if __name__ == "__main__":
    run()
