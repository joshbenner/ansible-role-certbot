import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('clients')


def test_certbot_installed(host):
    file = host.file('/opt/certbot/certbot-auto')
    assert file.exists
    assert file.is_file
    assert file.user == 'root'
    assert file.mode == 0o755


def test_wrapper_installed(host):
    assert host.file('/usr/local/sbin/certbot').exists


def test_cron_configured(host):
    file = host.file('/etc/cron.d/ansible-certbot')
    assert file.exists
    assert file.is_file
    assert 'certbot-auto' in file.content_string


def test_cert_issued(host):
    file = host.file('/etc/certbot/live/mycert/cert.pem')
    assert file.exists
