from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit_cld_upload_widget",
    version="0.1.0",
    author="Akshay Ranganath",
    author_email="akshay.ranganath@cloudinary.com",
    description="Streamlit component that allows you to embed Cloudinary's Uploader Widget",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=["streamlit>=1.2", "jinja2"],
)
