# nephelaiio.acme-dnschallenge-cloudflare

[![Build Status](https://travis-ci.org/nephelaiio/ansible-role-acme-dnschallenge-cloudflare.svg?branch=master)](https://travis-ci.org/nephelaiio/ansible-role-acme-dnschallenge-cloudflare)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-nephelaiio.acme-dnschallenge-cloudflare-blue.svg)](https://galaxy.ansible.com/nephelaiio/acme-dnschallenge-cloudflare/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/acme-dnschallenge-cloudflare) to issue acme certificates with dns challenge verification using cloudflare's name service

## Role Variables
The most common user overridable parameters for the role are

|| required || variable || description || type || default ||
|| yes || acme_certificate_domain | the fqdn to generate an acme certificate for | string | "{{ ansible_fqdn }}" |
|| yes || acme_certificate_cf_account_email | cloudflare api user email | string | "{{ lookup('env', 'CF_ACCOUNT_EMAIL') }}" |
|| yes || acme_certificate_cf_account_token | cloudflare api user token | string | "{{ lookup('env', 'CF_ACCOUNT_TOKEN') }}" |
| no | acme_certificate_group_members | members to add to the owner group for certificate files | [string] | [] |
| no | acme_certificate_add_ca | add acme ca to the  | boolean | false |
| no | acme_certificate_caurl | url to ca certificate | string | https://letsencrypt.org/certs/isrgrootx1.pem.txt |
| no | acme_certificate_intcaurl | url to ca intermediate certificate | string | https://letsencrypt.org/certs/letsencryptauthorityx3.pem.txt |
| no | acme_certificate_directory | url to ca directory | string | https://acme-v01.api.letsencrypt.org/directory (letsencrypt production url) |
| no | acme_certificate_cafile (*) | define to create symlink to issuing ca cert file | string | __undefined_ |
| no | acme_certificate_intcafile (*) | define to create symlink to issuing intermediate ca cert file | string | _undefined_ |
| no | acme_certificate_certfile (*) | define to create symlink to cert file | string | _undefined_ |
| no | acme_certificate_chainfile (*) | define to create symlink to certificate chain file | string | _undefined_ |
| no | acme_certificate_keyfile (*) | define to create symlink to certificate key file | string | _undefined_ |

You can view an example redefinition of some of the above parameters, most notably the ones concerning certificate ca in the [CI test configuration file](/molecule/default/molecule.yml)

(*) useful for backwards compatibility with existing nginx/apache configurations

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
  roles:
    - role: nephelaiio.acme-dnschallenge-cloudflare

## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](/requirements.txt)

Role is tested against the following distributions (docker images):
  * Ubuntu Xenial
  * CentOS 7
  * Debian Stretch

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
