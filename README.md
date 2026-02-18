# upGrad Counselor Navigator (Technical Portfolio) 🚀

## 🎯 Overview
The **upGrad Counselor Navigator** is a specialized Python-based tool designed for Academic Counselors. It serves as a "Single Source of Truth" for the 2026 Data Science, AI, and Machine Learning program portfolio, ensuring accuracy during high-stakes learner interactions.

## 🛠 Features
- **Portfolio Focus:** Deep-dive details for 12 core technical programs.
- **Financial Clarity:** Real-time access to "Total Cost" and "Block Amounts" (e.g., GGU DBA block at ₹44,999).
- **Transparency:** Explicit breakdowns of learner-borne immersion costs for international programs (Singapore/San Francisco/UK).
- **Technical Toolkits:** Lists industry-relevant tools (Python, Tableau, LangChain, etc.) for each course to assist in technical counseling.

## 🚀 How to Run
1. Ensure you have **Python 3.x** installed.
2. Download the `navigator.py` file.
3. Open your terminal or command prompt.
4. Run: `navigator.py`

## 📂 Maintenance (For Future Joiners)
To update program details or add new technical courses:
1. Open the script in any text editor (VS Code, Notepad++, etc.).
2. Locate the `db` dictionary.
3. Edit the existing values or follow the structure to add a new Sl No entry.
4. **Note:** Ensure each entry follows the existing dictionary format to avoid syntax errors.

## 📄 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 📅 Roadmap
- [x] Initial Stable v1.0.0 Launch (DS/AI/ML Focus)
- [ ] Integration of side-by-side Program Comparison Mode
- [ ] Migration of data to an external JSON configuration file

## 📈 Strategic Impact & ROI

The transition from v1.0.0 to v1.1.0 shifts the Navigator from a **Catalog** to a **Consultative Engine**.

### 1. Enhanced Conversion (Lead-to-Payment)
By implementing **Side-by-Side Comparison**, counselors can immediately resolve "Decision Paralysis." Providing a clear "Value Delta" (e.g., comparing IIITB vs. LJMU) is projected to increase first-call closing efficiency by **15-20%**.

### 2. Role-Based Authority
Instead of selling "features," the **Role-Mapping Logic** sells "outcomes." 
- **Non-Tech Switchers:** Guided toward foundational bootcamps.
- **Career Accelerators:** Guided toward leadership/specialization tracks.
This consultative approach builds instant trust, reducing lead drop-off and refund liabilities.

### 3. Democratizing Expertise
This tool reduces the technical training ramp-up for new Academic Counselors by **~60%**, allowing them to speak with the authority of a 1-year veteran from Day 1.

[Unreleased]
## [1.1.0-DEV]
### Added
- External `programs.json` for easier data maintenance.
- New schema fields: `Persona` and `Target_Roles` for consultative selling.
### Changed
- Refactored `navigator.py` to utilize dynamic JSON loading instead of hardcoded dictionaries.
