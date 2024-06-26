#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages

setup(
    name='DTLM',  # Replace with your package's name
    version='0.1.0',  # Your library's initial version
    description='Data transformation using large language models',  # Short description
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/DTL',  # URL to your repo
    license='MIT',  # Choose your license
    packages=find_packages(),
    install_requires=[
        # List all the dependencies here
        'openai==0.27.0', # For example, if you are using OpenAI's API
        'pandas',  # If your library depends on pandas
        'mistralai',# For mistral _update
        'ipywidgets',  # If you are using ipywidgets
        'tiktoken',
        'scikit-learn'
        # Add other dependencies as needed
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Development status
        'Intended Audience :: Data scientist,Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum version requirement of Python
)

