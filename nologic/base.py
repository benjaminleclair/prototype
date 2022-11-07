
def state_selector(_state, func_list):
    
    def _match(_fs, _s):
        for i in _fs:
            if i[0] == _s:
                return i[1]
    
    fs = map(lambda f: f(), func_list)
    f = _match(fs, _state)
    return f
    
