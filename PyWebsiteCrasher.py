import webbrowser

url = '10.30.40.181/gv_shout/'
# Windows
count = 0
inputB = int(input("Num times to crash page: "))
inputA = input("yes to run: ")
go = False
if inputA == 'yes':
  go = True
while (go and count < inputB):
  webbrowser.open_new_tab("10.30.40.181/gv_shout/")
  count+=1
  