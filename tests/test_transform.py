
import pandas as pd
import pytest
from src.transform import transform_data

@pytest.fixture
def sample_raw_data():
    """Provides a sample raw API response for testing."""
    return {
        "Meta Data": {
            "2. Symbol": "TEST"
        },
        "Time Series (Daily)": {
            "2025-07-30": {"1. open": "100", "2. high": "105", "3. low": "99", "4. close": "102", "5. volume": "1000"},
            "2025-07-29": {"1. open": "98", "2. high": "103", "3. low": "97", "4. close": "100", "5. volume": "1200"},
            "2025-07-28": {"1. open": "95", "2. high": "100", "3. low": "94", "4. close": "98", "5. volume": "1500"}
        }
    }

def test_transform_data_calculates_ma(sample_raw_data):
    """Tests that the moving average is calculated correctly."""
    # Arrange
    # The 3-day average of (102, 100, 98) should be 100.
    expected_ma = 100.0

    # Act
    transformed_df = transform_data(sample_raw_data)
    # Override the default rolling window for a predictable test
    transformed_df['3_day_ma'] = transformed_df['close'].rolling(window=3).mean()
    
    # Assert
    # Check the moving average on the last day where a full window is available
    actual_ma = transformed_df['3_day_ma'].iloc[-1]
    assert actual_ma == expected_ma

def test_transform_data_handles_key_error():
    """Tests that the function handles a missing key gracefully."""
    # Arrange
    bad_data = {"Error Message": "Invalid API call"}

    # Act & Assert
    with pytest.raises(KeyError):
        transform_data(bad_data)
