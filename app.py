import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Dashboard Configuration
st.set_page_config(page_title="Automated ETL Pipeline", layout="wide")
st.title("⚙️ Automated ETL Data Sanitization")
st.markdown("""
**Demonstration Asset | Python Data Specialist**  
This application visualizes the output of a custom vectorized pandas pipeline. 
It highlights the transformation of highly corrupted, non-standard database exports into mathematically viable payloads ready for downstream analytics.
""")


# 2. Data Ingestion (Cached for Performance)
@st.cache_data
def load_datasets():
    try:
        # Replace these filenames if yours differ
        raw = pd.read_csv("raw_transactions.csv")
        clean = pd.read_csv("clean_transactions.csv")
        return raw, clean
    except FileNotFoundError:
        st.error("System Error: CSV files not found. Execute backend pipeline first.")
        return pd.DataFrame(), pd.DataFrame()


raw_df, clean_df = load_datasets()

if not raw_df.empty and not clean_df.empty:
    st.divider()

    # 3. High-Level Aggregation Metrics
    st.subheader("Pipeline Telemetry")
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Raw Ingestion", f"{len(raw_df)} rows")
    col2.metric("Cleaned Output", f"{len(clean_df)} rows")
    col3.metric("Anomalies Filtered", f"{len(raw_df) - len(clean_df)} rows")

    total_revenue = clean_df['revenue'].sum()
    col4.metric("Verified Revenue", f"${total_revenue:,.2f}")

    st.divider()

    # 4. Interactive Data Comparison
    st.subheader("Data Entropy Resolution")
    tab1, tab2 = st.tabs(["✅ Sanitized Payload (Production Ready)", "⚠️ Raw Export (Corrupted)"])

    with tab1:
        st.dataframe(clean_df, use_container_width=True)
    with tab2:
        st.dataframe(raw_df, use_container_width=True)

    # 5. Downstream Visualization Proof
    st.subheader("Downstream Financial Aggregation")
    if len(clean_df) > 0:
        # Aggregate revenue by status
        rev_by_status = clean_df.groupby('status')['revenue'].sum().reset_index()

        # Matplotlib visualization
        fig, ax = plt.subplots(figsize=(10, 4))

        # Clean formatting
        ax.bar(rev_by_status['status'].str.title(), rev_by_status['revenue'], color='#2E86C1')
        ax.set_ylabel("Standardized Revenue (USD)")
        ax.set_title("Revenue Distribution by Transaction Status")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        st.pyplot(fig)
    else:
        st.warning("Insufficient valid data to generate downstream visualizations.")