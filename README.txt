RRCE IEEE STUDENT BRANCH WEBSITE (DEMO)

1. Extract this ZIP file.
2. Open the rrce_ieee_portal folder in VS Code.
3. Open Terminal > New Terminal.
4. Create a virtual environment:
   py -m venv .venv
5. Activate it in PowerShell:
   .\.venv\Scripts\Activate.ps1
   If PowerShell blocks activation, run:
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   then activate again.
6. Install Flask:
   python -m pip install -r requirements.txt
7. Run:
   python app.py
8. Open this address in your browser:
   http://127.0.0.1:5000

IMPORTANT:
- This is an original student-branch demo inspired by the general content layout of IEEE-USA.
- It is not an official IEEE or RRCE website.
- Replace sample event details and add approved RRCE/IEEE logos and contact details before publishing.
- The form currently shows a demo confirmation only; it does not save or email registrations.
