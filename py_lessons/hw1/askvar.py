def askvar(varname, num_barrier: list = None, len_barrier: list = None, raw=False):
    while True:
        var = input(f'Enter var {varname} >>> ')
        if len_barrier:
            if not (len_barrier[0] <= len(var) <= len_barrier[1]):
                continue
        if not raw:
            try:
                int_var = int(var)
                if num_barrier:
                    if num_barrier[0] <= int_var <= num_barrier[1]:
                        return int(var)
                else:
                    return int(var)
            except ValueError:
                try:
                    return float(var)
                except ValueError:
                    pass
        else:
            return var
