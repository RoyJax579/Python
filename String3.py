#to replace a word from a string
msg = "Hello, Roynickson"

msg2 = msg.replace("Roynickson", "Sam")

print(msg2)
print(msg)

#to add variable directly into a sentence, we use f strings
greeting = "Hello"
name = "Roynickson"

msg = f"{greeting}, {name.upper()}. Welcome!"
print(msg)

