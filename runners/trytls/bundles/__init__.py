import pkg_resources


def iter_bundles():
    for entry in pkg_resources.iter_entry_points("trytls.bundles"):
        yield entry.name


def load_bundle(name):
    for entry in pkg_resources.iter_entry_points("trytls.bundles", name):
        return entry.load()
    return None
