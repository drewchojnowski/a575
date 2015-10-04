pro solve_lane_emden,n,dx=dx,xfrac=xfrac,zfrac=zfrac,mass=mass,radius=radius,findconstants=findconstants,plot=plot,png=png
;=============================================================================;
; This program solves the Lane-Emden equation via a "shooting" method,        ;
; whereby initial values are used to start from the center and work outwards. ;
;                                                                             ;
; REQUIRED INPUT:                                                             ;
;        n = polytropic index                                                 ;
;                                                                             ;
; OPTIONAL INPUT:                                                             ;
;        dx = xi increment (determines fineness of solution)                  ;
; 	 xfrac = fractional hydrogen abundance (default is xfrac=0.7)         ;
;        zfrac = fractional metal abundance (default is zfrac=0.02)           ;
;        mass = stellar mass in grams (default is mass=1.9891d33)             ;
;        radius = stellar mass in cm (default is radius=6.955d10)             ;
;        [/findconstant] = option to calculate & print values                 ;
;        [/plot] = option to make plots                                       ;
;        [/png] = convert the .ps plots to .png                               ;
;                                                                             ;
; VARIABLES: (1) x = xi, (2) t = theta                                        ;
;                                                                             ;
; The following form will be used in calculation:                             ;
; d^2t/dx^2 = - [(2/x)*(dt/dx) + t^n]                                         ;
;=============================================================================;

;===============================================================
; BOUNDARY CONDITIONS:
;    1. t(x)=1 at x=0
;    2. dt/dx=0 at x=0
t=1.0
dtdx=0.0

;===============================================================
; give x a small, non-zero starting value:
x=0.0000000001

;===============================================================
; dx determines the fineness of the grid
; if n=2 and dx=0.0001,   43532 iterations/data points
; if n=2 and dx=0.00001, 434892 iterations/data points
if ~keyword_set(dx) then dx=0.00001
;===============================================================

outfile='polytrope_n'+stringize(n,ndec=2)+'.txt'
OPENW,gunit,outfile,/GET_LUN
counter=double(0)
; integrate outward until x=theta crosses the first zero
while t ge 0 do begin
	dtdx = dtdx-((2.0*dtdx/x)+(t^n))*dx
	t = t+(dtdx*dx)
	x = x+dx
	PRINTF,gunit,x,t,dtdx
	counter=counter+1
endwhile
FREE_LUN,gunit

PRINT,'the first zero was crossed after '+stringize(counter)+' iterations.'

;=============================================================================;
; Option to calculate values 
if keyword_set(findconstants) then begin
	if ~keyword_set(xfrac) then xfrac = 0.70 ; fractional Hydrogen abundance
	if ~keyword_set(zfrac) then zfrac = 0.02 ; fractional metal abundance
	if ~keyword_set(mass) then mass = 1.9891d33 ; solar mass (g)
	if ~keyword_set(radius) then radius = 6.955d10 ; solar radius (cm)
	grav = 6.67408d-8 ; gravitational constant (cm^3 g^-1 s^-2)
	m_u = 1.66054d-24 ; atomic mass unit (g)
	k_b = 1.380658d-16 ; Boltzmann constant (cm^2 g s^-2 K^-1)

	mu = 4.0/(3.0+(5.0*xfrac)-zfrac) ; mean molecular weight

	READCOL,outfile,x,t,dtdx,F='D,D,D',/SILENT
	p=WHERE(ABS(t) eq MIN(ABS(t)),np)

	x1=x[p]
	PRINT,'XI_1 = ',x1
	dtdx1=dtdx[p]
	PRINT,'dTHETA/dXI_1 = ',dtdx1
	bla = -1.0*(x1/(3.0*dtdx1))
	PRINT,'rho_c/rho_avg = ',bla
	bign = ((4.0*!pi)^(1.0/n))/(n+1.0) * ((-1.0*(x1^((n+1.0)/(n-1.0))))*dtdx1)^((1.0-n)/n)
	PRINT,'N_n = ',bign
	w_n=(4.0*!pi*(n+1.0)*(dtdx1^2.0))^(-1.0)
	PRINT,'W_n = ',w_n
	bigtheta=( -1.0*(n+1.0)*x1*dtdx1 )^(-1.0)
	PRINT,'Theta_n = ',bigtheta
	rho_c=bla*((3.0*mass)/(4.0*!pi*(radius^3.0)))
	PRINT,'Rho_c = ',rho_c
