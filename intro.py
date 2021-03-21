from helpers import colors


def print_intro():
    print(logo)
    print(intro)


primary_color = colors["magenta"]
code_color = colors["darkmagenta"]
link_color = colors["blue"]
off = colors["off"]

logo = f""" {primary_color}
 :::::::: :::::::::     :::  :::   ::: ::::::::  
:+:    :+::+:    :+:  :+: :+::+:   :+::+:    :+: 
      +:+ +:+    +:+ +:+   +:++:+ +:+ +:+        
    +#+   +#+    +:++#++:++#++:+#++:  +#++:++#++ 
  +#+     +#+    +#++#+     +#+ +#+          +#+ 
 #+#      #+#    #+##+#     #+# #+#   #+#    #+# 
################### ###     ### ###    ########  {off}"""  # Font: Alligator2

intro = f"""{primary_color}
   .+------+  +------+.
 .' |    .'|  |`.    | `
+---+--+'  |  |  `+--+---+
|   |  |   |  |   |  |   |
|  .+--+---+  +---+--+.  |
|.'    | .' you can use this command-line program to shortcut going to youtube for example and typing in the
+------+' search bar what you want, instead you can type what you want from the terminal {code_color}> 2days yt "foo bar"{primary_color}
+------+.  you can list commands {code_color}> 2days -list-commands {primary_color} and even add your own {code_color}> 2days -add-command  {primary_color}
|`.    | `. there are two kind of commands direct_link is to open a unique link and search_page is to open search 
|  `+--+---+ results page in the website that you gonna provide his query url  
|   |  |    | e.g (https://www.google.com/search?q=2days), {colors["red"]} Did you see any bug{primary_color} let us 
|   |  |    | catch it by opening an issue {primary_color} in the project repository
|   |  |    | on github {link_color} https://github.com/malikmouhiidine/2days/issues {primary_color}
|   |  |    | see { code_color } 2days --help { primary_color } for more options.
|   |  |    | and please contribute to the repository to make this program better or at least star it to make the
|   |  |    | contributors fell better about themselves.
|   |  |    | link to the repository: {link_color} https://github.com/malikmouhiidine/2days ❤︎ {primary_color}
|   |  |    | |   .  |  .
 +--+---+   | |  .   |  .
 `. |     `.| |.'    | .
   `+------+  +------+
   {off}"""

#
#
