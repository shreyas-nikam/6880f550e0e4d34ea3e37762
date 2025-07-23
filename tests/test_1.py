import pytest
from definition_423e54d422f4426c9da96e089ca45d16 import calculate_residual_risk

@pytest.mark.parametrize("inherent_risk, control_effectiveness, approach, expected", [
    ("High", "Effective", "Simple", "Low"),
    ("Medium", "Partially Effective", "Weighted", "Medium"),
    ("Low", "Ineffective", "Simple", "Low"),
    ("High", "Ineffective", "Weighted", "High"),
    ("Medium", "Effective", "Simple", "Low"),
])
def test_calculate_residual_risk(inherent_risk, control_effectiveness, approach, expected):
    assert calculate_residual_risk(inherent_risk, control_effectiveness, approach) == expected
