from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements.
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirement.txt','r')as file:
            ##Read lines from the files
            lines=file.readlines()
            ##process each lines
            for line in lines:
                requirement=line.strip()
                ##ignore the empty lines and -e .
                if requirement and requirement !='-e .':
                    requirement_lst.append(requirement)


    except FileNotFoundError:
        print("requirement.txt file not found")

    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Abhishek',
    author_email='ak42794673@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)