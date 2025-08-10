<div align="center">

# 🔐 AI Security Labs (Offline)
**Hands-on, offline-friendly labs for teaching secure AI engineering**  
*Prompt Injection · Adversarial Examples · Model Extraction · Data Poisoning*

[![CI](https://img.shields.io/github/actions/workflow/status/your-org/ai-security-labs-offline/ci.yml?label=lint)](./.github/workflows/ci.yml)
[![Docs](https://img.shields.io/badge/docs-mkdocs--material-blue)](https://your-org.github.io/ai-security-labs-offline/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

</div>

## 🚀 Why this repo?
- **Truly offline**: All datasets and sample images are bundled
- **Security-first**: Each lab maps to **NIST AI RMF** and **MITRE ATLAS**
- **Fast to run**: CPU-only, minimal dependencies, simple scripts
- **Training-ready**: Step-by-step docs, screenshots, and report templates

## 🧪 Labs
| # | Title | What you’ll learn | Folder |
|---|-------|--------------------|--------|
| 1 | Prompt Injection | Jailbreaks, hidden directives, guardrails | `labs/lab1_prompt_injection` |
| 2 | Adversarial Examples | FGSM against a simple classifier | `labs/lab2_adversarial_examples` |
| 3 | Model Extraction | API scraping, cloning, rate limiting, auth | `labs/lab3_model_extraction` |
| 4 | Data Poisoning | Detecting label flips/outliers; retraining | `labs/lab4_data_poisoning` |

> Full documentation: **https://your-org.github.io/ai-security-labs-offline/**

## ⚡ Quick start
```bash
python3 -m venv .venv
source .venv/bin/activate     # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## ▶️ Run a lab (example)
```bash
cd labs/lab3_model_extraction
python server.py                 # http://127.0.0.1:8000/predict (Terminal A)
python attacker_extract.py --n 2000 --outfile stolen.csv   # (Terminal B)
python mitigate_server.py --api-key SECRET123 --rate 5     # hardening
```

## 🧭 Framework Mapping
- **NIST AI RMF**: GV.3, GV.4, MP.3, MP.4, MP.5, MS.1–MS.3, MG.2–MG.5  
- **MITRE ATLAS**: Prompt Injection, Adversarial Example Generation, Model Extraction, Training Data Poisoning, Model Integrity Compromise

## 🤝 Contributing
We ❤️ PRs! See [CONTRIBUTING.md](./CONTRIBUTING.md) and our [Code of Conduct](./CODE_OF_CONDUCT.md).

## 🔒 Security
These labs are for **offline training**. Don’t expose the APIs to the public internet. See [SECURITY.md](./SECURITY.md).

---

<div align="center">
Made with ❤️ for security engineers leveling up their AI chops.
</div>
