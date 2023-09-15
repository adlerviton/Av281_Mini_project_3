"""
Test goes here

"""

from main import describe_with_polars
import polars as pl


def test_desc():
    """Function calling describe_with_polars"""
    
    # Call the function to be tested
    result = describe_with_polars('nba.csv')
    
    assert result.shape == (9, 10)
