
iOS backup utilities for python
===============================

This module detects iOS backups from OSX computers and can be used to fetch
some data like basic device information, SMS chats and so on.

All code is intended to use backups in read-only mode. Currently the script
just shows device info, and loads common databases with sqlite wrapper for
further processing.

Example usage
=============

This code is still so rough it's not yet in available with pip.

- Install with usual command

    python setup.py install

- List device info

    ios-backups list

API example
===========

Task: Get cursor for first iOSBackup object's SMS database, fetch raw messages.

    from iosbackups.backup import MobileDeviceBackups
    backups=MobileDeviceBackups()
    backups.load()
    cursor=backups[backups.keys()[0]].sms.cursor
    cursor.execute("""select * from message""")
    cursor.fetchall()

More to come. This will be abstracted and linked to contacts, don't worry!

TODO
====

Add code to the database classes to link and show SMS, contact, call etc. data
in some sensible way.

