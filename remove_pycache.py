import os
import shutil


PROJECT_HOME = os.pardir
print(PROJECT_HOME)

for root, dirs, files in os.walk(PROJECT_HOME):
    for d in dirs:
        if d.endswith('.pytest_cache') or d == '__pycache__':
        	directory_path = os.path.join(root, d)
        	print(directory_path)
        	shutil.rmtree(directory_path)