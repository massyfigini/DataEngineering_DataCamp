#######################
# Unit testing basics #
#######################

### Your first unit test using pytest

# Import the pytest package
import pytest

# Import the function convert_to_int()
from preprocessing_helpers import convert_to_int

# Complete the unit test name by adding a prefix
def test_on_string_with_one_comma():
  # Complete the assert statement
  assert convert_to_int("2,081") == 2081


### Spotting and fixing bugs

def convert_to_int(string_with_comma):
    # Fix this line so that it returns an int, not a str
    return int(string_with_comma.replace(",", ""))




#############################
# Intermediate unit testing #
#############################

### Write an informative test failure message

import pytest
from preprocessing_helpers import convert_to_int

def test_on_string_with_one_comma():
    test_argument = "2,081"
    expected = 2081
    actual = convert_to_int(test_argument)
    # Format the string with the actual return value
    message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(actual)
    # Write the assert statement which prints message on failure
    assert actual == expected, message


### Testing float return values

import numpy as np
import pytest
from as_numpy import get_data_as_numpy_array

def test_on_clean_file():
  expected = np.array([[2081.0, 314942.0],
                       [1059.0, 186606.0],
  					   [1148.0, 206186.0]
                       ]
                      )
  actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
  message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
  # Complete the assert statement
  assert actual == pytest.approx(expected), message


### Testing with multiple assert statements

def test_on_six_rows():
    example_argument = np.array([[2081.0, 314942.0], [1059.0, 186606.0],
                                 [1148.0, 206186.0], [1506.0, 248419.0],
                                 [1210.0, 214114.0], [1697.0, 277794.0]]
                                )
    # Fill in with training array's expected number of rows
    expected_training_array_num_rows = 4
    # Fill in with testing array's expected number of rows
    expected_testing_array_num_rows = 2
    actual = split_into_training_and_testing_sets(example_argument)
    # Write the assert statement checking training array's number of rows
    assert actual[0].shape[0] == expected_training_array_num_rows, "The actual number of rows in the training array is not {}".format(expected_training_array_num_rows)
    # Write the assert statement checking testing array's number of rows
    assert actual[1].shape[1] == 2, "The actual number of rows in the testing array is not {}".format(expected_testing_array_num_rows)


### Practice the context manager

import pytest

# Fill in with a context manager that will silence the ValueError
with pytest.raises(ValueError):
    raise ValueError

try:
    # Fill in with a context manager that raises Failed if no OSError is raised
    with pytest.raises(OSError):
        raise ValueError
except:
    print("pytest raised an exception because no OSError was raised in the context.")


### Unit test a ValueError

import numpy as np
import pytest
from train import split_into_training_and_testing_sets

def test_on_one_row():
    test_argument = np.array([[1382.0, 390167.0]])
    # Fill in with a context manager for checking ValueError
    with pytest.raises(ValueError):
      split_into_training_and_testing_sets(test_argument)

def test_on_one_row():
    test_argument = np.array([[1382.0, 390167.0]])
    # Store information about raised ValueError in exc_info
    with pytest.raises(ValueError) as exc_info:
      split_into_training_and_testing_sets(test_argument)
    expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
    # Check if the raised ValueError contains the correct message
    assert exc_info.match(expected_error_msg)


### Testing well: Boundary values

import pytest
from preprocessing_helpers import row_to_list

def test_on_no_tab_no_missing_value():    # (0, 0) boundary value
    # Assign actual to the return value for the argument "123\n"
    actual = row_to_list("123\n")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
    
def test_on_two_tabs_no_missing_value():    # (2, 0) boundary value
    actual = row_to_list("123\t4,567\t89\n")
    # Complete the assert statement
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
    
def test_on_one_tab_with_missing_value():    # (1, 1) boundary value
    actual = row_to_list("\t4,567\n")
    # Format the failure message
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


### Testing well: Values triggering special logic

import pytest
from preprocessing_helpers import row_to_list

def test_on_no_tab_with_missing_value():    # (0, 1) case
    # Assign to the actual return value for the argument "\n"
    actual = row_to_list("\n")
    # Write the assert statement with a failure message
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
    
def test_on_two_tabs_with_missing_value():    # (2, 1) case
    # Assign to the actual return value for the argument "123\t\t89\n"
    actual = row_to_list("123\t\t89\n")
    # Write the assert statement with a failure message
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


### Testing well: Normal arguments

import pytest
from preprocessing_helpers import row_to_list

