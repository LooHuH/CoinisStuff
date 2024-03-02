def askvar(varname, raw=False):
    while True:
        var = input(f'Enter var {varname} >>> ')
        if not raw:
            try:
                return int(var)
            except ValueError:
                pass
        else:
            return var
