import gettext, os

def setup_translation(lang):
    localedir = os.path.join(os.path.dirname(__file__), 'locale')
    translation = gettext.translation(
        'messages',
        localedir=localedir,
        languages=[lang],
        fallback=True
    )
    translation.install()
    return translation.gettext, translation.ngettext

# Change language here: "en" or "it"
_it, n_it = setup_translation("it")

print(_it("Welcome"))
print(_it("Hello, %s!") % "Marco")
print(n_it("You have %d message", "You have %d messages", 1) % 1)
print(n_it("You have %d message", "You have %d messages", 5) % 5)
print(_it("Save"))
print(_it("Settings"))