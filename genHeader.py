parts = "|".split(" ")

text = parts[0]

r = 40

for i in range(r):
  prev = parts[(1 - i) % len(parts)]
  next = parts[(3 + i) % len(parts)]
  text = prev + "</sup> " + text + " <sub>" + next
for i in range(r):
  text = "<sup>" + text + "</sub>"

print(text)