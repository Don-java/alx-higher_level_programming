[12:18 AM, 1/4/2023] Fasusi Esther ALX: #!/usr/bin/python3
"""This defines a locked class"""


class LockedClass:
    """
    Only allows instatiation of an attribute called first_name
    """

    _slots_ = ["first_name"]
[12:18 AM, 1/4/2023] Fasusi Esther ALX: #!/usr/bin/python3
LockedClass = _import_('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e._class.name_, e))
