from setuptools import setup, find_namespace_packages

setup(
    name="clean_folder",
    version=11.0,
    description="This is a sorter for files, it sorts files by folders and rename the folders according to the names of files",
    url="https://github.com/leegosx/hw_06/blob/main/sorter.py",
    author="Yan Bakhmat",
    author_email="yan.bakhmat@gmail.com",
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts':  [
            'clean-folder = clean_folder.clean:main',
        ],

    },
)
