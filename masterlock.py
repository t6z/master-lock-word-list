import enchant

d = enchant.Dict("en-US")
f = open("words.txt","w")


dials = [['b','d','j','l','m','n','p','r','s','t'],
         ['a','e','i','o','u','y','r','t','l','h'],
         ['a','c','d','e','o','r','s','t','l','n'],
         ['e','d','h','k','y','r','s','t','l','n']
]

for letter0 in dials[0]:
   for letter1 in dials[1]:
      for letter2 in dials[2]:
         for letter3 in dials[3]:
            word = letter0 + letter1 + letter2 + letter3
            if d.check(word):
               f.write(word + "\n")

f.close()

print("Done!")

