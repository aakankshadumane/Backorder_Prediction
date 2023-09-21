from setuptools import find_packages,setup

# This file is not run through terminal. 
# pip install -r requirements.txt is used to run requirements.txt file.
# requirements.txt file has -e . as last line. That triggers setup file
# to run automatically.
# .egg-info file will be created after installation of all modules.

HYPEN_E_DOT = "-e ."

def get_requirements(requirements_file:str):
    """
    This function will return list of requirements
    """
    # Empty List is created
    requirements = []
    with open(requirements_file, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        # While reading next line \n will get added at end of package
        # We are removing it so that only package name is extracted

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='backorder Prediction',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    author='Aakanksha Dumane',
    description='A machine learning project for Backorder Prediction',
    long_description='',
    url='https://github.com/aakankshadumane/Backorder_Prediction.git',
)
