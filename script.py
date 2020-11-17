f = open("location.ini", "r")
content = f.read()
f.close()
lines = content.split("\n")


dict_bssid = {
}
dict_spaces = {
}
# dict.update({'AP45':'f40f1b3491ad'})
# print dict
# print dict
# print dict
	
for line in lines:
	if ":" in line:
		line_mac = line.split(":")
		
		ap = line_mac[0][6:10]
		bssid = line_mac[1][1:13]
		dict_bssid[bssid] = ap
		
	elif "_" in line:
		line_spaces = line.split(",")
		spaces_ap = line_spaces[0][11:15]
		spaces_space = line_spaces[1].replace(")", "").replace("'", "").replace("]", "").replace(" ", "")
		
		dict_spaces[spaces_ap] = spaces_space
	
		
# print dict_bssid
# print dict_spaces
z = 0

while z==0:
	user_bssid = raw_input("enter the bssid")
	temp = dict_bssid[user_bssid]
	print dict_spaces[temp]
	print "enter zero(0) if you want to search more bssid's else press 1"
	z = input()