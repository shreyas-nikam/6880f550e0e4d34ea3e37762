import pytest
from definition_acc477d4013e403487a7e091afd733d2 import calculate_residual_risk

@pytest.mark.parametrize("inherent_risk, control_effectiveness, approach, expected", [
    ("High", "Effective", "Simple", "Low"),
    ("Medium", "Partially Effective", "Weighted", "Medium"),
    ("Low", "Ineffective", "Simple", "Low"),
    ("High", "Ineffective", "Weighted", "High"),
    ("Medium", "Effective", "Weighted", "Low"),
])
def test_calculate_residual_risk(inherent_risk, control_effectiveness, approach, expected):
    assert calculate_residual_risk(inherent_risk, control_effectiveness, approach) == expected
