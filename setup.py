from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='jatto_compare_version_strings',
    version='0.0.1',
    url='https://github.com/jattoabdul/compare_version_strings',
    license='MIT',
    author='Aminujatto Abdulqahhar',
    author_email='jattoade@gmail.com',
    packages=find_packages(exclude=['tests']),
    description='Compare version strings',
    long_description=long_description,
    long_description_content_type="text/markdown",
    test_suite='nose.collector',
    tests_require=['nose'],
    setup_requires=[
       'setuptools>=41.0.1',
       'wheel>=0.33.4'
    ],
    include_package_data=True,
    zip_safe=False
)
