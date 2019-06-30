from Crypto.Cipher import AES
import GameDataParser
import os

with open("gamebin/GameData.bin", 'rb') as opened_gamedata:
    readable_gamedata = opened_gamedata.read()

game_key = b"\x1f\xda\xfb\x19\xc2\xc3\x7e\x41\xbe\x39\x4d\x1d\x4b\x85\x85\x1d"
game_iv = b"\xce\x76\x3b\xb1\x26\x87\xda\xf0\x55\x1b\xbc\x18\x2d\xe2\x9f\x39"
game_decryptor = AES.new(game_key, AES.MODE_CBC, game_iv)

game_data = game_decryptor.decrypt(readable_gamedata)

parser = GameDataParser.GameDataParser(game_data)
modules = parser.read_gamedata()
print(modules[0])