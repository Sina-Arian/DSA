'''15.Write your own dictionary class that implements the various operations ...'''


class Dict():
    def __init__(self, key, value):
        self.entry = ((key,value),)

    def add(self, key, value):
        lst_entry = list(self.entry)
        lst_entry.append((key,value))
        self.entry = tuple(lst_entry)

    def keys(self) -> list:
        keys = []
        for item in self.entry:
            keys.append(item[0])
        return keys

    def values(self) -> list:
        values = []
        for item in self.entry:
            values.append(item[1])
        return values
    
    def items(self) -> list:
        pairs = []
        for item in self.entry:
            pairs.append(item)
        return pairs
    
    def get(self, key, default):
        keys = tuple(self.keys())
        if key in keys:
            ind = keys.index(key)
            item = self.entry[ind]
            return item[1]
        
        else:
            self.add(key, default)
            return self.get(key, default)
    
    def clear(self):
        self.entry = ()
        return self.entry

    def __str__(self):
        out = []
        for item in self.entry:
            out.append(f'{item[0]} : {item[1]}')
        return '{' + ', '.join(out) + '}'