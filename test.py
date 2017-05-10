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

    def test_ip(self):
        matching_ip = False
        command_output = self._remote_exec('/sbin/ifconfig | grep inet | grep addr')
        for ifconfig_line in command_output:
            if static_ip in ifconfig_line:
                matching_ip = True
        self.assertTrue(matching_ip, "\nStatic IP: %s not found in test ip" % static_ip)

    def test_nfs_mount_present(self):
        mounted_folder = False
        mount_point = False
        command_output = self._remote_exec('df -h')
        for output_line in command_output:
            if 'vagrant_test' in output_line:
                mounted_folder = True
            if '/opt/data' in output_line:
                mount_point = True
        self.assertTrue(mount_point, "\nMount point is not /opt/data")
        self.assertTrue(mounted_folder, "\nvagrant_tests folder not mounted")

    def test_go_server_installed(self):
        go_server_installed = False
        command_output = self._remote_exec('sudo yum info go-server | grep Repo')[0]
        if 'installed' in command_output:
            go_server_installed = True
        self.assertTrue(go_server_installed, "\nGo server not installed")

if __name__ == '__main__':
    port = '2200'
    static_ip = '192.168.33.10'
    unittest.main()
