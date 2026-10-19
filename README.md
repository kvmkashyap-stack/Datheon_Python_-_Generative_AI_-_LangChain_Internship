# SmartExtract — LLM-Based Structured Information Extraction

## Project Overview

SmartExtract is a Python-based Generative AI application that extracts structured information from unstructured resume text using Google Gemini and LangChain.

Recruiters and organizations often receive resumes in different formats, making manual information extraction time-consuming and inconsistent. SmartExtract addresses this problem by converting resume text into structured, validated JSON data.

The application uses prompt engineering, few-shot examples, and Pydantic models to extract information while handling missing fields without intentionally inventing data.

## Problem Statement

Extracting candidate information from unstructured resumes manually can be repetitive and error-prone. The goal of this project is to build a reusable Python application that processes resume text and returns structured information in a consistent JSON format.

## Key Features

- **LLM-powered extraction:** Uses Google Gemini through LangChain.
- **Prompt engineering:** Uses structured instructions and few-shot examples to guide extraction.
- **Structured output:** Produces JSON data matching a defined Pydantic schema.
- **Data validation:** Validates email addresses, field types, and non-negative experience values.
- **Missing-field handling:** Represents missing scalar values as `null` and missing collections as empty lists.
- **JSON export:** Saves extracted resume information to `output/resume.json`.
- **Automated testing:** Includes pytest tests for prompt behavior and schema validation.
