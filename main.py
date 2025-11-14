import json
from datetime import datetime, timedelta, timezone
import matplotlib.pyplot as plt
import pandas as pd

# ---------------- Load controls ----------------
with open("iso27001_controls.json", "r") as f:
    controls = json.load(f)

# India Timezone (IST = UTC +5:30)
IST = timezone(timedelta(hours=5, minutes=30))

assessment = []

# ---------------- CLI Functions ----------------
def show_header():
    print("\n" + "="*70)
    print("ISO 27001 GRC Mini System – Interactive CLI")
    print("Developed by: Devishi Mahajan")
    print("Date & Time:", datetime.now(IST).strftime("%d-%m-%Y | %I:%M %p %Z"))
    print("="*70)

def show_menu():
    print("\nMAIN MENU")
    print("1. View Control Summary by ID")
    print("2. View Remediation Guidance by ID")
    print("3. Conduct Self-Assessment")
    print("0. Exit System")

def find_control(control_id):
    for c in controls:
        if c['id'].lower() == control_id.lower():
            return c
    return None

def visualize_results():
    if not assessment:
        print("No assessment data yet. Please complete the self-assessment first.")
        return
    df = pd.DataFrame(assessment)
    status_counts = df['status'].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('ISO 27001 Compliance Overview – Devishi Mahajan')
    plt.show()

def generate_report():
    if not assessment:
        print("No assessment data found. Please complete the self-assessment first.")
        return
    df = pd.DataFrame(assessment)
    total = len(df)
    yes = (df['status'] == 'yes').sum()
    partial = (df['status'] == 'partial').sum()
    no = (df['status'] == 'no').sum()
    score = ((yes + 0.5 * partial) / total) * 100
    timestamp = datetime.now(IST).strftime("%d-%m-%Y | %I:%M %p %Z")

    print("\n" + "="*85)
    print("ISO 27001 Mini Self-Assessment Report")
    print("Developed by: Devishi Mahajan")
    print(f"Generated on : {timestamp}")
    print("="*85)
    print(f"Total Controls Assessed : {total}")
    print(f"Compliant (Yes)       : {yes}")
    print(f"Partial Compliance    : {partial}")
    print(f"Non-Compliant (No)    : {no}")
    print(f"Overall Compliance    : {score:.2f}%")
    print("="*85)

    print("\nDetailed Control-wise Summary:\n")
    for c in assessment:
        print(f"{c['id']} – {c['title']}")
        print(f"  Status       : {c['status'].capitalize()}")
        ctrl = find_control(c['id'])
        if ctrl and 'remediation' in ctrl:
            print(f"  Remediation : {ctrl['remediation']}")
        print("-"*85)

    print("\nEnd of Report")
    print("Developed by: Devishi Mahajan – ISO 27001 GRC Mini System")
    print("="*85)

# ---------------- CLI Loop ----------------
while True:
    show_header()
    show_menu()
    choice = input("\nEnter your choice (0-3): ").strip()

    if choice == "1":
        cid = input("Enter Control ID (e.g., A.5.1): ").strip()
        c = find_control(cid)
        if c:
            print(f"\nControl Summary: {c['id']} – {c['title']}")
            print(f"Description : {c['summary']}")
            print(f"Question    : {c['question']}")
            print("-"*70)
        else:
            print("Control not found. Please check the ID and try again.")

    elif choice == "2":
        cid = input("Enter Control ID (e.g., A.5.1): ").strip()
        c = find_control(cid)
        if c:
            print(f"\nRemediation Guidance: {c['id']} – {c['title']}")
            print(f"Remediation Steps : {c['remediation']}")
            if 'source' in c:
                print(f"Source Reference : {c['source']}")
            print("-"*70)
        else:
            print("Control not found. Please check the ID and try again.")

    elif choice == "3":
        print("\nISO 27001 Self-Assessment")
        print("Please answer each control as: Yes / Partial / No / Skip\n")

        for c in controls[:]:  # All controls
            print(f"\n{c['id']} – {c['title']}")
            print(f"Question: {c['question']}")
            ans = input("Compliance Status (Yes/Partial/No/Skip): ").strip().lower()
            if ans not in ["yes", "partial", "no", "skip"]:
                ans = "skip"
            assessment.append({
                "id": c['id'],
                "title": c['title'],
                "status": ans
            })

        print("\nSelf-Assessment Completed Successfully.")

        choice_viz = input("\nWould you like to visualize your compliance status? (yes/no): ").strip().lower()
        if choice_viz == "yes":
            visualize_results()

        choice_report = input("Would you like to generate a detailed report? (yes/no): ").strip().lower()
        if choice_report == "yes":
            generate_report()
        else:
            print("\nExiting without generating report. You can view it later from the menu.")

    elif choice == "0":
        print("\nExiting ISO 27001 GRC Mini System.")
        print("Developed by: Devishi Mahajan | Thank you for using the tool.")
        print("="*70)
        break

    else:
        print("Invalid input. Please choose a valid menu option.")
