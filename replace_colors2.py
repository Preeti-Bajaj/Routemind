import os
import re

def refactor_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Clean up all leftover blue/indigo classes to use primary or sand variants.
    # Replace anything ending with -blue-X with -primary-X
    # Note: earlier we did some replacements like 'bg-primary' which is fine, we don't mess with them.
    # Just catch the rest: shadow-blue-X, border-blue-X, hover:border-blue-X, ring-blue-X, text-blue-X, bg-blue-X
    content = re.sub(r'(-)?blue-(\d+)', r'\1primary-\2', content)
    content = re.sub(r'(-)?indigo-(\d+)', r'\1primary-\2', content)

    # Some specific hardcoded backgrounds:
    content = content.replace('bg-[#f8faff]', 'bg-sand-light')
    
    # We should make sure we didn't end up with `bg-primary-primary-600` by accident 
    # (shouldn't happen since regex matches 'blue-').

    # Let's also enforce `bg-white` staying pure white for cards, but pages should use sand-light or sand.
    # The user wanted: Sand colors for page backgrounds and sections instead of pure white where appropriate.
    # Actually, we reverted `bg-white` earlier, but maybe something like `min-h-screen bg-gray-50` was fixed already to `bg-sand`
    
    # Let's change the color of hover:shadow-blue-400/40 etc. The regex handles it: shadow-primary-400/40.

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

print("Done phase 2")
