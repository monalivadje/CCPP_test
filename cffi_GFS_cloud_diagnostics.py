import numpy as np
# use cffi library - a C Foreign Function Interface for Python
from cffi import FFI
ffi = FFI()

# function creates cdata variables of a type "double *" from a numpy array
# additionally checks if the array is contiguous   
def as_pointer(numpy_array):
    assert numpy_array.flags['F_CONTIGUOUS'], \
        "array is not contiguous in memory (Fortran order)"
    return ffi.cast("double*", numpy_array.__array_interface__['data'][0])


# define a python function - binding a C function
def GFS_cloud_diagnostics(nx, ny, nz, con_pi, variable_nparr):
    # provide a signature for the C function
    ffi.cdef("void c_GFS_cloud_diagnostics(int nCol, int nLev , int lsswr, int lslwr, double const con_pi , double lat[], double de_lgth[], double p_lay[], double cld_frac[], double p_lev[], double deltaZ[], , double cloud_overlap_param[], double precip_overlap_param[], int errflg, char errmsg[], int mtopa[], int mbota[],double cldsa[]);", override=True)

    # load a library with the C function
    lib = ffi.dlopen('libGFS_cloud_diagnostics.so')

    # create cdata variables  for each numpy array 
    # the cdata variables will be passed to the C function and can be changed 
    variable_CFFI = {}
    for item in ["lat", "de_lgth", "p_lay","cld_frac", "p_lev", "deltaZ", "cloud_overlap_param", "precip_overlap_param", "errmsg", "mtopa", "mbota", "cldsa"]:
        variable_CFFI[item] = as_pointer(variable_nparr[item]) 

    # create additional variables that will be passed to the C function as values
    [:, :, :] = [1, nx] * 3
    [:, :, :] = [1, ny] * 3
    [:, :, :] = [1, nz] * 3

    # call the C function 
    lib.c_GFS_cloud_diagnostics( nCol, nLev, lsswr, lslwr, con_pi  variable_CFFI["lat"], variable_CFFI["de_lgth"], variable_CFFI["p_lay"], 
                  variable_CFFI["cld_frac"], variable_CFFI["p_lev"], variable_CFFI["deltaZ"], 
                  variable_CFFI["cloud_overlap_param"], variable_CFFI["precip_overlap_param"],errflag,variable_CFFI["errmsg"],variable_CFFI["mtopa"],
                  variable_CFFI["mbota"], variable_CFFI["cldsa"]
                  )
