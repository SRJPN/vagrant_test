import subprocess
import unittest

class TestVagrantBoxes(unittest.TestCase):

    def _remote_exec(self, command):
        remote_exec_command = ['ssh', '-t', 'vagrant@127.0.0.1', '-p', port, '-i', '.vagrant/machines/default/virtualbox/private_key', command]
        return subprocess.check_output(remote_exec_command).strip().split('\n')

    def test_os_version(self):
        actual_release = self._remote_exec('cat /etc/redhat-release')[0].strip()
        expected_release = 'CentOS release 6.7 (Final)'
        self.assertEqual(actual_release, expected_release, "\nExpected release: %s\nActual Release: %s" % (expected_release, actual_release) )

if __name__ == '__main__':
    port = '2200'
    unittest.main()