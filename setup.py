import pathlib
import setuptools

setuptools.setup(
    name="enalsis",
    version="0.1.0",
    description="A simple and powerful text analysis package.",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/Tanay-Dwivedi/English-pip-Package",
    author="Tanay Dwivedi",
    author_email="tanaydwivedi2002@gmail.com",
    license="MIT",
    license_file="LICENSE",
    readme="README.md",
    project_urls={
        "Documentation": "https://github.com/Tanay-Dwivedi/English-pip-Package/blob/master/README.md",
        "Source": "https://github.com/Tanay-Dwivedi/English-pip-Package",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
    ],
    python_requires=">= 3.12",
    install_requires=[
        "spacy",
        "textblob",
        "py3langid",
    ],  # {will add the required dependencies or packages}
    packages=setuptools.find_packages(),
    include_package_data=True,
)
