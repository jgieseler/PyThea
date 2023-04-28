from .version import version as __version__
import streamlit.web.bootstrap
from astropy.utils.data import get_pkg_data_filename

# get full path to PyThea_app.py
fullpath = get_pkg_data_filename('PyThea_app.py', package='PyThea')

# execute streamlit app
# run ?streamlit.web.bootstrap.run to get info on the options
streamlit.web.bootstrap.run(fullpath, '', [], [])