;	alternate way to calculate p_c
	k=bign*grav*(mass^((n-1.0)/n))*(radius^((3.0-n)/n))
;	p_c=k*(rho_c^((n+1.0)/n))
;	PRINT,'P_c = ',p_c
	p_c=(w_n*grav*(mass^2.0))/(radius^4.0)
	PRINT,'P_c = ',p_c
	t_c=(bigtheta*grav*mass*mu*m_u)/(k_b*radius)
	PRINT,'T_c = ',t_c
	mass_tot=(-4.0*!pi)*((((n+1)*k)/(4.0*!pi*grav))^(3/2.0))*((x1^2.0)*dtdx1)
	PRINT,'Total mass = ',mass_tot
endif

;=============================================================================;
; option to make plots
if keyword_set(plot) then begin
	outfile='polytrope_n'+stringize(n,ndec=2)
	SET_PLOT,'PS'  &  !P.FONT=0
	DEVICE,FILENAME=outfile+'.ps',/COLOR,XSIZE=11,YSIZE=8,/INCHES,SET_FONT='Times-Roman'
	xtit=CGSYMBOL('xi')  &  ytit=CGSYMBOL('theta')
	CTLOAD,39

	!P.POSITION=[0.08,0.095,0.99,0.99]

	PLOT,x,t,/NODATA,CHARSIZE=1.6,XS=1,YS=1,XTIT=xtit,YTIT=ytit,YR=[0,1],XR=[0,x1],XTHICK=2,YTHICK=2,THICK=2
	OPLOT,x,t,COLOR=35,THICK=2
	OPLOT,x,t^n,COLOR=80,THICK=2
	OPLOT,x,t^(n+1),COLOR=215,THICK=2
	mass_int=(-4.0*!pi)*((((n+1)*k[0])/(4.0*!pi*grav))^(3/2.0))*((x^2.0)*dtdx)
	q=mass_int/mass_tot[0]
	OPLOT,x,q,COLOR=250,THICK=2

	label1=CGSYMBOL('theta')+'('+CGSYMBOL('xi')+') = T/T!DC!N'
	label2=CGSYMBOL('theta')+'!Un!N('+CGSYMBOL('xi')+') = '+CGSYMBOL('rho')+'/'+CGSYMBOL('rho')+'!DC!N'
	label3=CGSYMBOL('theta')+'!Un+1!N('+CGSYMBOL('xi')+') = P/P!DC!N'
	label4='q('+CGSYMBOL('xi')+') = m/M'

	XYOUTS,x1-x1*0.05,0.75,'n = '+stringize(n,ndec=2),ALIGNMENT=1,COLOR=0,CHARSIZE=1.6
	XYOUTS,x1-x1*0.05,0.65,label1,ALIGNMENT=1,COLOR=35,CHARSIZE=1.4
	XYOUTS,x1-x1*0.05,0.55,label2,ALIGNMENT=1,COLOR=80,CHARSIZE=1.4
	XYOUTS,x1-x1*0.05,0.45,label3,ALIGNMENT=1,COLOR=215,CHARSIZE=1.4
	XYOUTS,x1-x1*0.05,0.35,label4,ALIGNMENT=1,COLOR=250,CHARSIZE=1.4

	DEVICE, /CLOSE
	SET_PLOT,'X'
	; option to make pngs
	if KEYWORD_SET(png) then SPAWN,'convert -flatten '+outfile+'.ps '+outfile+'.png'
endif

end
