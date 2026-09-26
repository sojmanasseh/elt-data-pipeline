# Automated ETL Data Sanitization Pipeline

## Overview
This repository contains a lightweight, high-performance Python ETL (Extract, Transform, Load) pipeline designed to ingest, clean, and standardize severely degraded database exports. Built entirely on vectorized `pandas` operations, it eliminates the computational overhead of standard iterative loops, ensuring scalability for large B2B datasets.

## The STAR Methodology

### **Situation**
Modern businesses generate massive volumes of transactional data, but manual entry errors, legacy system exports, and inconsistent formatting often render this data unusable for analytics. Analysts waste hours manually cleaning alphanumeric noise from financial columns, resolving null values, and parsing fragmented temporal data, leading to delayed reporting and increased operational friction.

### **Task**
The objective was to engineer a fully automated, fail-safe sanitization pipeline capable of processing unstructured CSV dumps into clean, downstream-ready payloads without manual intervention. The system needed to handle unpredictable entropy: floating currency symbols, broken date formats, and missing critical fields.

### **Action**
I developed a modular Python pipeline leveraging native `pandas` C-bindings for vectorized data coercion. The architecture executes the following deterministic phases:
*   **Vectorized Type Coercion:** Deploys regex pattern matching (`r'[^\d.-]'`) to strip alphanumeric noise from financial data and coerces unparseable anomalies to standardized `NaN` values.
*   **Temporal Standardization:** Harmonizes heterogeneous date formats into strict `datetime64[ns]` formats. 
*   **Text Normalization:** Applies lowercasing and whitespace stripping across all categorical vectors simultaneously.
*   **Null-Handling & Critical Path Filtering:** Drops rows lacking absolute mission-critical identifiers while executing domain-specific imputation for secondary fields.

### **Result**
The pipeline converts heavily corrupted datasets into 100% mathematically viable, standardized CSV outputs. By utilizing C-level vectorization rather than Python `for` loops, execution time is optimized for large-scale enterprise data. The resulting dataset guarantees accurate downstream machine learning ingestion, automated dashboard rendering, and reliable financial aggregations.
