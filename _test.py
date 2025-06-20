import pytest

#function to test square
def square(n):
    return n**2

#function to test cube
def cube(n):
    return n**3

#function to test fifth power
def fifth_power(n):
    return n**5

#Testing the square function
def test_square():
    assert square(2) == 4, "Test failed : Sqauare of 2 should be the 4"
    assert square(3) == 9, "Test failed : Sqauare of 3 should be the 9"

#Testing the cube function
def test_cube():
    assert cube(2) == 8, "Test failed : cube of 2 should be the 8"
    assert cube(3) == 27, "Test failed : cube of 3 should be 27" 

#Testing the fifth_power function
def test_fifth_power():
    assert fifth_power(2) == 32, "Test failed : fifth power of 2 should be 32"
    assert fifth_power(3) == 243, "Test failed : fifth power of 3 should be 243"       

#test for invalid input 
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")