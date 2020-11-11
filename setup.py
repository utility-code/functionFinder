import setuptools

with open("lis.txt", "r") as f:
    lis = f.read()

setuptools.setup(name='functionvis',
                 version='0.1.3',
                 description='Visualize all functions and classes in a directory',
                 long_description=lis,
                 long_description_content_type="text/markdown",
                 url='https://github.com/SubhadityaMukherjee/functionFinder',
                 author='Subhaditya Mukherjee',
                 author_email='msubhaditya@gmail.com',
                 license="MIT",
                 packages=setuptools.find_packages(),
                 python_requires='>=3.6',
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ],
                 zip_safe=False)
