import setuptools


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="iClock",
    version="0.0.1",
    keywords="pyqt clock widget",
    author="odest",
    author_email="destrochloridium@gmail.com",
    description="Fully Customizable Clock Widget",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="GPLv3",
    url="https://github.com/odest/iClock",
    packages=setuptools.find_packages(),
    install_requires=[
        "PyQt5",
        "pillow",
        "darkdetect",
    ],
    extras_require = {
        'full': ['scipy', 'pillow', 'colorthief']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ],
    project_urls={
        'Source Code': 'https://github.com/odest/iClock'
    }
)
