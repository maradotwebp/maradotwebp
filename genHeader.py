letter = "|"
text = letter
r = 40

for i in range(r):
  text = letter + "</sup> " + text + " <sub>" + letter
for i in range(r):
  text = "<sup>" + text + "</sub>"

print(text)