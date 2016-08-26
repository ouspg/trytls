import pkg_resources


def iter_formatters():
    for entry in pkg_resources.iter_entry_points("trytls.formatters"):
        yield entry.name


def load_formatter(name):
    for entry in pkg_resources.iter_entry_points("trytls.formatters", name):
        return entry.load()
    return None
