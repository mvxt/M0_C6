from sys import platform
import unittest

from pexpect import replwrap

class TestSecuritySystem(unittest.TestCase):
    def assert_interactions(self, tests):
        for interaction in tests:
            output = self.child.run_command(interaction[0])
            self.assertEqual(interaction[1], output)

    def setUp(self):
        command = 'python'
        if platform == 'linux' or platform == 'darwin':
            command += '3'
        self.child = replwrap.REPLWrapper(f'{command} security_system.py', 'Input: ', None)

    def test_simple(self):
        """Tests simple scenario, each user checks in, checks out"""
        tests = [
            ('mhenderson in', '  mhenderson is checked in\r\n'),
            ('mhenderson out', '  mhenderson is checked out\r\n'),
            ('jjabrams in', '  jjabrams is checked in\r\n'),
            ('jjabrams out', '  jjabrams is checked out\r\n'),
            ('sbrown in', '  sbrown is checked in\r\n'),
            ('sbrown out', '  sbrown is checked out\r\n'),
            ('enterocc in', '  enterocc is checked in\r\n'),
            ('enterocc out', '  enterocc is checked out\r\n'),
            ('zzdawg in', '  zzdawg is checked in\r\n'),
            ('zzdawg out', '  zzdawg is checked out\r\n')
        ]
        self.assert_interactions(tests)

    def test_bad_user(self):
        """Tests logging in w/ a bad username"""
        tests = [
            ('elonmusk in', '  ALARM SOUNDED\r\n')
        ]
        self.assert_interactions(tests)

    def test_multi_login(self):
        """Tests logging in multiple times"""
        tests = [
            ('jjabrams in', '  jjabrams is checked in\r\n'),
            ('jjabrams in', '  ALARM SOUNDED\r\n')
        ]
        self.assert_interactions(tests)

    def test_multi_logout(self):
        """Tests logging out multiple times"""
        tests = [
            ('jjabrams in', '  jjabrams is checked in\r\n'),
            ('jjabrams out', '  jjabrams is checked out\r\n')
            ('jjabrams out', '  ALARM SOUNDED\r\n')
        ]
        self.assert_interactions(tests)

    def test_multi_logout(self):
        """Tests various gibberish commands"""
        tests = [
            ('blah blah hubba bubba', '  ALARM SOUNDED\r\n'),
            ('in in out', '  ALARM SOUNDED\r\n'),
            ('exit', '  ALARM SOUNDED\r\n'),
            ('abcdeja:LKEP#U (*Q Oo:UIO@:UFJIOF)(!*', '  ALARM SOUNDED\r\n')
        ]
        self.assert_interactions(tests)

if __name__ == '__main__':
    unittest.main()
