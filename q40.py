fc = 0
sc = 0
d = {'INFO' : 'Connection successful','ERROR' : 'Timeout','INFO':'Retry'}
# try:
#     f = open('yamu.txt','r')
# except FileNotFoundError:
#     msg = "file doesn't supporting reading"
# if msg == "file doesn't supporting reading":
#     sc = sc + 1
# else:
#     fc = fc + 1
v = d.values()
print(v)
s = ['Connection successful','Retry']
f = ['Timeout','Invalid']
for i in v:
    if i in s:
        sc = sc + 1
    else:
        fc = fc + 1
print(f"Succes count is : {sc}")
print(f"Failure count is : {fc}")