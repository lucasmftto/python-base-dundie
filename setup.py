import os
from setuptools import setup, find_packages

def read(*paths):
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()
    
def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"', '-'))
    ]

setup(
    name='dundie',
    version='0.1.0',
    description="Reward Points System for Dunder Mifflin",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Lucas Favaretto, Bruno Rocha(LinuxTips)",
    python_requires=">=3.8",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__:main"
        ]
    },
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev": read_requirements("requirements.dev.txt"),
        "test": read_requirements("requirements.test.txt")
    }
)