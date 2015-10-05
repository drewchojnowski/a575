import numpy as np
from astropy.io import ascii

def get_isochrone_struct(file,quantities):
    data=ascii.read(file)
    str={'z':data['col1'],'log_age':data['col2'],'m_ini':data['col3'],'m_act':data['col4'],
         'log_l':data['col5'],'log_t':data['col6'],'log_g':data['col7'],'mbol':data['col8'],
         'u':data['col9'],'b':data['col10'],'v':data['col11'],'r':data['col12'],'i':data['col13'],
         'j':data['col14'],'h':data['col15'],'k':data['col16'],'int_imf_stage':data['col17']}

    print quantities

    return str

