import os
import re
import glob

def refactor_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Colors mapping
    content = re.sub(r'bg-indigo-600', 'bg-primary', content)
    content = re.sub(r'hover:bg-indigo-700', 'hover:bg-primary-light', content)
    content = re.sub(r'bg-indigo-700', 'bg-primary-dark', content)
    content = re.sub(r'bg-indigo-800', 'bg-primary-dark', content)
    content = re.sub(r'bg-indigo-900', 'bg-primary-dark', content)
    content = re.sub(r'bg-indigo-500', 'bg-primary-light', content)
    
    content = re.sub(r'text-indigo-600', 'text-primary', content)
    content = re.sub(r'text-indigo-700', 'text-primary-dark', content)
    content = re.sub(r'text-indigo-800', 'text-primary-dark', content)
    content = re.sub(r'text-indigo-900', 'text-primary-dark', content)
    content = re.sub(r'text-indigo-500', 'text-primary-light', content)
    
    content = re.sub(r'border-indigo-500', 'border-primary', content)
    content = re.sub(r'border-indigo-600', 'border-primary', content)
    content = re.sub(r'ring-indigo-500', 'ring-primary', content)
    content = re.sub(r'ring-indigo-600', 'ring-primary', content)
    
    content = re.sub(r'from-indigo-600', 'from-primary', content)
    content = re.sub(r'from-indigo-800', 'from-primary-dark', content)
    content = re.sub(r'from-indigo-900', 'from-primary-dark', content)
    content = re.sub(r'to-indigo-800', 'to-primary-light', content)
    content = re.sub(r'to-indigo-900', 'to-primary-dark', content)
    content = re.sub(r'to-indigo-600', 'to-primary-light', content)
    
    # Previous replace command did bg-sand-light instead of bg-white! We reverted it using git checkout. So it has blue again.
    content = re.sub(r'bg-blue-600', 'bg-primary', content)
    content = re.sub(r'hover:bg-blue-700', 'hover:bg-primary-light', content)
    content = re.sub(r'bg-blue-700', 'bg-primary-dark', content)
    content = re.sub(r'bg-blue-800', 'bg-primary-dark', content)
    content = re.sub(r'bg-blue-900', 'bg-primary-dark', content)
    content = re.sub(r'bg-blue-500', 'bg-primary-light', content)
    content = re.sub(r'bg-blue-50', 'bg-sand', content)
    content = re.sub(r'bg-blue-100', 'bg-sand', content)
    
    content = re.sub(r'text-blue-600', 'text-primary', content)
    content = re.sub(r'text-blue-700', 'text-primary-dark', content)
    content = re.sub(r'text-blue-800', 'text-primary-dark', content)
    content = re.sub(r'text-blue-900', 'text-primary-dark', content)
    content = re.sub(r'text-blue-500', 'text-primary-light', content)
    
    content = re.sub(r'border-blue-500', 'border-primary', content)
    content = re.sub(r'border-blue-600', 'border-primary', content)
    content = re.sub(r'ring-blue-500', 'ring-primary', content)
    content = re.sub(r'ring-blue-600', 'ring-primary', content)

    content = re.sub(r'from-blue-600', 'from-primary', content)
    content = re.sub(r'from-blue-800', 'from-primary', content)
    content = re.sub(r'from-blue-900', 'from-primary-dark', content)
    content = re.sub(r'to-blue-800', 'to-primary-light', content)
    content = re.sub(r'to-blue-900', 'to-primary-dark', content)
    content = re.sub(r'to-blue-600', 'to-primary-light', content)
    
    # Hero gradient specific rule
    content = re.sub(r'from-blue-900 via-blue-800 to-blue-900', 'from-primary-dark via-primary to-primary-dark', content)
    content = re.sub(r'from-blue-800 to-blue-600', 'from-primary to-primary-light', content)


    # 2. Hardcoded hex colors
    content = content.replace('#1E3A8A', '#3730A3') # Primary Dark
    content = content.replace('#2563EB', '#4F46E5') # Primary
    content = content.replace('#3B82F6', '#6366F1') # Primary Light

    # 3. Overall background. Replace `bg-gray-50` with `bg-sand` (for the warm sand background)
    content = re.sub(r'bg-gray-50', 'bg-sand', content)
    content = re.sub(r'bg-slate-50', 'bg-sand', content)
    
    # Fix the persistent voice button that I just broke with Emerald earlier
    content = re.sub(r'bg-emerald-500', 'bg-primary', content)
    content = re.sub(r'hover:bg-emerald-600', 'hover:bg-primary-light', content)

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

print("Done")
