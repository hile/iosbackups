"""
Common databases in iOS backups
"""

import os

from iosbackups import iOSBackupError
from systematic.sqlite import SQLiteDatabase, SQLiteError

DATABASE_FILES_MAP = {
    'sms':          '3d0d7e5fb2ce288813306e4d4636395e047a3d28',
    'calls':        '2b2b0084a1bc3a5ac8c27afdf14afb42c61a19ca',
    'contacts':     '31bb7ba8914766d4ba40d6dfb6113c8b614be442',
    'calendar':     '2041457d5fe04d39d0ab481178355df6781e6858',
    'notes':        'ca3bc056d4da0bbf88b5fb3be254f3b7147e639c',
    'locations':    '4096c9ec676f2847dc283405900e284a7c815836',
}

class iOSDatabase(SQLiteDatabase):
    """Parent class for iOS sqlite databases

    """
    def __init__(self, backup):
        try:
            filename = DATABASE_FILES_MAP[self.name]
        except KeyError:
            raise iOSBackupError('Unknown database: {0}'.format(self.name))

        path = os.path.join(backup.path, filename)
        if not os.path.isfile(path):
            raise iOSBackupError('No such file: {0}'.format(path))

        super(iOSDatabase, self).__init__(path)


class SMS(iOSDatabase):
    """SMS database

    """
    name = 'sms'
    def __init__(self, backup):
        super(SMS, self).__init__(backup)


class Contacts(iOSDatabase):
    """Contacts database

    """
    name = 'contacts'
    def __init__(self, backup):
        super(Contacts, self).__init__(backup)


class Calls(iOSDatabase):
    """Calls database

    """
    name = 'calls'
    def __init__(self, backup):
        super(Calls, self).__init__(backup)


class Calendar(iOSDatabase):
    """Calendar database

    """
    name = 'calendar'
    def __init__(self, backup):
        super(Calendar, self).__init__(backup)


class Notes(iOSDatabase):
    """Notes database

    """
    name = 'notes'
    def __init__(self, backup):
        super(Notes, self).__init__(backup)


class Locations(iOSDatabase):
    """Locations database

    """
    name = 'locations'
    def __init__(self, backup):
        super(Locations, self).__init__(backup)
