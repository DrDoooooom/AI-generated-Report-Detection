# AI Generated Report Detector

This project detects if a report text is generated by AI or written by a human. It uses natural language processing and named entity recognition to analyze the text.

# How it Works

   * Uses spaCy for NER with the en_core_web_sm model
   * Focuses on detecting "ORG" named entities which are more prevalent in AI text
   * Classifies report as AI generated if "ORG" entities are found, else considers it human written

# Usage

Run python detector.py and input/upload text for analysis.

# Requirements

   * Python
   * spaCy
   * Tkinter

# Limitations

   * Accuracy decreases for advanced AI generation methods
   * Works best for English text
   * PDF extraction can be unreliable
