import requests
import pytest
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Define the base URL for the FastAPI application.
BASE_URL = "http://localhost:8000"

# Load the credit card fraud dataset
# Ensure the dataset path is correct and accessible
dataset_path = "/Users/jonathandyer/Documents/Dyer Innovation/data/credit_card_transaction_data_labeled.csv"
df = pd.read_csv(dataset_path)

# Select a sample row for testing
# Exclude the 'Class' column, which is the label
sample_row = df.drop(columns=['Class']).iloc[0]

# Standardize the numeric features using the same scaler settings as the model
scaler = StandardScaler()
scaler.fit(df.drop(columns=['Class']))  # Fit the scaler with the DataFrame, keeping feature names

# Convert the sample row to a DataFrame to retain feature names
sample_df = pd.DataFrame([sample_row])
print(f'Sample Row: {sample_row}')

# Transform the sample row using the fitted scaler
sample_scaled = scaler.transform(sample_df)

# Create a DataFrame with the expected column names
columns = df.drop(columns=['Class']).columns.tolist()  # Get the feature names
sample_scaled_df = pd.DataFrame(sample_scaled, columns=columns)

sample_scaled_list = sample_scaled_df.iloc[0].tolist()

# Define a fixture for sample input data.
@pytest.fixture
def sample_input():
    return {'features': sample_scaled_list}

# Test the /predict/ endpoint of the FastAPI application.
def test_predict(sample_input):
    print(f'Sample Input: {sample_input}')
    response = requests.post(f"{BASE_URL}/predict/", json=sample_input)
    assert response.status_code == 200
    assert "prediction" in response.json()
    prediction = response.json()["prediction"]
    assert isinstance(prediction, (int, float))  # Ensure the prediction is a number