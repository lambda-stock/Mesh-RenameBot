current_lang = "tr"
if current_lang == "tr":
    from .tr import TrTrans as Trans
else:
    ...
#def get_trans(title, lang = None) -> str:
#    if lang is None:
#        if current_lang == "en":
#            return getattr(EnTrans, title)
#    else:
#        if current_lang == "en":
#            return getattr(EnTrans, title)
