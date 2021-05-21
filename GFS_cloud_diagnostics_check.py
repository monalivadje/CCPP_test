import sys
sys.path.append(".")
import numpy as np
from cffi_GFS_cloud_diagnostics import GFS_cloud_diagnostics

nx = 1
ny = 2
nz = 3
con_pi = 3.14

variable_nparr = {}
variable_nparr["lat"] = np.ones((nx,ny), order='F') 
variable_nparr["de_lgth"] = np.ones((nx,ny), order='F')
variable_nparr["p_lay"] = np.asfortranarray(np.ones((nx,ny,nz))) 
variable_nparr["cld_frac"] = np.ones((nx,ny,nz), order="F")
variable_nparr["p_lev"] = np.ones((nx,ny,nz), order='F')
variable_nparr["deltaZ"] = np.ones((nx,ny,nz), order='F') 
variable_nparr["cloud_overlap_param"] = np.ones((nx,ny,nz), order='F')
variable_nparr["precip_overlap_param"] = np.ones((nx,ny,nz), order='F')
variable_nparr["errmsg"][] = ' '
for var_nm in ["mtopa", "mbota", "cldsa"]:
    variable_nparr[var_nm] = np.zeros((nx,ny,nz), order="F")
GFS_cloud_diagnostics(nx, ny, nz, con_pi, variable_nparr)
