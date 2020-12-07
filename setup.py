import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kangaroo-leozz37",
    version="0.0.1",
    author="Leonardo Lima",
    author_email="leonardoaugusto287@gmail.com",
    description="User-friendly lib for sockets in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leozz37/kangaroo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
