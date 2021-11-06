import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "oneNeuronSh"
USERNAME = "dshiv"

setuptools.setup(
    name=f"{PROJECT_NAME}-{USERNAME}",
    version="0.0.1",
    author=USERNAME,
    author_email="dshivendra88@gmail.com",
    description="its implementation of perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url= f"https://github.com/{USERNAME}/{PROJECT_NAME}",
    project_url= {
        "Bug Traker" : f"https://github.com/{USERNAME}/{PROJECT_NAME}/issues",
    },
    classifiers= [
        "Programming Language  :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent "
    ],
    package_dir={"", "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires = ">3.6",
    install_requires = [
        "numpy",
        "pandas",
        "joblib",
        "matplotlib",
    ]
)    