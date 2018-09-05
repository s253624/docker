import os

os.system("docker build --build-arg http_proxy=http://172.16.7.55:8888 --build-arg https_proxy=http://172.16.7.55:8888 --rm -t sshd .")
