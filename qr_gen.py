import pyqrcode
import sys

#Global configuration, you can channge it if you need...
Directory = ".//QRCode_Dir//"

#Called function, looping the URL, and change it into QR code format, and store into the QRCode_Dir directory, no return
def Url_To_QR(filename):
	f = open("url_list.txt","r")
	index = 0
	for line in f.readlines():
		cur_url = line.split("\n")[0]
		url = pyqrcode.create(cur_url)
		url.png('%surl_%d.png'%(Directory,index), scale=8)
		print("Printing QR code")
		print(url.terminal())
		index = index + 1

#Main function, just for call the core function, and perform the excception handling.
if __name__=='__main__':
	try:
		your_file = sys.argv[1]
		Url_To_QR(your_file)
		if(len(sys.argv)>2):
			raise Exception("Too many input...,you just need to input one URL list")
	except Exception as error:
		print("[!] Error occur, reason : %s"%error)
		print("[!] please input your file, let me show you...\npython qr_gen.py <your file name>")