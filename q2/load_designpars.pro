function load_designpars,targetdir,name,locst,desst

;============================================================================================
; this function is used to convert design pars header values to a structure
; written by Drew Chojnowski, 07/2015
;============================================================================================

dparsfile = targetdir+'/fields/'+name+'_loc00'+locst+'/des'+desst+'/apTS_designpars_'+name+'-00'+desst+'.par'
test=FILE_TEST(dparsfile) & if test eq 0 then stop,'designpars file not found for '+name+', design '+desst

tmp=YANNY_READONE(dparsfile,/ANON,HDR=hdr)

dpars=REPLICATE({fieldname:'none', racen:!VALUES.D_NAN, deccen:!VALUES.D_NAN, designid:0L, locationid:0L, $
		 plateid:0L, design_type:'none', design_driver:'none', comments:'none', radius:!VALUES.F_NAN, $
		 short_ver:-1, med_ver:-1, long_ver:-1, n_visits:-1, n_tellfib:-1, n_skyfib:-1, n_scifib:-1, $
		 n_bins:-1, jkmin:FLTARR(5), jkmax:FLTARR(5), bin_wdflag:INTARR(5), bin_usewdflag:INTARR(5), $
		 bin_frac:FLTARR(5), bin_pri:INTARR(5), jk_tbit:INTARR(5), wd_tbit:INTARR(5), co_frac:FLTARR(3), $
		 co_hmin:FLTARR(3), co_hmax:FLTARR(3), co_nvisits:INTARR(3), sc_minh:!VALUES.F_NAN, $
		 sc_maxh:!VALUES.F_NAN, te_mnjk:!VALUES.F_NAN, te_mxjk:FLTARR(3), te_minh:!VALUES.F_NAN, $
		 te_maxh:FLTARR(2), clra:DBLARR(16), cldec:DBLARR(16), clrad:DBLARR(16) },1)

dpars.fieldname = YANNY_PAR(hdr,'fieldname')
dpars.racen = YANNY_PAR(hdr,'racen')
dpars.deccen = YANNY_PAR(hdr,'deccen')
dpars.designid = YANNY_PAR(hdr,'designid')
dpars.locationid = YANNY_PAR(hdr,'locationid')
dpars.plateid = YANNY_PAR(hdr,'plateid')
dpars.design_type = YANNY_PAR(hdr,'design_type')
dpars.design_driver = YANNY_PAR(hdr,'design_driver')
dpars.comments = YANNY_PAR(hdr,'comments')
dpars.radius = YANNY_PAR(hdr,'radius')
dpars.short_ver = YANNY_PAR(hdr,'short_ver')
dpars.med_ver = YANNY_PAR(hdr,'med_ver')
dpars.long_ver = YANNY_PAR(hdr,'long_ver')
dpars.n_visits = YANNY_PAR(hdr,'n_visits')
dpars.n_tellfib = YANNY_PAR(hdr,'n_tellfib')
dpars.n_skyfib = YANNY_PAR(hdr,'n_skyfib')
dpars.n_scifib = YANNY_PAR(hdr,'n_scifib')
dpars.n_bins = YANNY_PAR(hdr,'n_bins')
dpars.jkmin = YANNY_PAR(hdr,'jkmin')
dpars.jkmax = YANNY_PAR(hdr,'jkmax')
dpars.bin_wdflag = YANNY_PAR(hdr,'bin_wdflag')
dpars.bin_usewdflag = YANNY_PAR(hdr,'bin_usewdflag')
dpars.bin_frac = YANNY_PAR(hdr,'bin_frac')
dpars.bin_pri = YANNY_PAR(hdr,'bin_pri')
dpars.jk_tbit = YANNY_PAR(hdr,'jk_tbit')
dpars.wd_tbit = YANNY_PAR(hdr,'wd_tbit')
dpars.co_frac = YANNY_PAR(hdr,'co_frac')
dpars.co_hmin = YANNY_PAR(hdr,'co_hmin')
dpars.co_hmax = YANNY_PAR(hdr,'co_hmax')
dpars.co_nvisits = YANNY_PAR(hdr,'co_nvisits')
dpars.sc_minh = YANNY_PAR(hdr,'sc_minh')
dpars.sc_maxh = YANNY_PAR(hdr,'sc_maxh')
dpars.te_mnjk = YANNY_PAR(hdr,'te_mnjk')
dpars.te_mxjk = YANNY_PAR(hdr,'te_mxjk')
dpars.te_minh = YANNY_PAR(hdr,'te_minh')
dpars.te_maxh = YANNY_PAR(hdr,'te_maxh')
dpars.clra = YANNY_PAR(hdr,'clra')
dpars.cldec = YANNY_PAR(hdr,'cldec')
dpars.clrad = YANNY_PAR(hdr,'clrad')

RETURN,dpars

end