def test_on_normal_argument_1():
    actual = row_to_list("123\t4,567\n")
    # Fill in with the expected return value for the argument "123\t4,567\n"
    expected = ["123", "4,567"]
    assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)
    
def test_on_normal_argument_2():
    actual = row_to_list("1,059\t186,606\n")
    expected = ["1,059", "186,606"]
    # Write the assert statement along with a failure message
    assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)


### TDD: Tests for normal arguments

def test_with_no_comma():
    actual = convert_to_int("756")
    # Complete the assert statement
    assert actual == 756, "Expected: 756, Actual: {0}".format(actual)
    
def test_with_one_comma():
    actual = convert_to_int("2,081")
    # Complete the assert statement
    assert actual == 2081, "Expected: 2081, Actual: {0}".format(actual)
    
def test_with_two_commas():
    actual = convert_to_int("1,034,891")
    # Complete the assert statement
    assert actual == 1034891, "Expected: 1034891, Actual: {0}".format(actual)


### TDD: Requirement collection

# Give a name to the test for an argument with missing comma
def test_on_string_with_missing_comma():
    actual = convert_to_int("178100,301")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
    
def test_on_string_with_incorrectly_placed_comma():
    # Assign to the actual return value for the argument "12,72,891"
    actual = convert_to_int("12,72,891")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
    
def test_on_float_valued_string():
    actual = convert_to_int("23,816.92")
    # Complete the assert statement
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


### TDD: Implement the function

def convert_to_int(integer_string_with_commas):
    comma_separated_parts = integer_string_with_commas.split(",")
    for i in range(len(comma_separated_parts)):
        # Write an if statement for checking missing commas
        if len(comma_separated_parts[i]) > 3:
            return None
        # Write the if statement for incorrectly placed commas
        if i != 0 and len(comma_separated_parts[i]) != 3:
            return None
    integer_string_without_commas = "".join(comma_separated_parts)
    try:
        return int(integer_string_without_commas)
    # Fill in with a ValueError
    except ValueError:
        return None




###################################
# Test Organization and Execution #
###################################

### Create a test class

import pytest
import numpy as np

from models.train import split_into_training_and_testing_sets

# Declare the test class
class TestSplitIntoTrainingAndTestingSets(object):
    # Fill in with the correct mandatory argument
    def test_on_one_row(self):
        test_argument = np.array([[1382.0, 390167.0]])
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)
        expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
        assert exc_info.match(expected_error_msg)


### Running test classes

import numpy as np

def split_into_training_and_testing_sets(data_array):
    dim = data_array.ndim
    if dim != 2:
        raise ValueError("Argument data_array must be two dimensional. Got {0} dimensional array instead!".format(dim))
    num_rows = data_array.shape[0]
    if num_rows < 2:
        raise ValueError("Argument data_array must have at least 2 rows, it actually has just {0}".format(num_rows))
    # Fill in with the correct float
    num_training = int(0.75 * data_array.shape[0])
    permuted_indices = np.random.permutation(data_array.shape[0])
    return data_array[permuted_indices[:num_training], :], data_array[permuted_indices[num_training:], :]


### Mark a test class as expected to fail

# Mark the whole test class as "expected to fail"
@pytest.mark.xfail
class TestModelTest(object):
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
        actual = model_test(test_input, 2.0, 1.0)
        message = "model_test({0}) should return {1}, but it actually returned {2}".format(test_input, expected, actual)
        assert actual == pytest.approx(expected), message
        
    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)

# Add a reason for the expected failure
@pytest.mark.xfail(reason="Using TDD, model_test() has not yet been implemented")
class TestModelTest(object):
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
        actual = model_test(test_input, 2.0, 1.0)
        message = "model_test({0}) should return {1}, but it actually returned {2}".format(test_input, expected, actual)
        assert actual == pytest.approx(expected), message
        
    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)


### Mark a test as conditionally skipped

# Import the sys module
import sys

class TestGetDataAsNumpyArray(object):
    # Mark as skipped if Python version is greater than 2.7
    @pytest.mark.skipif(sys.version_info > (2, 7))
    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0],
                             [1059.0, 186606.0],
                             [1148.0, 206186.0]
                             ]
                            )
        actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
        assert actual == pytest.approx(expected), message

class TestGetDataAsNumpyArray(object):
    # Add a reason for skipping the test
    @pytest.mark.skipif(sys.version_info > (2, 7), reason="Works only on Python 2.7 or lower")
    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0],
                             [1059.0, 186606.0],
                             [1148.0, 206186.0]
                             ]
                            )
        actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
        assert actual == pytest.approx(expected), message
