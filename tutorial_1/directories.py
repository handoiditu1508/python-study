from pathlib import Path

current_path = Path(__file__)
print(str(current_path))

# input here is the relative path from the folder of the terminal
path = Path("modules")
print(path.exists())

path = Path("tutorial_1")
print(path.exists())

for file in path.glob("*.py"):
    print(file)
