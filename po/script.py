import polib

# statico al momento
for lang in ["en", "it"]:
    po_path = f"po/locale/{lang}/LC_MESSAGES/messages.po"
    mo_path = f"po/locale/{lang}/LC_MESSAGES/messages.mo"

    po = polib.pofile(po_path)
    po.save_as_mofile(mo_path)

print("Compiled .po to .mo")