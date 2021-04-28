
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ar-augment",
    version="1.0.0",
    author="Abdulshaheed Alqunber",
    author_email="abdulshaheedalqunber@gmail.com",
    license="MIT",
    description="Augment Arabic data for deep learning tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='arabic, arabic nlp, nlp',
    url="https://github.com/ashaheedq/ArAugment",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: Arabic',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'markovify', 'google_trans_new'
    ],

)