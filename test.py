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

    def test_cpus(self):
        actual_cpus = self._remote_exec('/usr/bin/nproc')[0].strip()
        expected_cpus = '1'
        self.assertEqual(actual_cpus, expected_cpus, "\nExpected cpus: %s\nActual cpus: %s" % (expected_cpus, actual_cpus) )

    def test_memory(self):
        actual_memory = int(self._remote_exec('cat /proc/meminfo | grep MemTotal')[0].replace('MemTotal:','').replace('kB','').strip())
        minimum_memory = 1887436
        maximum_memory = 2097152
        self.assertLess(actual_memory, maximum_memory, '\nMemory allocated greater than 2GB')
        self.assertGreater(actual_memory, minimum_memory,'\nMemory allocated lesser than 1.8GB')

if __name__ == '__main__':
    port = '2200'
    unittest.main()