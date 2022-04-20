from setuptools import setup

setup(
    name='signature',
    version='0.1.0',
    py_modules=['signature'],
    install_requires=[
        #Работа с терминалом
        'Click',
        #Криптобиблиотека
        'pycryptodome'
    ],
    entry_points={
        'console_scripts': [
            'signature = signature:cli',
        ],
    },
)
