# NLP in Practice: Text Analysis and Classification (Task 12)

This repository contains two parts:
1. A rule-based Resume Information Extractor (phone numbers and emails).
2. Sentiment Classification on a small custom dataset (positive, negative, neutral).

Structure:
```
NLP_Text_Analysis_Task12/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── sample_resumes/
│   │   ├── resume1.txt
│   │   ├── resume2.txt
│   │   └── resume3.txt
│   └── sentiment_dataset.csv
│
├── output/
│   └── output.json
│
├── resume_extractor/
│   └── resume_extractor.py
│
└── sentiment_analysis/
    └── sentiment_classification.ipynb
```

## How to run

1. Install requirements:
```
pip install -r requirements.txt
```

2. Run the resume extractor:
```
python resume_extractor/resume_extractor.py
```
This reads `data/sample_resumes/*.txt` and writes `output/output.json`.

3. Open the notebook:
```
jupyter notebook sentiment_analysis/sentiment_classification.ipynb
```
or open it in VS Code / Colab.

