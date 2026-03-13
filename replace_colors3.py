import os
import re

def refactor_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    content = content.replace('#2563eb', '#4F46E5')
    content = content.replace('#1e3a8a', '#3730A3')
    content = content.replace('#3b82f6', '#6366F1')
    content = content.replace('#f8faff', '#FAF8F3')
    content = content.replace('#ffffff', '#FFFFFF') # just in case
    
    # Check for text-gray-800 or text-gray-900? 
    # Usually UI uses gray-800 for dark text. The prompt says TEXT DARK: #1F2937 (which is gray-800).
    # Since Tailwind text-gray-800 is #1F2937, it's correct.

    if original != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for root, _, files in os.walk('c:/Users/KIIT0001/OneDrive/Desktop/New folder/my-react-app/client/src'):
    for file in files:
        if file.endswith('.jsx') or file.endswith('.js') or file.endswith('.css') or file.endswith('.html'):
            filepath = os.path.join(root, file)
            # Ensure it's not node_modules
            if 'node_modules' not in filepath:
                refactor_file(filepath)

print("Done phase 3")
