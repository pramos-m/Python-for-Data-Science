from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package',
    author='pramos-m',
    license="MIT",
    author_email='pramos-m@student.42barcelona.com',
    url='to update',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [],
    },
    python_requires=">=3.6",
)
