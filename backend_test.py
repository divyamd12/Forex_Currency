import pytest
import os
import requests
import requests

BASE_URL = 'http://127.0.0.1:5000'


@pytest.fixture
def test_data2():
    return {
        'currency1': 'Australian dollar (AUD)',
        'currency2': 'Australian dollar (AUD)',
        'amount': "100",
    }

def test_get_amount(test_data2):
    response = requests.post(f'{BASE_URL}/get_amount', data=test_data2)
    assert response.status_code == 200

    # Additional assertions based on your specific requirements
    assert response.text is not None

@pytest.fixture
def test_data():
    return {
        'currency1': 'Australian dollar (AUD)',
        'currency2': 'Australian dollar (AUD)',
        'duration': 'Yearly',
        'startDate': '2012',
        'endDate': '2015',
    }

def test_get_plot(test_data):
    response = requests.post(f'{BASE_URL}/get_plot', data=test_data)
    assert response.status_code == 200

    # Check if the plot file is created
    assert os.path.exists("static/my_plot.png")

    # Additional assertions based on your specific requirements
    assert response.text is not None

    # Clean up: Remove the generated plot file
    os.remove("static/my_plot.png")
