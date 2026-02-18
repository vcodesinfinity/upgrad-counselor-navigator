import json
import os
import textwrap

# =================================================================
# PROJECT: upGrad AC Navigator
# VERSION: 1.1.0-FIXED
# STATUS:  Infrastructure Stable (External JSON)
# AUTHOR:  VK
# =================================================================

def load_data():
    """Dynamically locates and loads the JSON file based on script location."""
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, 'programs.json')
    
    if not os.path.exists(file_path):
        print(f"\n[!] ERROR: Could not find {file_path}")
        print("Ensure 'programs.json' is in the same folder as this script.")
        return {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("\n[!] ERROR: 'programs.json' has a syntax error (check your commas/brackets).")
        return {}

def show_menu(db):
    """Displays a formatted table of Sl Nos and Program Names for quick reference."""
    print("\n" + "="*95)
    print(f"{'Sl No':<8} | {'Abbr':<12} | {'Program Name'}")
    print("-" * 95)
    
    # Sort keys numerically so 10 comes after 9 (not after 1)
    sorted_keys = sorted(db.keys(), key=lambda x: int(x))
    for key in sorted_keys:
        print(f"{key:<8} | {db[key].get('Abbr', 'N/A'):<12} | {db[key].get('Program', 'Unknown')}")
    print("="*95)

def display_program(program_id, db):
    """Formats and prints detailed information for a single program."""
    data = db.get(str(program_id))
    if not data:
        print(f"\n[!] Invalid Selection '{program_id}'. Please choose a Sl No from the list.")
        return

    wrapper = textwrap.TextWrapper(width=95, subsequent_indent="    ")
    
    print("\n" + "█"*95)
    print(f" {data.get('Abbr', 'N/A')} | {data.get('Program', 'N/A').upper()} ")
    print("█"*95)
    
    # List of fields to display (Label, JSON Key)
    fields = [
            ("Course Type", "Course Type"),
            ("Duration", "Duration"),
            ("Eligibility", "Eligibility"),
            ("Mode", "Learning Mode"),
            ("Certificates", "Certificates"),
            ("Faculty", "Academic Faculty"),
            ("Industry", "Industry Experts"),
            ("Tools", "Relevant Tools"),
            ("Pi", "Pi"),  
            ("Immersion", "Immersion"),
            ("Top Projects", "Top Projects"),
            ("Cost", "Total Cost"),
            ("Block Amount", "Block Amount"),
            ("Pitch", "Counselor Pitch")
    ]

    for label, key in fields:
        val = data.get(key)
        if val and val != "N/A":
            print(f"● {label:<15}: {wrapper.fill(val)}")
    
    # Career Metadata for v1.1 Logic
    print("-" * 95)
    roles = data.get('Target_Roles', [])
    print(f"● Target Roles  : {', '.join(roles) if roles else 'N/A'}")
    print(f"● Best For      : {data.get('Persona', 'N/A')}")
    print("="*95)

def main():
    db = load_data()
    if not db:
        input("\nPress Enter to exit...")
        return

    while True:
        show_menu(db)
        print("\n[ Menu: Enter Sl No | Type 'q' to Quit ]")
        choice = input("Selection > ").strip().lower()
        
        if choice == 'q':
            print("\nExiting Navigator. Happy Counseling!")
            break
        
        # In the next update, we will handle comma-separated choices here
        display_program(choice, db)
        input("\n>>> Press ENTER to return to the Main Menu...")

if __name__ == "__main__":
    main()