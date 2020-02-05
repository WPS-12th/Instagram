#!/usr/bin/env python
import argparse
import os
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('mode', type=str, choices=['init', 'renew'])

USER = 'ubuntu'
HOST = '13.125.236.55'
TARGET = f'{USER}@{HOST}'
HOME = str(Path.home())
IDENTITY_FILE = os.path.join(HOME, '.ssh', 'wps12th.pem')
SOURCE = os.path.join(HOME, 'projects', 'fastcampus', '12th', 'instagram')
SECRETS_FILE = os.path.join(SOURCE, 'secrets.json')

DOCKER_OPTIONS = [
    ('--rm', ''),
    ('-it', ''),
    ('--name', 'certbot'),
    # Let's encrypt volumes
    ('-v', '/etc/letsencrypt:/etc/letsencrypt'),
    ('-v', '/var/lib/letsencrypt:/var/lib/letsencrypt'),
]


def run(cmd, ignore_error=False):
    process = subprocess.run(cmd, shell=True)
    if not ignore_error:
        process.check_returncode()


def ssh_run(cmd, tty=False, ignore_error=False):
    run(f"ssh {'-tt' if tty else ''} -o StrictHostKeyChecking=no -i {IDENTITY_FILE} {TARGET} -C {cmd}",
        ignore_error=ignore_error)


def cert_init():
    ssh_run('sudo docker run {options} certbot/certbot {cmd}'.format(
        options=' '.join([f'{key} {value}' for key, value in DOCKER_OPTIONS]),
        cmd="certonly -d 'wps.pby.kr' --manual",
    ), tty=True)


def cert_renew():
    ssh_run('sudo docker run {options} certbot/certbot {cmd}'.format(
        options=' '.join([f'{key} {value}' for key, value in DOCKER_OPTIONS]),
        cmd="renew",
    ), tty=True)


if __name__ == '__main__':
    args = parser.parse_args()
    try:
        if args.mode == 'init':
            cert_init()
        elif args.mode == 'renew':
            cert_renew()
    except subprocess.CalledProcessError as e:
        print('deploy-docker-secrets Error!')
        print(' cmd:', e.cmd)
        print(' returncode:', e.returncode)
        print(' output:', e.output)
        print(' stdout:', e.stdout)
        print(' stderr:', e.stderr)
