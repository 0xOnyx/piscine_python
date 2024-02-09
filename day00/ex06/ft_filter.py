def ft_filter(iterable, function):
    if function is None:
        return [item for item in iterable if item]
    else:
        return [item for item in iterable if function(item)]
