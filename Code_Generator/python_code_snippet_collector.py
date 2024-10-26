from github import Github
import re
from datasets import Dataset
from transformers import PreTrainedTokenizer

g = Github("your_github_token")

repo = g.get_repo("openai/gym")

# Extract Code functions
def extract_functions_from_code(code):
    pattern = re.compile(r"def\s+(\w+)\s*(.*):")
    functions = pattern.findall(code)
    return functions

# Fetch .py files from the repo
files = []
contents = repo.get_contents("")
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    elif file_content.path.endswith(".py"):
        files.append(file_content)

# Extract functions and create datasets
data = {"code": [], "function_name": []}
for file in files:
    code = file.decoded_content.decode("utf-8")
    functions = extract_functions_from_code(code)
    for function in functions:
        data["code"].append(code)
        data["function_name"].append(function)

# Create a Hugging Face dataset
dataset = Dataset.from_dict(data)
dataset.save_to_disk("data/")
print("Dataset created and Saved Successfully")