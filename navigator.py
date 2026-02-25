import json
import os
import textwrap

# =================================================================
# PROJECT: upGrad AC Navigator
# VERSION: 1.3.2 (UI Fixed Baseline)
# BRANCH:  dev
# =================================================================

def load_data(filename):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, filename)
    if not os.path.exists(file_path): return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def show_catalogue(db_p):
    """
    FIXED UI: Dynamically calculates column widths to prevent 
    overlapping borders with long abbreviations or names.
    """
    # Define Column Widths
    SL_WIDTH, ABBR_WIDTH, TOTAL_WIDTH = 6, 22, 98 # Increased to accommodate "EPGC-GenAI (IITKGP)"
    NAME_WIDTH = TOTAL_WIDTH - (SL_WIDTH + ABBR_WIDTH + 10) # Remaining space
    
    # Border Elements
    top = "╔" + "═"*(SL_WIDTH+2) + "╦" + "═"*(ABBR_WIDTH+2) + "╦" + "═"*(NAME_WIDTH+2) + "╗"
    sep = "╠" + "═"*(SL_WIDTH+2) + "╬" + "═"*(ABBR_WIDTH+2) + "╬" + "═"*(NAME_WIDTH+2) + "╣"
    bot = "╚" + "═"*(SL_WIDTH+2) + "╩" + "═"*(ABBR_WIDTH+2) + "╩" + "═"*(NAME_WIDTH+2) + "╝"

    print(f"\n{'upGrad AI & DS CATALOGUE v1.3.2':^{TOTAL_WIDTH}}\n" + top)
    print(f"║ {'ID':<{SL_WIDTH}} ║ {'Abbreviation':<{ABBR_WIDTH}} ║ {'Program Name':<{NAME_WIDTH}} ║\n" + sep)

    for k in sorted(db_p.keys(), key=int):
        # Wrap the name to fit the dynamic NAME_WIDTH
        wrapped = textwrap.wrap(db_p[k]['Program'], width=NAME_WIDTH) 
        # Print the first line
        print(f"║ {k:<{SL_WIDTH}} ║ {db_p[k]['Abbr']:<{ABBR_WIDTH}} ║ {wrapped[0]:<{NAME_WIDTH}} ║")
        # Print subsequent lines for long names
        for line in wrapped[1:]:
            print(f"║ {'':<{SL_WIDTH}} ║ {'':<{ABBR_WIDTH}} ║ {line:<{NAME_WIDTH}} ║")
    print(bot)

def main():
    db_p = load_data('programs.json')
    db_c = load_data('curriculum.json') # Loaded for future use
    
    while True:
        show_catalogue(db_p)
        print("\n[ s(id): Snapshot | d(id): Detailed | f: Filter | q: Quit ]")
        cmd = input("Selection > ").strip().lower()

        if cmd == 'q': 
            print("\nExiting Navigator. Happy Counseling!")    
            break
        elif cmd.startswith('s'): print(f"\n[DEV] Logic for Snapshot {cmd[1:]} coming in Milestone 2.")
        elif cmd.startswith('d'): print(f"\n[DEV] Logic for Detailed {cmd[1:]} coming in Milestone 2.")
        elif cmd == 'f': print("\n[DEV] Logic for Search coming in Milestone 3.")
        else: print("\n[!] Use commands like s1, d1, or f.")
        input("\nPress Enter...")

if __name__ == "__main__":
    main()
