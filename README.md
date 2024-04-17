# streamlit_cld_upload_widget

Embed Cloudinary's [Upload Widget]() as a component in Streamlit application.

## Installation instructions 

```sh
pip install streamlit_cld_upload_widget
```

## Usage instructions

```python
import streamlit as st

from streamlit_cld_upload_widget import upload_widget

value = upload_widget(cloud_name="<<your cloudinary account name>>", upload_preset="<<your unsigned upload preset name")

st.write(value)
```

## Detailed Usage

Upload widget is the tool used for embedding Cloudinary's Upload Widget into your application. The widget has quite a few customization parameters. This python module exposes the following options:

| Parameter      | Purpose                                                                                                                                                            | Default Value                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| cloud_name     | This is your Cloudinary account name. To retrieve it, you may have to login to the Cloudinary's console and get the details from \`Programmable Media\` dashboard. | demo                                         |
| upload_preset  | The [_unsigned upload preset_]() to be used for the upload. If you would like to use signed uploads, this widget may not work for you. | None |
| sources        | An array of options listing the sources from where the files can be uploaded. | ['local', 'url'] |
| multiple       | Whether multiple files can be selected for upload | False | 
| max_files      | (If `multiple=True`), this option imposes limit on the maximum number of file that can be selected at once. | 1 |
| allowed_formats | Lists the file formats that are supported for upload. These are based on the file extensions. | ['webp', 'gif', 'jpg', 'png', 'mp4', 'mov'] | 
| show_powered_by | Boolean flag indicating whether Cloudinary branding should be shown on the Upload Widget. | True | 
| tags           | An array listing the set of tags to be applied to the image at upload. | [] | 
| context        | A string of the format `name=value|name1=value1` representing the context metadata values | None |


This repo is published on PyPi at: []().