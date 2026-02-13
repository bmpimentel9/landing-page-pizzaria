# Perfumaria Sumirê - Automated Analysis Pipeline

**V4 Carvalho Consultoria Digital**

## 📋 Overview

Automated pipeline for creating comprehensive digital presence analysis presentations.

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r ../requirements.txt

# Run complete pipeline
python main.py

# Or run steps individually
python 01_browser_automation.py
python 02_llm_testing.py
python 03_chart_generator.py
python 04_pptx_builder.py
python validate.py
```

## 📁 Scripts

- **config.py** - Configuration and color palette
- **utils.py** - Utility functions
- **01_browser_automation.py** - Data collection (mock + real)
- **02_llm_testing.py** - LLM platform testing
- **03_chart_generator.py** - Generate 7 charts
- **04_pptx_builder.py** - Build 13-slide PPTX
- **validate.py** - Validation checks
- **main.py** - Main pipeline orchestrator

## 📊 Output

Final presentation: `../output/sumire-analise-digital.pptx` (13 slides)

## ⚙️ Options

```bash
python main.py --skip-data      # Skip data collection
python main.py --validate-only  # Only validate
```

## 🎨 Customization

Edit `config.py` to change:
- Colors (V4 Carvalho brand palette)
- Company data (Sumirê info)
- Competitors list
- LLM platforms to test

## 🔍 Validation

Run `python validate.py` to check:
- ✅ Data files exist
- ✅ All 7 charts generated
- ✅ PPTX has 13 slides

---

See `../README.md` for complete documentation.
