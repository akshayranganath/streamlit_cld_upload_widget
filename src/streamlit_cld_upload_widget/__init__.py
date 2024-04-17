from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called upload_widget,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"upload_widget", path=str(frontend_dir)
)

# Create the python function that will be called
def upload_widget(
    cloud_name:str,
    upload_preset:str,
    sources: Optional[list] = ['local', 'url'],
    multiple: Optional[bool] = False,
    max_files: Optional[int] = 1,
    tags: Optional[list] = [],
    context: Optional[str] = None,
    allowed_formats: Optional[list] = ['webp', 'gif', 'jpg', 'png', 'mp4', 'mov'],
    show_powered_by: Optional[bool] = True,
    key: Optional[str] = None
)->dict:
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        cloudName = cloud_name,
        uploadPreset = upload_preset,
        sources = sources,
        multiple = multiple,
        maxFiles = max_files,
        tags = tags,
        context = context,
        allowedFormats = allowed_formats,
        showPoweredBy = show_powered_by,
        key = key
    )

    return component_value


def main():
    st.write("## Example")
    value = upload_widget(
        'dbmataac4',
        'upload-widget',
        show_powered_by=False
    )

    st.write(value)


if __name__ == "__main__":
    main()
