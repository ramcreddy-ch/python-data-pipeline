import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def run_etl():
    logging.info("Starting ETL process...")
    # Simulate loading data
    data = {
        'id': [1, 2, 3],
        'value': [10.5, 20.0, 15.5],
        'status': ['active', 'inactive', 'active']
    }
    df = pd.DataFrame(data)
    
    # Transformation: Filter active
    df_active = df[df['status'] == 'active']
    
    # Aggregation
    total_val = df_active['value'].sum()
    logging.info(f"ETL Complete. Total active value: {total_val}")
    return df_active

if __name__ == "__main__":
    run_etl()
