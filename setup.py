from setuptools import setup, find_packages

setup(
    name='jatto_compare_version_strings',
    version='0.0.1',
    url='https://github.com/jattoabdul/compare_version_strings',
    license='MIT',
    author='Aminujatto Abdulqahhar',
    author_email='jattoade@gmail.com',
    description='Compare version strings',
    long_description=open("README.md", "r").read(),
    packages=find_packages(exclude=['tests']),
    long_description_content_type="text/markdown",
    install_requires=[
        'pytest',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data=True,
    zip_safe=False
)
