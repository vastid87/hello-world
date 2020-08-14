def substitute():  
  convert_code = {
      "a":"²", "b":"@", "c":"#", "d":"$", "e":"%", "f":"^", "g":"&", "h":"*",
      "i":"/", "j":">", "k":"<", "l":"~", "m":"◘", "n":"◙", "o":"♂", "p":"♀",
      "q":"☼", "r":"►", "s":"◄", "t":"↕", "u":"¶", "v":"§", "w":"∟", "x":"╛",
      "y":"├", "z":"┼", " ":"_", ",":"⌠", ".":"⌡", "'":"√", "?":"■", "!":"♣", '²': "a",
      "@": 'b', '#': 'c', '$': 'd', '%': 'e', '^': 'f', '&': 'g', '*': 'h',
      '/': 'i', '>': 'j', '<': 'k', '~': 'l', '◘': 'm', '◙': 'n', '♂': 'o',
      '♀': 'p', '☼': 'q', '►': 'r', '◄': 's', '↕': 't', '¶': 'u', '§': 'v',
      '∟': 'w', '╛': 'x', '├': 'y', '┼': 'z', '_': ' ', '⌠': ',', '⌡': '.',
      "√": "'", '■': '?', "♣":"!"
  }

  print("A simple letter/symbol substitution program.\nRight click to copy and paste (Ctrl+c will disrupt the program).\nYou can also type in your own text to convert it to symbols.")

  while True:
      user = input().lower()
      if user == "000":
        break
      list1 = []
      for letter in user:
        if letter in convert_code:
            list1.append(convert_code[letter])



      print(*list1, sep="")
