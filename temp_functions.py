from Exercise_4_problem_1 import fahr_to_celsius

def test_48():
	assert round(fahr_to_celsius(48), 2)==8.89

def test_71():
	assert round(fahr_to_celsius(71), 2)==21.67

from Exercise_4_problem_2 import temp_classifier

def test_0():
	assert temp_classifier(16.5)==3

def test_1():
	assert temp_classifier(2)==2

def test_2():
	assert temp_classifier(-5)==0

def test_2():
	assert temp_classifier(11)==2