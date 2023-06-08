from setuptools import setup, find_packages

setup(
    name='dundie',
    version='0.1.0',
    description="Reward Points System for Dunder Mifflin",
    author="Lucas Favaretto, Bruno Rocha(LinuxTips)",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__:main"
        ]
    }
)