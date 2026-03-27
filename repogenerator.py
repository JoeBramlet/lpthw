import os

# Root folder for your project
root = "python3-companion-book"

# Directory structure
folders = {
    "chapters": [f"ex{i:02}.md" for i in range(1, 53)],
    "exercises": [f"ex{i:02}" for i in range(1, 53)],
    "templates": ["chapter_template.md"],
    "book": ["preface.md", "introduction.md", "outline.md"],
}

# Create root folder
os.makedirs(root, exist_ok=True)

# Create folders and files
for folder, files in folders.items():
    folder_path = os.path.join(root, folder)
    os.makedirs(folder_path, exist_ok=True)

    # Chapters and book files are simple markdown files
    if folder in ["chapters", "templates", "book"]:
        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write(f"# {file.replace('.md', '').title()}\n")
    
    # Exercises need subfolders and Python files
    if folder == "exercises":
        for ex in files:
            ex_path = os.path.join(folder_path, ex)
            os.makedirs(ex_path, exist_ok=True)

            # Create the three standard files
            py_files = [
                f"{ex}.py",
                f"{ex}b.py",
                f"{ex}_intro.py"
            ]

            for py in py_files:
                py_path = os.path.join(ex_path, py)
                if not os.path.exists(py_path):
                    with open(py_path, "w") as f:
                        f.write(f"# {py}\n")
