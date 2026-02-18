import json
import os
import textwrap

# =================================================================
# PROJECT: upGrad AC Navigator
# VERSION: 1.2.0 (Comparison Engine & Logic Refinement)
# STATUS:  Stable Infrastructure
# AUTHOR:  Vinay Kumar
# =================================================================

def load_data():
    """Dynamically locates and loads the JSON file based on script location."""
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, 'programs.json')
    
    if not os.path.exists(file_path):
        print(f"\n[!] ERROR: Could not find {file_path}")
        return {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("\n[!] ERROR: 'programs.json' syntax error.")
        return {}

def show_menu(db):
    """Displays a formatted table of Sl Nos and Program Names."""
    print("\n" + "="*95)
    print("   upGrad 2026 OFFICIAL AC NAVIGATOR (Working Professionals) (v1.2.0 STABLE)   ")
    print("\n" + "="*95)
    print(f"{'Sl No':<8} | {'Abbr':<12} | {'Program Name'}")
    print("-" * 95)
    sorted_keys = sorted(db.keys(), key=lambda x: int(x))
    for key in sorted_keys:
        print(f"{key:<8} | {db[key].get('Abbr', 'N/A'):<12} | {db[key].get('Program', 'Unknown')}")
    print("="*95)

def compare_programs(ids, db):
    """Side-by-side comparison logic for two selected programs."""
    p1 = db.get(ids[0])
    p2 = db.get(ids[1])
    
    if not p1 or not p2:
        print(f"\n[!] Error: One or both Sl Nos ({ids}) are invalid.")
        return

    col_w = 38   # Program column width
    lbl_w = 15   # Label column width
    
    print("\n" + "█"*95)
    print(f"{'COMPARING':<{lbl_w}} | {p1['Abbr']:^{col_w}} | {p2['Abbr']:^{col_w}}")
    print("█"*95)

    # Specific metrics for a quick sales comparison
    metrics = [
        ("Full Program", "Program"),
        ("Duration", "Duration"),
        ("Total Cost", "Total Cost"),
        ("Certificates", "Certificates"),
        ("Eligibility", "Eligibility"),
        ("Tools", "Relevant Tools"),
        ("Best For", "Persona")
    ]

    for label, key in metrics:
        wrap1 = textwrap.wrap(str(p1.get(key, "N/A")), width=col_w-2)
        wrap2 = textwrap.wrap(str(p2.get(key, "N/A")), width=col_w-2)
        
        max_lines = max(len(wrap1), len(wrap2))
        for i in range(max_lines):
            l_text = label if i == 0 else ""
            w1 = wrap1[i] if i < len(wrap1) else ""
            w2 = wrap2[i] if i < len(wrap2) else ""
            print(f"{l_text:<{lbl_w}} | {w1:<{col_w}} | {w2}")
        print("-" * 95)

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
    
    fields = [
        ("Course Type", "Course Type"),
        ("Duration", "Duration"),
        ("Eligibility", "Eligibility"),
        ("Mode", "Learning Mode"),
        ("Certificates", "Certificates"),
        ("Faculty", "Academic Faculty"),
        ("Industry", "Industry Experts"),
        ("Tools", "Relevant Tools"),
        ("Top Projects", "Top Projects"),
        ("Pi Pack", "Pi"),
        ("Immersion", "Immersion"),
        ("Cost", "Total Cost"),
        ("Block Amount", "Block Amount"),
        ("Counselor Pitch", "Counselor Pitch")
    ]

    for label, key in fields:
        val = data.get(key)
        if val and val != "N/A":
            print(f"● {label:<15}: {wrapper.fill(str(val))}")
    
    print("-" * 95)
    print(f"● Target Roles  : {', '.join(data.get('Target_Roles', []))}")
    print(f"● Best For      : {data.get('Persona', 'N/A')}")
    print("="*95)

def main():
    db = load_data()
    if not db:
        input("\nPress Enter to exit...")
        return

    while True:
        # Optional: Uncomment the next line to clear screen on each loop
        # os.system('cls' if os.name == 'nt' else 'clear') 
        
        show_menu(db)
        print("\n[ Selection: Enter '3' for Details | Enter '3,4' to Compare | 'q' to Quit ]")
        choice = input("Selection > ").strip().lower()
        
        if choice == 'q':
            print("\nExiting Navigator. Happy Counseling!")
            break
        
        # --- Logic Gate: Multi-select vs Single-select ---
        if "," in choice:
            ids = [x.strip() for x in choice.split(",")]
            compare_programs(ids, db)
        elif choice:
            display_program(choice, db)
        else:
            continue # Handles accidental empty Enters
        
        # Universal pause for the user to read before the menu returns
        input("\n>>> Press ENTER to return to Menu...")

if __name__ == "__main__":
    main()