# nephelaiio.acme-dnschallenge-route53

[![Build Status](https://travis-ci.org/nephelaiio/ansible-role-acme-dnschallenge-route53.svg?branch=master)](https://travis-ci.org/nephelaiio/ansible-role-acme-dnschallenge-route53)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-nephelaiio.acme-dnschallenge-route53-blue.svg)](https://galaxy.ansible.com/nephelaiio/acme-dnschallenge-route53/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/acme-dnschallenge-route53) to issue acme certificates with dns challenge verification using route53 name service

## Role Variables

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Dependencies

* [[geerlingguy.repo-epel](https://github.com/geerlingguy/ansible-role-repo-epel)]
* [[nephelaiio.plugins](https://github.com/nephelaiio/ansible-role-plugins)]
* [[nephelaiio.pip](https://github.com/nephelaiio/ansible-role-pip)]

See the [requirements.yml](requirements) and [meta.yml](meta) files for more details

## Example Playbook

- hosts: servers
  vars:
    acme_certificate_email: ci@nephelai.io
    acme_certificate_domain: "{{ ansible_fqdn }}"
    acme_certificate_aws_accesskey_id: "{{ lookup('env', 'AWS_AK_ID') }}"
    acme_certificate_aws_accesskey_secret: "{{ lookup('env', 'AWS_AK_SECRET') }}"
  roles:
    - role: nephelaiio.acme-dnschallenge-route53

## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](/requirements.txt)

Role is tested against the following distributions (docker images):
  * Ubuntu Xenial
  * CentOS 7
  * Debian Stretch

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
