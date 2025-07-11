from default_api import browser_navigate, browser_view, browser_input, browser_click

def navigate(brief, intent, url):
    return browser_navigate(brief=brief, intent=intent, url=url)

def view(brief):
    return browser_view(brief=brief)

def input_text(brief, index, press_enter, text):
    return browser_input(brief=brief, index=index, press_enter=press_enter, text=text)

def click(brief, index):
    return browser_click(brief=brief, index=index)


