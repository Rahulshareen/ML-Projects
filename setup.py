from setuptools import find_packages,setup
from typing import List
hypen_e_dot = '-e .'
def get_requirements(file_path)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)


setup(
    name="mlprojects",
    version = '0.0.1',
    author = 'Rahul',
    author_email= 'rahulshareen@gmail.com',
    packages= find_packages(),
    install_reqires = get_requirements('requirements.txt')
)