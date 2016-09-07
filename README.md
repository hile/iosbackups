
iOS backup utilities for python
===============================

This module detects iOS backups from OSX computers and can be used to fetch
some data like basic device information, SMS chats and so on.

All code is intended to use backups in read-only mode. Currently the script
just shows device info, and loads common databases with sqlite wrapper for
further processing.

TODO
====

Add code to the database classes to link and show SMS, contact, call etc. data
in some sensible way.

