#William Thompson (wtt53)
#Tests for retirement functionality

from retirement import *
import pytest

def test_InvalidAgeTypeRaisesValueError():
	with pytest.raises(ValueError):
		retirement("string", 50000.00, 35.0, 1000000.00)

def test_InvalidSalaryTypeRaisesValueError():
	with pytest.raises(ValueError):
		retirement(50, "string", 35.0, 1000000.00)

def test_InvalidPercentTypeRaisesValueError():
	with pytest.raises(ValueError):
		retirement(50, 50000.00, "string", 1000000.00)

def test_InvalidGoalTypeRaisesValueError():
	with pytest.raises(ValueError):
		retirement(50, 50000.00, 35.0, "string")

def test_InvalidAgeValueRaisesValueError():
	with pytest.raises(ValueError):
		retirement(102, 50000.00, 35.0, 1000000.00)

def test_InvalidSalaryValueRaisesValueError():
	with pytest.raises(ValueError):
		retirement(50, -50.00, 35.0, 1000000.00)

def test_InvalidPercentValueRaisesValueError():
	with pytest.raises(ValueError):
		retirement(50, 50000.00, -5.0, 1000000.00)

def test_InvalidGoalValueRaisesValueError():
	with pytest.raises(ValueError):
		retirement(50, 50000.00, 35.0, -75.00)

def test_RetirementOutput():
	assert isinstance(retirement(50, 50000.00, 35.0, 1000000.00), str)