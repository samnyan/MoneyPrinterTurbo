from app.models.schema import VideoAspect, VideoTransitionMode
from webui.i18n import tr

SUPPORT_LOCALES = [
    "zh-CN",
    "zh-HK",
    "zh-TW",
    "de-DE",
    "en-US",
    "fr-FR",
    "vi-VN",
    "th-TH",
]

# Select options

VIDEO_SOURCES = {
    "pexels": tr("Pexels"),
    "pixabay": tr("Pixabay"),
    "local": tr("Local file"),
    "douyin": tr("TikTok"),
    "bilibili": tr("Bilibili"),
    "xiaohongshu": tr("Xiaohongshu"),
}

VIDEO_LANGUAGES = {
    "": tr("Auto Detect"),
    **{value: value for _, value in enumerate(SUPPORT_LOCALES)},
}

VIDEO_CONCAT_MODES = {
    "sequential": tr("Sequential"),
    "random": tr("Random"),
}


# 视频转场模式
VIDEO_TRANSITION_MODES = {
    VideoTransitionMode.none.value: tr("None"),
    VideoTransitionMode.shuffle.value: tr("Shuffle"),
    VideoTransitionMode.fade_in.value: tr("FadeIn"),
    VideoTransitionMode.fade_out.value: tr("FadeOut"),
    VideoTransitionMode.slide_in.value: tr("SlideIn"),
    VideoTransitionMode.slide_out.value: tr("SlideOut"),
}

VIDEO_ASPECT_RATIOS = {
    VideoAspect.portrait.value: tr("Portrait"),
    VideoAspect.landscape.value: tr("Landscape"),
}

BGM_OPTIONS = {
    "": tr("No Background Music"),
    "random": tr("Random Background Music"),
    "custom": tr("Custom Background Music"),
}

SUBTITLE_POSITIONS = {
    "top": tr("Top"),
    "center": tr("Center"),
    "bottom": tr("Bottom"),
    "custom": tr("Custom"),
}
