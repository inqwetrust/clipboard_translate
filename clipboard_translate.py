import subprocess
from subprocess import Popen, PIPE
# import commands
import clipboard
import os
from translate import Translator

text = ''
while True:

    if text != clipboard.paste() and len(clipboard.paste()) > 0:
        print(clipboard.paste())
        text = clipboard.paste()
        translator = Translator(to_lang="zh-TW")
        translation = Translator.translate(translator, str(text))
        print(translation)
        text = str(translation).replace('&gt;', '>')
        clipboard.copy(str(translation).replace('&gt;', '>'))
