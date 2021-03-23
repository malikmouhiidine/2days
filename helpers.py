colors = {
    "white":    "\033[1;37m",
    "yellow":   "\033[1;33m",
    "green":    "\033[1;32m",
    "blue":     "\033[1;34m",
    "cyan":     "\033[1;36m",
    "red":      "\033[1;31m",
    "magenta":  "\033[1;35m",
    "black":    "\033[1;30m",
    "darkwhite":  "\033[0;37m",
    "darkyellow": "\033[0;33m",
    "darkgreen":  "\033[0;32m",
    "darkblue":   "\033[0;34m",
    "darkcyan":   "\033[0;36m",
    "darkred":    "\033[0;31m",
    "darkmagenta": "\033[0;35m",
    "darkblack":  "\033[0;30m",
    "off":        "\033[0;0m"
}

dictionaries_path = "C:\\Users\\malik\\OneDrive\\Desktop\\projects\\2days\\dictionaries.json"


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
