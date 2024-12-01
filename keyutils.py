from libqtile.config import Click, Drag,  Key


def parsekey(key):
    modifier_prefixes = {
        "m-": "mod4", "c-": "control", "s-": "shift", "m1-": "mod1",
        "m2-": "mod2", "m3-": "mod3", "m4-": "mod4",
    }
    mods = []
    while True:
        for prefix, value in modifier_prefixes.items():
            if key.startswith(prefix):
                mods.append(value)
                key = key.removeprefix(prefix)
                break
        else:
            break
    return mods, key


def key(key, action, desc):
    return Key(*parsekey(key), action, desc=desc)


def drag(key, action, start, **kwargs):
    return Drag(*parsekey(key), action, start=start, **kwargs)


def click(key, action, *args, **kwargs):
    return Click(*parsekey(key), action, *args, **kwargs)
