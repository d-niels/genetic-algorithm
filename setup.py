
from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="ga",
    version="0.0.1",
    description="Genetic Algorithms",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/d-niels/ga",
    author="David Nielsen",
    author_email="d.niels1998@gmail.com",
    keywords="genetic",
    packages=['ga'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False
)
