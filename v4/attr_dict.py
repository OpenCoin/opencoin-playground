class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

    def __getattr__(self, item):
        if item not in self:
            raise AttributeError(item)
        return self[item]


def to_attr_dict(dct):
    out = AttrDict()
    for k, v in sorted(dct.items()):
        out[k] = to_attr_dict(v) if isinstance(v, dict) else v
    return out