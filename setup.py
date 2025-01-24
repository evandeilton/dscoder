from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="dscoder",
    version="0.1.1",
    author="José Lopes",
    author_email="evandeilton@example.com",
    description="dscoder - AI Code Generation Agent For Data Science Programming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/evandeilton/dscoder",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "dscoder=agent:main",
        ],
    },
)
