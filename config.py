import configparser

kcd = {
	"0":0x30,
	"1":0x31,
	"2":0x32,
	"3":0x33,
	"4":0x34,
	"5":0x35,
	"6":0x36,
	"7":0x37,
	"8":0x38,
	"9":0x39,
	"a":0x41,
	"b":0x42,
	"c":0x43,
	"d":0x44,
	"e":0x45,
	"f":0x46,
	"g":0x47,
	"h":0x48,
	"i":0x49,
	"j":0x4A,
	"k":0x4B,
	"l":0x4C,
	"m":0x4D,
	"n":0x4E,
	"o":0x4F,
	"p":0x50,
	"q":0x51,
	"r":0x52,
	"s":0x53,
	"t":0x54,
	"u":0x55,
	"v":0x56,
	"w":0x57,
	"x":0x58,
	"y":0x59,
	"z":0x5A,
	"s_":0x10,
	"c_":0x11,
	"a_":0x12,
	'__':0x20,
	'.':0xBE,
	',':0xBC,
	'-':0xBD,
	'=':0xBB,
	';':0xBA,
	'/':0xBF,
	'`':0xC0,
	'[':0xDB,
	'|':0xDC,
	']':0xDD,
	"'":0xDE,
	'n0':0x60,
	'n1':0x61,
	'n2':0x62,
	'n3':0x63,
	'n4':0x64,
	'n5':0x65,
	'n6':0x66,
	'n7':0x67,
	'n8':0x68,
	'n9':0x69,
	'n*':0x6A,
	'n+':0x6B,
	'n-':0x6D,
	'n.':0x6E,
	'n/':0x6F,
	'e_':0x0D
	}

file = 'config.ini'
config = configparser.ConfigParser()
config.read(file)

Keys = config['Keys']
k1t = Keys['k1'].lower()
k2t = Keys['k2'].lower()

k1c = kcd.get(k1t,0x01)
k2c = kcd.get(k2t,0x02)

Settings = config['Settings']
window_width = int(Settings['window_width'])
window_height = int(Settings['window_height'])
adaptive_button_size = int(Settings['adaptive_button_size'])
trail_length = float(Settings['trail_length'])
FPS = float(Settings['FPS'])
trail_speed = float(Settings['trail_speed'])
key1_position = float(Settings['key1_position'])
key2_position = float(Settings['key2_position'])

Colors = config['Colors']
c1_split = (Colors['button_color'].split(','))
color1 = []
for i in c1_split:
	color1.append(int(i))

c2_split = (Colors['trail_color'].split(','))
color2 = []
for i in c2_split:
	color2.append(int(i))

c3_split = (Colors['text_color'].split(','))
color3 = []
for i in c3_split:
	color3.append(int(i))

bc_split = (Colors['background_color'].split(','))
background_color = []
for i in bc_split:
	background_color.append(int(i))
