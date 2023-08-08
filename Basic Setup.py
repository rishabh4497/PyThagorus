import os

def create_directories_and_files():
    for directory in directories:
      os.makedirs(os.path.join(project_root, directory), exist_ok=True)

      #we need to create placeholder for python code inside our folders
      with open(os.path.join(project_root, directory, '__init__.py'), 'w') as init_file:
        pass

    print(f"This is our project structure under {project_root}")
    for directory in directories:
         print(f" - {directory}")

#This part is optional

def create_readme():
    with open(os.path.join(project_root, 'README.md'), 'w') as readme_file:
      readme_file.write(" We need to add MathFormula to python code\n")
      readme_file.write("This project is AI model that will convert math formulas to python code")
      readme_file.write(" Components \n")
      for directory in directories:
          readme_file.write(f"- {directory}\n")
      readme_file.write(" How to Run \n")
      readme_file.write(" All Instructions Here.\n")

    print(" Readme file is created")

# Now we need to define requirements

def create_requirements():
    with open(os.path.join(project_root, 'requirements.txt'), 'w') as requirements_file:
      requirements_file.write("numpy\nopencv-python\nsympy\n")

    print("reuirements file is completed")

project_root = "/content/PyThagorus"
os.makedirs(project_root, exist_ok=True)

directories = [
    'formula_parsing',
    'math_to_python',
    'image_preprocessing',
    'ocr',
    'integration',
    'testing',
    'ui',
    'documentation',
]

create_directories_and_files()
create_readme()
create_requirements()
