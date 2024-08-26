import colorama


def print_meta(print_str):
    return print_custom("***%s***" % print_str, color=colorama.Fore.YELLOW, prompt=prompt)

def print_warn(print_str, prompt=False):
    return print_custom("[WARN:  %s]" % print_str, color=colorama.Fore.MAGENTA, prompt=prompt)

def print_err(print_str, prompt=False):
    return print_custom("[ERR:   %s]" % print_str, color=colorama.Fore.RED, prompt=prompt)

def print_debug(print_str, prompt=False):
    return print_custom("[DEBUG: %s]" % print_str, color=colorama.Fore.CYAN, prompt=prompt)

def print_temp(print_str, prompt=False):
    return print_custom("[TEMP:  %s]" % print_str, color=colorama.Fore.BLUE, prompt=prompt)

def print_prompt(print_str, color=colorama.Fore.GREEN):
    return print_custom(print_str, color=color, prompt=True)

def print_custom(print_str, color, style=colorama.Style.BRIGHT, prompt=False):
    """Must specify color like "colorama.Fore.CYAN"
    """
    print(color + style, end="")
    if prompt:
        print(print_str)
        return input("> " + colorama.Style.RESET_ALL)
    else:
        print(print_str + colorama.Style.RESET_ALL)
        return None

