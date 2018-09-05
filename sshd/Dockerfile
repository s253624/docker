FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y openssh-server

RUN echo 'root:root' | chpasswd

RUN mkdir /root/.ssh
RUN mkdir /var/run/sshd

COPY ./entry_point.sh /
RUN chmod +x /entry_point.sh

EXPOSE 22

#CMD ["/usr/sbin/sshd", "-D"]
ENTRYPOINT ["/entry_point.sh"]
