pro plothess,infile=infile,age=age,outfile=outfile,quantities=quantities,mtotal=mtotal,nbins=nbins

if ~keyword_set(infile) then infile='isochrones/zp00.dat'
if ~keyword_set(age) then age=9.0
if ~keyword_set(m_tot) then m_tot=100.0
if ~keyword_set(nbins) then nbins=[20,20]

fmt='f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f'
READCOL,infile,z,logage,m_ini,m_act,logl,logt,logg,mbol,um,bm,vm,rm,im,jm,hm,km,int_imf,stage,F=fmt,/SILENT,count=ns

gd=where(logage eq age,ngd)
xdata=logt[gd] & nx=n_elements(x)
ydata=logl[gd] & ny=n_elements(y)
int_imf=int_imf[gd]

xbinsize=abs(max(xdata)-min(xdata))/nbins[0]
ybinsize=abs(max(ydata)-min(ydata))/nbins[1]

xpos=fltarr(nbins[0]*nbins[1])
ypos=fltarr(nbins[0]*nbins[1])
imf=fltarr(nbins[0]*nbins[1])

xpos=0
ypos=0
z=0
for i=0,nbins[0]-1 do begin
    for j=0,nbins[1]-1 do begin
        xpos1=min(xdata)+(xbinsize/2.)+(xbinsize*i)
        ypos1=min(ydata)+(ybinsize/2.)+(ybinsize*j)

        if i eq 0 and j eq 0 then xpos=xpos1 else xpos=[xpos,xpos1]
        if i eq 0 and j eq 0 then ypos=ypos1 else ypos=[ypos,ypos1]

        incell=where((xdata ge xpos1-xbinsize/2.) and (xdata lt xpos1+xbinsize/2.) and (ydata ge ypos1-ybinsize/2.) and (ydata lt ypos1+ybinsize/2.),nincell)

        if nincell eq 0 then begin
            z1=0.0
        endif else begin
            if nincell eq 1 then begin
                z1=(int_imf[incell+1]-int_imf[incell])*m_tot
            endif else begin
                z1=(int_imf[max(incell)]-int_imf[min(incell)])*m_tot
            endelse
        endelse
        if i eq 0 and j eq 0 then z=z1 else z=[z,z1]
    endfor
endfor

writecol,'idl_hess_'+stringize(nbins[0])+'x'+stringize(nbins[1])+'.txt',xpos,ypos,z,fmt='(f,x,f,x,f)'

fname='idl_hess'
SET_PLOT,'PS'  &  !P.FONT=0
DEVICE,FILENAME=fname+'.ps',/COLOR,XSIZE=8,YSIZE=7,/INCHES,SET_FONT='Helvetica'
xtit='logT'  &  ytit='logL'
CTLOAD,1,/reverse

!P.MULTI=[0,1,1,2,0]
!P.POSITION=[0.08,0.08,0.99,0.99]
xr=[max(xpos)+xbinsize/2.,min(xpos)-xbinsize/2.]
yr=[min(ypos)-ybinsize/2.,max(ypos)+ybinsize/2.]
PLOTC,xpos,ypos,z,/xs,/ys,ps=sym(5),symsize=2,xr=xr,yr=yr
CTLOAD,39
xbins=xpos[uniq(xpos)]
for i=0,nbins[0]-1 do oplot,[xbins[i]+xbinsize/2.,xbins[i]+xbinsize/2.],[-100,100]
for i=0,nbins[1]-1 do oplot,[-100,100],[ypos[i]+ybinsize/2.,ypos[i]+ybinsize/2.]
oplot,xdata,ydata,ps=sym(1),symsize=0.5
PLOT,xpos,ypos,/nodata,/xs,/ys,xthick=2,ythick=2,xtit=xtit,ytit=ytit,xr=xr,yr=yr

DEVICE, /CLOSE
SET_PLOT,'X'
SPAWN,'convert -flatten '+fname+'.ps '+fname+'.png'


end
