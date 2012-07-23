def cleanup(registry):
    ad = registry._adapters
    for i in range(len(ad)):
        cleanup_empty_adapters(ad[i])


def cleanup_empty_adapters(map):
    keys = map.keys()
    for key in keys:
        sub = map[key]
        #if type(sub) == type((,)):
        #    if not sub:
        #        del map[key]
        if type(sub) == type({}):
            cleanup_empty_adapters(sub)
            if not sub:
                del map[key]
