import unittest
import passwordChecker


class TestPasswordChecker(unittest.TestCase):
    def test_checkpassword_missing_number(self):
        '''Should check for number'''
        test_missing_number_params = 'sDnded@_'

        result = passwordChecker.checkPassword(
            test_missing_number_params, test_missing_number_params)
        self.assertEqual(result, False)

    def test_checkpassword_checkDoNotMatch(self):
        '''Should check if both password do not match'''

        test_params = 'sDnded@_8'
        test_params_conf = 'sDn8ded@_'

        result = passwordChecker.checkPassword(test_params, test_params_conf)
        self.assertEqual(result, False)

    def test_checkpassword_incorect_length(self):
        '''Should check if password lenght ic correct'''

        test_incorect_length_params = 'sDnde4@'

        result = passwordChecker.checkPassword(
            test_incorect_length_params, test_incorect_length_params)
        self.assertEqual(result, False)

    def test_checkpassword_missing_upperCase(self):
        '''Should check if password is missing uppercase'''

        test_missing_upperCase_params = 'sdnde4@_'

        result = passwordChecker.checkPassword(
            test_missing_upperCase_params, test_missing_upperCase_params)
        self.assertEqual(result, False)


unittest.main()
