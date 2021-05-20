module GFS_cloud_diagnostics_wrap

  ! using a module for interoperating with C 
  use iso_c_binding, only: c_int, c_double, c_char
  ! using an original Fortran module with a subroutine we want to use 
  use GFS_cloud_diagnostics 

  contains

  subroutine GFS_cloud_diagnostics_init()
  end subroutine GFS_cloud_diagnostics_init

  ! defining a C function - binding for Fortran function
  subroutine c_GFS_cloud_diagnostics_run(nCol, nLev , lsswr, lslwr, lat, de_lgth, p_lay,    &
       cld_frac, p_lev, deltaZ, cloud_overlap_param, precip_overlap_param, con_pi,       &
       mtopa, mbota, cldsa, errmsg, errflg
                      ) bind(c)
                
     implicit none           

    ! declaration of variables that will be passed as values 
    integer(c_int), intent(in), value :: nCol, nLev , lsswr, lslwr
    
    real(c_double), intent(in), value :: con_pi
                                        
    ! declaration arrays that will be passed as pointers
    real(c_double),  intent(in)       :: lat, de_lgth, p_lay,    &
       cld_frac, p_lev, deltaZ, cloud_overlap_param, precip_overlap_param
       
    ! variables that will be returned as values  
    integer(c_int), intent(out), value :: errflg
    
    ! arrays that will be returned as pointers
     character(c_char),  intent(out)    :: errmsg
    
     integer(c_int) ,  intent(out)      :: mtopa, mbota
      
      real(c_double) , intent(out)      :: cldsa
                                      

    ! calling the original Fortran function
    call GFS_cloud_diagnostics_run(nCol, nLev, lsswr, lslwr, lat, de_lgth, p_lay,    &
       cld_frac, p_lev, deltaZ, cloud_overlap_param, precip_overlap_param, con_pi,       &
       mtopa, mbota, cldsa, errmsg, errflg)
               

    end subroutine c_GFS_cloud_diagnostics_run
    
    subroutine GFS_cloud_diagnostics_finalize()
    end subroutine GFS_cloud_diagnostics_finalize
    
end module GFS_cloud_diagnostics_wrap
