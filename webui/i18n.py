from app.config import config
from app.utils import utils

import streamlit as st

LOCALES = utils.load_locales(utils.i18n_dir())


def tr(key):
    if "ui_language" not in st.session_state:
        st.session_state["ui_language"] = config.ui.get(
            "language", utils.get_system_locale()
        )
    loc = LOCALES.get(st.session_state["ui_language"], {})
    return loc.get("Translation", {}).get(key, key)
