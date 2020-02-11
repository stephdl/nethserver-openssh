==================
nethserver-openssh
==================

OpenSSH is the premier connectivity tool for remote login with the SSH protocol. 
It encrypts all traffic to eliminate eavesdropping, connection hijacking, and other attacks. 
In addition, OpenSSH provides a large suite of secure tunneling capabilities, 
several authentication methods, and sophisticated configuration options.

The OpenSSH suite consists of the following tools:

- Remote operations are done using ssh, scp, and sftp.
- Key management with ssh-add, ssh-keysign, ssh-keyscan, and ssh-keygen.
- The service side consists of sshd, sftp-server, and ssh-agent. 
   

Properties
==========

the props of the service to configure openssh:

::

 sshd=service
    AllowGroups=group1,group2:sftp,group3
    LoginGraceTime=2m
    MaxAuthTries=6
    PasswordAuthentication=yes
    PermitRootLogin=yes
    Protocol=2
    SubsystemSftp=yes
    TCPPort=22
    UsePAM=yes
    access=green,red
    status=enabled


The prop ``AllowGroups`` is used by the service only if the property ``$sssd{'ShellOverrideStatus'}`` is enabled.

- ``AllowGroups``: a comma separated list of group allowed to connect to the sshd service, if the option ``:sftp`` is specified then the group is restricted to SFTP
- ``SubsystemSftp``: (yes|no) enable the sftp service
- ``LoginGraceTime``: The time after which the server disconnects if the user has not successfully logged in.
- ``MaxAuthTries``: Specifies the maximum number of authentication attempts permitted per connection. 
  Once the number of failures reaches half this value, additional failures are logged.
- ``PasswordAuthentication``: (yes,no) Specifies whether password authentication is allowed.
- ``PermitRootLogin``: (yes,no) Specifies whether root can log in using ssh.
- ``TCPPort``: Use this TCP port to use sshd
- ``UsePAM``: (yes,no) Pam can be used to authentify user
- ``access``: Allow ssh connection to your firewall following different zones.
- ``status``: (enabled,disabled) Enable or disable the sshd service

Events
======

Two events takes care to expand and restart the service

``nethserver-openssh-update`` (sshd is restarted)
``nethserver-openssh-save`` (sshd is reloaded)
