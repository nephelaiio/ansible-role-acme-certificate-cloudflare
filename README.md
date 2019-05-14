# nephelaiio.acme-dnschallenge-route53

[![Build Status](https://travis-ci.org/nephelaiio/ansible-role-acme-dnschallenge-route53.svg?branch=master)](https://travis-ci.org/nephelaiio/ansible-role-acme-dnschallenge-route53)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-nephelaiio.acme-dnschallenge-route53-blue.svg)](https://galaxy.ansible.com/nephelaiio/acme-dnschallenge-route53/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/acme-dnschallenge-route53) to issue acme certificates with dns challenge verification using route53 name service

## Role Variables

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Dependencies

By default this role does not depend on any external roles. If any such dependency is required please [add them](/meta/main.yml) according to [the documentation](http://docs.ansible.com/ansible/playbooks_roles.html#role-dependencies)

## Example Playbook

- hosts: servers
  roles:
     - role: nephelaiio.acme-dnschallenge-route53
       acme_dnschallenge_route53_package_state: latest


## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](/requirements.txt)

Role is tested against the following distributions (docker images):
  * Ubuntu Xenial
  * CentOS 7
  * Debian Stretch
  * Arch Linux

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
