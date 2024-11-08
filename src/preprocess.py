import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Load dataset from CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean dataset by handling missing values and dropping irrelevant columns."""
    df.dropna(inplace=True)
    df.drop(['transaction_id'], axis=1, inplace=True)  # Drop ID column if not useful for modeling
    return df

def feature_engineering(df):
    """Create new features like transaction frequency or average transaction amount."""
    df['transaction_hour'] = pd.to_datetime(df['transaction_time']).dt.hour
    return df

def scale_features(df, columns):
    """Scale numerical features for model compatibility."""
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df