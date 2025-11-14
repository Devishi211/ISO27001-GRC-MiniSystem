# ISO 27001 GRC Mini System

**Developed by:** Devishi Mahajan

---

## Overview

A mini interactive GRC (Governance, Risk, and Compliance) system based on ISO 27001 controls.
Helps users self-assess compliance, view remediation guidance, visualize results, and generate detailed reports.

The working model uses `iso27001_controls.json` (222 controls) and `main.py`.
For ease of understanding, the **sample output** demonstrates only the first 10 controls.

---

## Key Features

* View control summary by ID
* View remediation guidance by ID
* Conduct self-assessment for selected controls
* Visualize compliance results in graphs
* Generate detailed compliance report

---

## Getting Started

### Prerequisites

* Python 3.x
* VS Code or Jupyter Notebook

Required Python libraries:

* pandas
* matplotlib

Install dependencies via:

```bash
pip install -r requirements.txt
```

---

### Usage

1. Open `main.py` in VS Code.
2. Run the script:

```bash
python main.py
```

3. CLI Menu Options:

* **View control summary by ID**
* **View remediation guidance by ID**
* **Conduct self-assessment**

4. Self-Assessment:

* Enter compliance status for each control: **Yes, Partial, No, or Skip**
* Can select the full range of controls or a custom range, e.g., `controls[10:30]`

5. Visualization & Report:

* Option to view a pie chart of compliance status
* Detailed report includes **control ID, title, status, and remediation**

---

## Future Enhancements

* Downloadable reports (PDF/Excel)
* Support for other compliance frameworks (GDPR, DPDP)
* Advanced CLI options (range selection, multiple assessments, comparison)
* Enhanced input handling beyond standard options
* Automated dashboards with richer visuals

---

## License

Open for personal and educational use. Adapt and extend as needed.
