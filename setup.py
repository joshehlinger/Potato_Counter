import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='potato-counter',
    version="0.0.1",
    author="Joshua Ehlinger",
    install_requires=open('requirements.txt').read(),
    description='Counts potatoes',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshehlinger/potato_counter",
    py_modules=['counter'],
    entry_points={
        'console_scripts': [
            'potato-counter = counter:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
