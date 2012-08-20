def cleanup_leftovers(site_manager):
    cleanup_registry(site_manager.adapters)
    cleanup_registry(site_manager.utilities)


def cleanup_registry(registry):
    adapters = registry._adapters
    for i in range(len(adapters)):
        cleanup_empty_adapters(adapters[i])
    subscribers = registry._subscribers
    for i in range(len(subscribers)):
        cleanup_empty_subscribers(subscribers[i])
    registry.p_changed = True


def cleanup_empty_adapters(map):
    keys = map.keys()
    for key in keys:
        sub = map[key]
        if type(sub) == dict:
            cleanup_empty_adapters(sub)
            if not sub:
                del map[key]


def cleanup_empty_subscribers(map):
    keys = map.keys()
    for key in keys:
        sub = map[key]
        if type(sub) == tuple:
            if not sub:
                del map[key]
        if type(sub) == dict:
            cleanup_empty_subscribers(sub)
            if not sub:
                del map[key]
