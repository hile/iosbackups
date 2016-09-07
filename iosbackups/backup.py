"""
iOS device backup
"""

import os
import glob
import plistlib

from iosbackups import iOSBackupError
from iosbackups.databases import SMS, Calls, Contacts, Calendar, Notes, Locations

DEFAULT_PATH = os.path.expanduser('~/Library/Application Support/MobileSync/Backup/')


class DeviceInfo(dict):
    """Basic info

    Basic device info from Info.plist
    """
    def __init__(self, backup):
        self.backup = backup
        filename = '{0}/Info.plist'.format(backup.path)
        try:
            pl = plistlib.readPlist(filename)
        except Exception as e:
            raise iOSBackupError('Error opening {0}: {1}'.format(filename, e))

        self.update(
            device_name=pl['Device Name'],
            last_backup_date=pl['Last Backup Date'],
            imei=pl['IMEI'],
            serial_number=pl['Serial Number'],
            product_name=pl['Product Name'],
            product_type=pl['Product Type'],
            product_version=pl['Product Version'],
        )

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            pass


class iOSBackup(object):
    """iOS device backup

    This class is used to open the backup by path
    """
    def __init__(self, path):
        self.path = path.rstrip(os.sep)
        if not os.path.isdir(self.path):
            raise iOSBackupError('Not a directory: {0}'.format(self.path))

        self.info = DeviceInfo(self)
        self.sms = SMS(self)
        self.calls = Calls(self)
        self.contacts = Contacts(self)
        self.calendar = Calendar(self)
        self.notes = Notes(self)
        self.locations = Locations(self)

    def __cmp__(self, other):
        if isinstance(other, basestring):
            return cmp(self.info.device_name, other)

        if not isinstance(other, iOSBackup):
            raise TypeError

        for key in ( 'last_backup_date', 'device_name', 'product_type', 'serial_number', ):
            a = self.info[key]
            b = other.info[key]
            if a != b:
                return cmp(a, b)
        return 0


class MobileDeviceBackups(dict):
    """Loader for backups

    Loads backups from directory to iOSBackup objects
    """
    def __init__(self, path=DEFAULT_PATH):
        self.path = path
        if not os.path.isdir(self.path):
            raise iOSBackupError('Not a directory: {0}'.format(self.path))

    def load(self):
        """Load backups

        Load seemingly valid backups from directory
        """
        self.clear()
        for path in glob.glob('{0}/*/'.format(self.path)):
            if  os.path.isdir(path):
                try:
                    backup = iOSBackup(path)
                    self[backup.info.serial_number] = backup
                except iOSBackupError, emsg:
                    continue
