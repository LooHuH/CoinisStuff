def find_num(mode: object, list_in: list):
    class Container:
        def __init__(self, num, i) -> None:
            self.num = num
            self.i = i
    max_num = mode(list_in)
    max_num_index = list_in.index(max_num)
    return Container(max_num, max_num_index)