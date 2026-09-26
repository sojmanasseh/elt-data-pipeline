import pandas as pd
import numpy as np


def generate_corrupted_data(filepath="raw_transactions.csv"):
    np.random.seed(42)  # Deterministic generation for reproducibility

    data = {
        "transaction_id": [f"TXN-{i:04d}" for i in range(1, 16)],
        "purchase_date": [
            "2023-01-15", "01/16/2023", "Jan 17th 2023", "2023.01.18",
            np.nan, "2023-01-20", "invalid_date", "12-31-2022",
            "2023/02/01", "02-02-23", "2023-02-05 14:30:00",
            "March 1st, 2023", np.nan, "2023-04-10", "15-04-2023"
        ],
        "revenue": [
            "$1,250.50", "USD 500", " 450.00 ", "invalid", "1,000",
            np.nan, "$890.99", "750..00", "EUR 600", "99.99",
            "1,200.50", "$ 340.00", "NaN", " 800.00 ", "1500"
        ],
        "customer_email": [
            "john@example.com", "JANE@EXAMPLE.COM", "bob.smith@domain",
            "alice@domain.com", np.nan, "charlie@web.org", "david@web",
            "eve@domain.com", "frank@web.org", "grace@domain.com",
            "henry@domain.com", " IVY@WEB.ORG ", np.nan, "jack@domain.com", "kyle.example.com"
        ],
        "status": [
            "Completed", "completed ", "Pending", "  Failed", "Completed",
            "Canceled", "Completed", np.nan, "pending", "COMPLETED",
            "Failed", "  completed", "Pending", "CANCELED", "Completed"
        ]
    }

    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
    print(f"[System] Corrupted dataset generated: {filepath}")


if __name__ == "__main__":
    generate_corrupted_data()