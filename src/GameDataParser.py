import struct

class GameDataParser:
    def __init__(self, game_data):
        self.game_data = game_data
        self.game_data_len = len(self.game_data)
        self.game_data_pos = 0

    def get_cur_data(self):
        return self.game_data[self.game_data_pos:]

    def read_gamedata(self):
        module_contents = []
        while (self.game_data_pos < self.game_data_len) and not self.game_data_pos + 16 > self.game_data_len:
            module_string = self.read_string()
            module_size = self.read_size()
            module_code = self.read_code(module_size)

            module_dict = {}
            module_dict['module_string'] = module_string
            module_dict['module_size'] = module_size
            module_dict['module_code'] = module_code
            module_contents.append(module_dict)
        return module_contents

    def read_string(self):
        module_string = []
        for letter in self.get_cur_data():
            if letter == 0:
                self.game_data_pos += 1
                break
            else:
                module_string.append(chr(letter))
                self.game_data_pos += 1
        return ''.join(module_string)

    def read_code(self, length):
        if length < 0:
            length = abs(length)
        code = self.get_cur_data()[:length]
        self.game_data_pos += length
        return code

    def read_size(self):
        size_bytes = self.get_cur_data()[:4]
        readable_size = struct.unpack('<i', size_bytes)
        self.game_data_pos += 4
        return readable_size[0]