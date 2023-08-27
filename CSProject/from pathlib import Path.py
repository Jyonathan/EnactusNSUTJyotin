from pathlib import Path
path= Path("CSProject")
for i in path.glob("*.py"):
    print(i)