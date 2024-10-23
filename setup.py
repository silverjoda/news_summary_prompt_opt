from setuptools import setup, find_packages

setup(
    name="news_summary_prompt_opt",
    version="0.1.0",
    description="A project for optimizing prompts",
    author="Teymur Azayev",
    author_email="heizen.sh@gmail.com",
    url="https://github.com/silverjoda/news_summary_prompt_opt",  # Replace with your project's URL
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here, e.g.:
        # 'numpy>=1.19.0',
        # 'pandas>=1.1.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
