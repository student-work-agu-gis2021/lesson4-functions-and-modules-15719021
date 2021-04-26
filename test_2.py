from Exercise_4_problem_2 import temp_classifier

def test_0():
	assert temp_classifier(16.5)==3

def test_1():
	assert temp_classifier(2)==2

def test_2():
	assert temp_classifier(-5)==0

def test_2():
	assert temp_classifier(11)==2
