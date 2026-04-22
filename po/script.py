import polib

for lang in ["en", "it"]:
    po_path = f"locale/{lang}/LC_MESSAGES/messages.po"
    mo_path = f"locale/{lang}/LC_MESSAGES/messages.mo"

    po = polib.pofile(po_path)
    po.save_as_mofile(mo_path)

print("Compiled .po to .mo")