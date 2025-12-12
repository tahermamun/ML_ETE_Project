from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Return a list of requirements from a requirements.txt file."""
    with open(file_path) as f:
        requirements = [line.strip() for line in f if line.strip()]
    return requirements

setup(
    name='ml_ete_project',
    version='0.0.1',
    description='Machine Learning ETE Project',
    author='Taher Mamun',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
