import pathlib
import setuptools

setuptools.setup(
    name="enalsis",
    version="0.1.0",
    description="A simple and powerful text analysis package.",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    # url="github url"
    author="Tanay Dwivedi",
    author_email="tanaydwivedi2002@gmail.com",
    license="MIT",
    license_file="LICENSE",
    readme="README.md",
    # project_urls = {
    #     "Documentation": "docs url",
    #     "Source": "github url"
    # }
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
        "numpy",
        "pandas",
        "nltk",
    ],  # {will add the required dependencies or packages}
    packages=setuptools.find_packages(),
    include_package_data=True,
)
