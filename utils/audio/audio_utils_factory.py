#!/usr/bin/env python3


class AudioUtilsFactory():

    def __init__(self, platform="osx"):
        self._platform = platform

    def get_audio_utils(self):
        if self._platform == "android":
            return self._get_android_audio_utils()
        else:
            return self._get_pc_audio_utils()

    def _get_pc_audio_utils(self):
        from utils.audio.pc_audio_utils import PcAudioUtils
        pc_audio_utils = PcAudioUtils()
        return pc_audio_utils

    def _get_android_audio_utils(self):
        from utils.audio.android_audio_utils import AndroidAudioUtils
        android_audio_utils = AndroidAudioUtils()
        return android_audio_utils
