#!/usr/bin/env python3
"""
Made By Ryan Cham Rui Yang -Last update 12 Jan 2026
bruteforcehelper.py - Password variation generator for security testing
Usage: python3 bruteforcehelper.py <input_file> <output_file>
"""

import sys
import string

def generate_variations(username):
    """Generate password variations from a username"""
    variations = set()
    
    # Original username
    variations.add(username)
    
    # Basic case variations
    variations.add(username.lower())
    variations.add(username.upper())
    variations.add(username.capitalize())
    
    # Remove special characters and create variations
    clean = ''.join(c for c in username if c.isalnum())
    if clean != username:
        variations.add(clean)
        variations.add(clean.lower())
        variations.add(clean.upper())
        variations.add(clean.capitalize())
    
    # Replace special characters with common substitutes
    special_replacements = {
        ' ': '_',
        '%': '_',
        '@': 'a',
        '$': 's',
        '!': 'i',
        '3': 'e',
        '1': 'i',
        '0': 'o',
        '4': 'a',
        '5': 's',
        '7': 't',
    }
    
    for old, new in special_replacements.items():
        if old in username:
            replaced = username.replace(old, new)
            variations.add(replaced)
            variations.add(replaced.lower())
            variations.add(replaced.upper())
            variations.add(replaced.capitalize())
    
    # Add common number suffixes
    common_numbers = ['123', '1234', '12345', '1', '01', '2024', '2025']
    base_variations = list(variations.copy())
    
    for base in base_variations:
        for num in common_numbers:
            variations.add(base + num)
            variations.add(base.lower() + num)
            variations.add(base.capitalize() + num)
    
    # Add common prefixes/suffixes
    common_additions = ['!', '@', '#', '123!', '!123', '_123']
    
    for base in base_variations:
        for addition in common_additions:
            variations.add(base + addition)
            variations.add(addition + base)
    
    # Year variations
    years = ['2024', '2025', '23', '24', '25']
    for base in base_variations:
        for year in years:
            variations.add(base + year)
    
    # Common patterns
    if len(username) > 0:
        # First letter capitalized + rest lowercase + numbers
        variations.add(username[0].upper() + username[1:].lower() + '123')
        variations.add(username[0].upper() + username[1:].lower() + '1')
        
    return sorted(variations)

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_file> <output_file>")
        print("Example: python3 bruteforcehelper.py usernames.txt results.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        # Read usernames from input file
        with open(input_file, 'r', encoding='utf-8') as f:
            usernames = [line.strip() for line in f if line.strip()]
        
        if not usernames:
            print(f"Error: No usernames found in {input_file}")
            sys.exit(1)
        
        print(f"Loaded {len(usernames)} username(s) from {input_file}")
        
        # Generate variations for all usernames
        all_variations = []
        for username in usernames:
            variations = generate_variations(username)
            all_variations.extend(variations)
            print(f"Generated {len(variations)} variations for: {username}")
        
        # Remove duplicates while preserving order
        seen = set()
        unique_variations = []
        for var in all_variations:
            if var not in seen:
                seen.add(var)
                unique_variations.append(var)
        
        # Write to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            for variation in unique_variations:
                f.write(variation + '\n')
        
        print(f"\nTotal unique variations generated: {len(unique_variations)}")
        print(f"Results written to: {output_file}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied accessing files")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
