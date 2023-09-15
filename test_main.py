"""
Test goes here

"""

from main import PDdescribe
import pandas as pd


def test_desc():
    """Function calling PDdescribe"""
    data = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]}
    
    # Call the function to be tested
    result = PDdescribe(data)
    
    # Define your expected output
    expected_output = pd.DataFrame({
        'A': [5.0, 3.0, 1.581139, 1.0, 2.0, 3.0, 4.0, 5.0],
        'B': [5.0, 30.0, 15.811388, 10.0, 20.0, 30.0, 40.0, 50.0]
    }, index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
    assert result.shape == (8, 2)