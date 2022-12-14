import os

# Directories needed
dirs = [
    os.path.join("data", "raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src",
    "data_collection"
]

# Create the directories and write a .gitkeep file inside each directory (we cannot commit an empty directory in git)
for dir in dirs:
    os.makedirs(dir , exist_ok=True)
    with open(os.path.join(dir , ".gitkeep"),"w") as f: # writing "w" for specifing that we want to write the file also
        pass
        

files = [
    'params.yaml',
    '.gitignore', # Here we push all the files which we dont want to push into git
    os.path.join('src' , '__init__.py' )

]

for file_ in files:
    with open(file_, "w") as f:
        pass