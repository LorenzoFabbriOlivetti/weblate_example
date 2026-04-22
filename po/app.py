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
_it, n_it = setup_translation("en")

print(_it("Benvenuto"))
print(_it("Ciao, %s!") % "Marco")
print(n_it("Hai %d messaggio", "Hai %d messaggi", 1) % 1)
print(n_it("Hai %d messaggio", "Hai %d messaggi", 5) % 5)
print(_it("Salva"))
print(_it("Impostazioni"))