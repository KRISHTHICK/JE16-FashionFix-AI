import subprocess

def chat_with_fashion_agent(prompt):
    cmd = f"A user needs help with this outfit issue: {prompt}. Suggest stylish and creative solutions."
    result = subprocess.run(["ollama", "run", "tinyllama", cmd], capture_output=True, text=True)
    return result.stdout.strip()
