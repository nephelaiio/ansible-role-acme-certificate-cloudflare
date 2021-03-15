import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_chain(host):
    certdir = "/etc/letsencrypt/live"
    intcert = f"{certdir}/letsencrypt-stg-int-r3.pem"
    cacert = f"{certdir}/letsencrypt-stg-root-x1.pem"
    crtfile = f"{certdir}/*.nephelai.io.crt"
    cmd = f"openssl verify -CAfile {cacert} -untrusted {intcert} {crtfile}"
    assert host.run_test(cmd).rc == 0


def test_key(host):
    keydir = "/etc/letsencrypt/keys"
    cmd = f"openssl rsa -in {keydir}/*.nephelai.io"
    assert host.run_test(cmd).rc == 0


def test_symlinks(host):
    certdir = "/etc/letsencrypt/live"
    intcert = f"{certdir}/letsencrypt-stg-int-r3.pem"
    cacert = f"{certdir}/letsencrypt-stg-root-x1.pem"
    calink = "/tmp/cafile"
    intlink = "/tmp/intfile"
    crtlink = "/tmp/crtfile"
    assert host.file(intlink).exists
    assert host.file(intlink).is_symlink
    assert host.file(intlink).linked_to == intcert
    assert host.file(calink).exists
    assert host.file(calink).is_symlink
    assert host.file(calink).linked_to == cacert
    assert host.file(crtlink).exists
    assert host.file(crtlink).is_symlink


def test_chain_symlinks(host):
    certdir = "/tmp"
    intcert = f"{certdir}/intfile"
    cacert = f"{certdir}/cafile"
    crtfile = f"{certdir}/crtfile"
    cmd = f"openssl verify -CAfile {cacert} -untrusted {intcert} {crtfile}"
    assert host.run_test(cmd).rc == 0


def test_key_symlink(host):
    keydir = "/tmp"
    cmd = f"openssl rsa -in {keydir}/keyfile"
    assert host.run_test(cmd).rc == 0
