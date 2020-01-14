from setuptools import setup, find_packages


requirements = """
tensorflow
opencv-python
imutils
plotly
keras
"""
setup(name="obrazyMRI", install_requires=requirements,
	packages=find_packages())


