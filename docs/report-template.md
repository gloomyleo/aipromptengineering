# 📝 AI Security Labs – Trainee Report Template

Use this template to capture your findings while running the labs.

---

## Participant
- **Name:**  
- **Date:**  
- **Team/Function:**  

## Environment
- **OS / Version:**  
- **Python Version:**  
- **CPU/GPU:** (CPU is fine)  
- **Anything unusual:**  

---

## Lab 1 – Prompt Injection
**Goal:** Understand how prompts can subvert LLM guardrails; test defenses.

### Prompts Attempted
| Prompt | Baseline Output (vulnerable) | Mitigated Output | Notes |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |

**Observations:**  
- What worked? What didn’t?  
- Any leakage or unsafe responses?  

**Controls/Mitigations to Carry Forward:**

---

## Lab 2 – Adversarial Examples (Digits)
**Goal:** Generate FGSM examples that change a classifier’s decision.

### Runs
| Epsilon | Success? | Comments |
|---:|:---:|---|
| 0.1 |  |  |
| 0.5 |  |  |
| 1.0 |  |  |

**Attach:** `adv_result.png` (original vs adversarial)  

**Observations:**  
- Visual distortion vs. attack success tradeoff  
- Which epsilon worked best and why?

---

## Lab 3 – Model Extraction (Iris API)
**Goal:** Approximate a model via API queries; test mitigations.

### Baseline (Vulnerable)
- **Collected samples:**  
- **Clone accuracy (holdout):**  

### Mitigated (API key + rate limit + reduced outputs)
- **429s observed?**  
- **Clone accuracy (holdout):**  
- **API key used:** yes / no

**Logs/Screenshots:**  
- Paste key excerpts showing 401/429 and attacker behavior.

**Mitigations to Adopt:**  
-  …

---

## Lab 4 – Data Poisoning Detection
**Goal:** Detect label flips/outliers; retrain and compare.

### Results
| Poison % | Contamination | Clean Acc | Poisoned Acc | Cleaned Acc | Removed Samples |
|---:|---:|---:|---:|---:|---:|
| 0.1 | 0.1 |  |  |  |  |

**Observations:**  
- How sensitive are results to parameters?  
- Any false positives from the anomaly detector?

---

## Framework Mapping (tick what you addressed)
- **NIST AI RMF:** GV.3 ☐ GV.4 ☐ MP.3 ☐ MP.4 ☐ MP.5 ☐ MS.1 ☐ MS.2 ☐ MS.3 ☐ MG.2 ☐ MG.3 ☐ MG.4 ☐ MG.5 ☐
- **MITRE ATLAS:** Prompt Injection ☐ Adversarial Examples ☐ Model Extraction ☐ Data Poisoning ☐ Model Integrity Compromise ☐

---

## Final Notes & Next Actions
- What would you harden in production?
- Any follow-up experiments?

---

**Downloads:**  
- PDF: [AI_Sec_Lab_Report_Template.pdf](assets/AI_Sec_Lab_Report_Template.pdf)
- Markdown: [report-template.md](report-template.md)

> To generate a DOCX, use Pandoc locally:
```bash
pandoc docs/report-template.md -o AI_Sec_Lab_Report_Template.docx
```
