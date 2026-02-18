# Changelog - upGrad AC Navigator

All notable changes to this project will be documented in this file.
## [1.1.0-STABLE] - 2026-02-18
### Added
- External `programs.json` for easier data maintenance.
- New schema fields: `Persona` and `Target_Roles` for consultative selling.
- "Press Enter to continue" logic to prevent menu auto-scroll.
- Dynamic Catalog Menu showing Sl No, Abbr, and Program Name.
- Support for optional fields: `Pi Pack`, `Immersion`, and `Top Projects`.
### Changed
- Refactored `navigator.py` to utilize dynamic JSON loading instead of hardcoded dictionaries.
- Terminal pathing issues using absolute directory mapping (`os.path`).
- Numeric sorting logic for programs (10, 11, 12 now follow 9).

## [1.0.0] - 2026-02-17
### Added
- **Final Technical Portfolio:** Confirmed all 12 DS, AI, and ML programs.
- **DBA Seat Block Policy:** Updated GGU DBA block amount to ₹ 44,999.
- **Immersion Transparency:** Added cost breakdown for international immersions (Transfers, Visa, Insurance, etc.).
- **Relevant Tools Section:** Integrated industry tools for every program to assist in technical counseling.
- **Enhanced UI:** Optimized console display width to 95 characters to handle high-detail course descriptions.

### Fixed
- Fixed text alignment and wrapping logic for long eligibility criteria.
- Standardized program abbreviations across the database.

## [0.7.0] - 2026-02-15
### Added
- Initial build (Beta).
- Basic lookup functionality for 11 programs.
- Fundamental cost and duration details.
