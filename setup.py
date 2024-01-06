from setuptools import setup

APP=['LoginAndRegister.py']
OPTIONS = {
    'argv-emulation': True,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)