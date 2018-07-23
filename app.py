'''﻿﻿import time
import json
import re
import os
import zlib
import decimal
import urllib2
import datetime'''





#﻿import datetime
import time,datetime
import json
import re
import os
import zlib
import decimal
import urllib2

import socket
import gzip
from StringIO import StringIO
from base64 import b64encode, b64decode
from decimal import Decimal


from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512



class Client(object):
  def __init__(self, serverkey, privatekey, useridd):
   self.serverkey= serverkey
   self.privatekey= privatekey
   self.useridd= useridd





  def modeon(self):
   print('MODE: ON')
   if os.path.exists('fairlay.txt'):
     with open('fairlay.txt','r') as rfl:
       rfa=rfl.read()
       print(rfa)

  
  
  
  def backtolay(self,odd,amt,target,newodd,newamt,check,ich,indd):
   oddod=''
   liab=''
   slay=''
   layamt=''
   llayamt=''
   bako=''
   pbako=''
   playamt=''
   podd=''
   reservedamt=''
   tot=''
   percen=''
   lisk=''
   reservedamt=check['reserved']
   oddod=newodd-1
   if newodd !='0.0':
     if decimal.Decimal(str(newamt)) >= decimal.Decimal(str(reservedamt)):
       bako=odd*amt
       bako-=amt
       layamt=odd*amt/newodd
       llayamt=layamt
       slay=0.35*layamt/100
       llayamt-=slay
       liab=oddod*layamt
     
       pbako=0.35*bako/100
       bako-=pbako
  
  
  
  
  
       tot=amt+liab
       playamt=llayamt-amt
       podd=bako-liab
       minc=min(podd,playamt)
       percen=minc*100/tot
       if percen >= target:
         if liab >= check['reserved']:
           check['closeodd'].append([newodd,reservedamt,ich[8],ich[10]])
           #check['state']='closed'
           lisk=[check['closeodd'][-1][-2],indd,1,newodd,reservedamt]
         if liab < check['reserved']:
           check['closeodd'].append([newodd,round(float(liab),2),ich[8],ich[10]])
           #check['state']='closed'
           lisk=[check['closeodd'][-1][-2],indd,1,newodd,round(float(liab),2)]
  
   return [check,lisk]
  
  
  
  
  def laytoback(self,odd,amt,target,newodd,newamt,check,ich,indd):
   oddod=''
   slay=''
   layamt=''
   llayamt=''
   backamt=''
   bako=''
   pbako=''
   playamt=''
   podd=''
   reservedamt=''
   tot=''
   percen=''
   lisk=''
   reservedamt=check['reserved']
   oddod=odd-1
   if newodd !='0.0':
     if decimal.Decimal(str(newamt)) >= decimal.Decimal(str(reservedamt)):
       layamt=amt/oddod
       llayamt=layamt
       slay=0.35*layamt/100
       llayamt-=slay
       backamt=layamt*odd/newodd
     
       bako=backamt*newodd
       bako-=backamt
       pbako=0.35*bako/100
       bako-=pbako
  
       tot=amt+backamt
       playamt=llayamt-backamt
       podd=bako-amt
       minc=min(podd,playamt)
       percen=minc*100/tot
       if percen >= target:
         if backamt >= check['reserved']:
           check['closeodd'].append([newodd,reservedamt,ich[8],ich[10]])
           #check['state']='closed'
           lisk=[check['closeodd'][-1][-2],indd,0,newodd,reservedamt]
  
         if backamt < check['reserved']:
           check['closeodd'].append([newodd,round(float(backamt),2),ich[8],ich[10]])
           #check['state']='closed'
           lisk=[check['closeodd'][-1][-2],indd,0,newodd,round(float(backamt),2)]
  
   return [check,lisk]
  
  
  
  
  
  
  def clist(self,finlistt,listch):
  
   #import funfst,dump,load,backtolay,laytoback
   clist=[]
   nam=''
   kat=[]
   hold=''
   hors=''
   indd=''
   lik=''
   #timt=[[300,2400,'>5<40'],[780,2160,'>13<36'],[300,1020,'>5<17'],[300,1260,'>5<21'],[3480,5460,'>58<1.31min'],[1680,3660,'>28<1.01min']]
  
  # for vit in timt:
   with open('fairlay.txt','r') as lop:
     listukk=json.load(lop)
   tm=listukk['timestamp'][-1]
   for ic in finlistt:
     fi=self.funfst(ic)
     clist.append(fi)
   for ik in clist:
     indd=clist.index(ik)
     nam=ik[-2]+'-'+ik[-1]
      # hors=ik[-1]
     if nam in listch:
        # kat.append(j)
      # if nam in kat:
       hold=listukk[tm][nam]
       if hold !='':
         if hold['state']=='open':
           if hold['status']=='lay':
             hold=self.laytoback(hold['openodd'][0],hold['openodd'][1],hold['target'],ik[2],ik[3],hold,ik,indd)
             lik=hold[1]
           if hold['status']=='back':
             hold=self.backtolay(hold['openodd'][0],hold['openodd'][1],hold['target'],ik[6],ik[7],hold,ik,indd)
             lik=hold[1]
           listukk['loadp']={nam:hold[0]}
           if listukk['lock'] > 0:
             listukk['lock']= listukk[0]['lock']-1
             listukk['release'].append(ik[11],ik[12])
           
           #listukk['loadp']=hold
           with open('fairlay.txt','w') as hola:
             json.dump(listukk,hola)
  
  
  
  
  def tsorttimey(self,time):
   #import re,datetime,decimal,tsorttime,tsorttimer
   #,tsorttimey
   fe=self.tsorttimer(time)
   fa=self.tsorttime()
   a=datetime.timedelta(seconds=fe)
   b=datetime.timedelta(seconds=fa)
   c=b-a
   c=str(c)
  
   mo=re.compile(r'(\d+):(\d+):(\d+)')
   ba=mo.findall(c)
   aa=int(ba[0][0])
   bb=int(ba[0][1])
   cc=int(ba[0][2])
   aa=aa*3600
   bb=bb*60
   cc=aa+bb+cc
   return cc
  
  def tsorttimer(self,time):
   import re,datetime
  #time=datetime.datetime.now()
  #time=str(time)
  #time='11:50'
   mo=re.compile(r'(\d+):(\d+)')
   ba=mo.findall(time)
   a=int(ba[0][0])
   b=int(ba[0][1])
   a=a*3600
   b=b*60
   c=a+b
   return c
  # print(c)
  # print
  
  
  def tsorttime(self):
   import re,datetime
   time=datetime.datetime.utcnow()
   time=str(time)
   mo=re.compile(r'(\d+):(\d+):(\d+)')
   ba=mo.findall(time)
   a=int(ba[0][0])
   b=int(ba[0][1])
   c=int(ba[0][2])
   a=a*3600
   b=b*60
   c=a+b+c
   return c
  
  
  
  def tsortdelta(self,time):
   import datetime
   ''',decimal,tsorttime,tsorttimer'''
   #,tsorttimey
   fe=self.tsorttimer(time)
   fa=self.tsorttime()
   a=datetime.timedelta(seconds=fe)
   b=datetime.timedelta(seconds=fa)
   c=b-a
   c=str(c)
   return c
  
  
  def subb(self,mo):
   import re
   namchan=re.compile(r'\[\]')
   nb=namchan.sub('[[0.0,0.0]]',mo)
   return nb
  
  
  def stake(self,stak,per):
   rm=5*stak/100
   stak-=rm
   bg=per*stak/100
   sm=stak-bg
   bg=round(float(bg),2)
   sm=round(float(sm),2)
   rm=round(float(rm),2)
   return [bg,sm,rm]
  
  def sorttime(self,time):
   import re
   time=str(time)
   mo=re.compile(r'(\d+:\d+)')
   ba=mo.findall(time)
   a=ba[0]
   #b=int(ba[0][1])
   #c=int(ba[0][2])
   return str(a)
  
  
  def settlevoid(self):
   import json
   z=''
   tm=''
   k=''
   l=''
   m=''
   cn=1200
   
   with open('fairlay.txt','r') as tk:
     z=json.load(tk)
   tm=z['timestamp'][-1]
   releaseg=z['release1']
   if z['release1'] !=[]:
     for j in z['release1']:
   
   
   
   
       k=self.tsorttimer(j[0])
       k+=1200
       l=self.tsorttime()
       m=l-k
       if m<cn:
         ###self.settledmatchq()
         if j not in releaseg:
           z['release1'].remove(j)
           if z['lock']>0:
             z['lock']-=1
           self.dumpp(z)
  
  
  def settledtime(self):
   import json
   z=''
   tm=''
   k=''
   l=''
   m=''
   cn=1200
   
   with open('fairlay.txt','r') as tk:
     z=json.load(tk)
   tm=z['timestamp'][-1]
   if z['release'] !=[]:
     for j in z['release']:
   
   
   
   
       k=self.tsorttimer(j[0])
       k+=1200
       l=self.tsorttime()
       m=l-k
       if m<cn:
         ###self.settledmatchq()
         z['release'].remove(j)
         if z['lock']>0:
           z['lock']-=1
         self.dumpp(z)
  
  
  '''def laytoback(odd,amt,target,newodd,newamt,check,ich):
   oddod=''
   slay=''
   layamt=''
   llayamt=''
   backamt=''
   bako=''
   pbako=''
   playamt=''
   podd=''
   reservedamt=''
   tot=''
   percen=''
   reservedamt=check['reserved']
   oddod=odd-1
   if newodd !='0.0':
     if decimal.Decimal(str(newamt)) >= decimal.Decimal(str(reservedamt)):
       layamt=amt/oddod
       llayamt=layamt
       slay=0.25*layamt/100
       llayamt-=slay
       backamt=layamt*odd/newodd
     
       bako=backamt*newodd
       bako-=backamt
       pbako=0.25*bako/100
       bako-=pbako
  
       tot=amt+backamt
       playamt=llayamt-backamt
       podd=bako-amt
       minc=min(podd,playamt)
       percen=minc*100/tot
       if percen >= target:
         if backamt >= check['reserved']:
           check['closeodd'].append([newodd,reservedamt,ich[8],ich[10]])
           check['state']='closed'
         if backamt < check['reserved']:
           check['closeodd'].append([newodd,round(float(backamt),3),ich[8],ich[10]])
           check['state']='closed'
   return check
  '''
  
  
  
  #getorder
  import re
  def getl(self,p):
   mo=re.compile(r'(\d+).(\d+)')
   ba=mo.findall(p)
   return int(ba[0][0][0])
  def getr(self,p):
   mo=re.compile(r'(\d+).(\d+)')
   ba=mo.findall(p)
   return int(ba[0][1][0])
  
  #funfste
  '''import funfst'''
  def funfste(self,fst,scd):
   alist=self.funfst(fst)
   blist=self.funfst(scd)
   return [alist,blist]
  
  
  
  
  
  import decimal
  ''',getorder'''
  def funfst(self,fst):
   alist=[]
   fstbone=self.getl(str(fst[2]))
   fstbtwo=self.getr(str(fst[2]))
   fstback=float(fst[2])
   fstbamt=float(fst[4])
  
   fstlone=self.getl(str(fst[3]))
   fstltwo=self.getr(str(fst[3]))
   fstlay=float(fst[3])
   fstlamt=float(fst[5])
  
   fsttime=fst[7]
   fstid=int(fst[10])
   fstrtime=str(fst[11])
   fstctime=fst[8]
   fststamp=fst[9]
   
   alist.append(fstbone)
   alist.append(fstbtwo)
   alist.append(fstback)
   alist.append(fstbamt)
   alist.append(fstlone)
   alist.append(fstltwo)
   alist.append(fstlay)
   alist.append(fstlamt)
   alist.append(fsttime)
   alist.append(fstrtime)
   
   #alist.append(fstctime)
   alist.append([fstctime,fstid,fststamp])
   
   alist.append(fstid)
   alist.append(fststamp)
   alist.append(fst[0])
   alist.append(fst[1])
   return alist
  
  
  
  def dateteste(self):
   import re,datetime
   time=datetime.datetime.utcnow()
   time=str(time)
   mo=re.compile(r'(\d+-\d+-\d+)')
   ba=mo.findall(time)
   ka=str(ba[0])
   return ka
  
  
  def datetest(self):
   import re,datetime
   time=datetime.datetime.now()
   time=str(time)
   #mo=re.compile(r'(\d+-\d+-\d+)')
   #ba=mo.findall(time)
   #print(str(ba[0]))
   return time
  
  
  
  '''def clist(finlistt,listch):
  
   import json
   #funfst,dump,load,backtolay,laytoback
   clist=[]
   nam=''
   kat=[]
   hold=''
   hors=''
   #timt=[[300,2400,'>5<40'],[780,2160,'>13<36'],[300,1020,'>5<17'],[300,1260,'>5<21'],[3480,5460,'>58<1.31min'],[1680,3660,'>28<1.01min']]
  
  # for vit in timt:
   with open('fairlay.txt','r') as lop:
     listukk=json.load(lop)
   tm=listukk['timestamp'][-1]
   for ic in finlistt:
     fi=self.funfst(ic)
     clist.append(fi)
   for ik in clist:
     nam=ik[-2]+'-'+ik[-1]
      # hors=ik[-1]
     if nam in listch:
        # kat.append(j)
      # if nam in kat:
       hold=listukk[tm][nam]
       if hold !='':
         if hold['state']=='open':
           if hold['status']=='lay':
             hold=self.laytoback(hold['openodd'][0],hold['openodd'][1],hold['target'],ik[2],ik[3],hold,ik)
           if hold['status']=='back':
             hold=self.backtolay(hold['openodd'][0],hold['openodd'][1],hold['target'],ik[6],ik[7],hold,ik)
           listukk[loadp]={nam:hold}
           #if listukk['lock'] > 0:
           #  listukk['lock']= listukk[0]['lock']-1
           #  listukk['release'].append(ik[11],ik[12])
           
           #listukk['loadp']=hold
           with open('fairlay.txt','w') as hola:
             json.dump(listukk,hola)
  '''
  
  def bids(self,t,g):
  # g=[]
   import re
   num1=re.compile(r'\"Bids\"\:(\[\[)(\d+.\d+),(\d+.\d+)(\]\])')
   mo=num1.findall(t)
   for i in range(len(mo)):
     g.append(mo[i][1])
   return g
  
  
  def bidamt(self,t,g):
  # g=[]
   import re
   num1=re.compile(r'\"Bids\"\:(\[\[)(\d+.\d+),(\d+.\d+)(\]\])')
   mo=num1.findall(t)
   for i in range(len(mo)):
     g.append(mo[i][2])
   return g
  
  
  '''def backtolay(odd,amt,target,newodd,newamt,check,ich):
   oddod=''
   liab=''
   slay=''
   layamt=''
   llayamt=''
   bako=''
   pbako=''
   playamt=''
   podd=''
   reservedamt=''
   tot=''
   percen=''
   reservedamt=check['reserved']
   oddod=newodd-1
   if newodd !='0.0':
     if decimal.Decimal(str(newamt)) >= decimal.Decimal(str(reservedamt)):
       bako=odd*amt
       bako-=amt
       layamt=odd*amt/newodd
       llayamt=layamt
       slay=0.25*layamt/100
       llayamt-=slay
       liab=oddod*layamt
     
       pbako=0.25*bako/100
       bako-=pbako
  
  
  
  
  
       tot=amt+liab
       playamt=llayamt-amt
       podd=bako-liab
       minc=min(podd,playamt)
       percen=minc*100/tot
       if percen >= target:
         if liab >= check['reserved']:
           check['closeodd'].append([newodd,reservedamt,ich[8],ich[10]])
           check['state']='closed'
         if liab < check['reserved']:
           check['closeodd'].append([newodd,round(float(liab),3),ich[8],ich[10]])
           check['state']='closed'
   return check
  '''
  
  
  def asks(self,t,g):
  # g=[]
   import re
   num1=re.compile(r'\"Asks\"\:(\[\[)(\d+.\d+),(\d+.\d+)(\]\])')
   mo=num1.findall(t)
   for i in range(len(mo)):
   	  g.append(mo[i][1])
   return g
  
  
  def askamt(self,t,g):
  # g=[]
   import re
   num1=re.compile(r'\"Asks\"\:(\[\[)(\d+.\d+),(\d+.\d+)(\]\])')
   mo=num1.findall(t)
   for i in range(len(mo)):
   	  g.append(mo[i][2])
   return g
  
  
  
  
  def timeinticks(self):
   tm=''
   nonce=''
   c=''
   c=3600*15
   c=10000000*c
   with open('fairlay.txt','r') as do:
     dok=json.load(do)
   tm=dok['timestamp'][-1]
   nonce=dok[tm]['nonce']
   nonce-=c
   return nonce
  
  
  
  
  
  '''def settledtimeq():
   import json
   z=''
   tm=''
   k=''
   l=''
   m=''
   t=''
   resolved=['resolved','runnerwon',etc]
   #import tsorttimer,tsorttime,load,dump
   cn=1200
   
   with open('fairlay.txt','r') as tk:
     z=json.load(tk)
   tm=z['timestamp'][-1]
   if z['release'] !=[]:
     t=self.getmatched()
     for j in z['release']:
       if t !=None and t !=[]:
         for i in t:
           if i['UserOrder']['MarketID']==j[0]:
             if i['status'] in resolved:
               z['release'].remove(j)
               if z['lock']>0:
                 z['lock']-=1
     with open('fairlay.txt','w') as kt:
       json.dump(z,kt)
   '''
  
  
  def flisttime(self,kpag):
   #import
   ''' datetest,bids,asks,bidamt,askamt,sorttime,tsortdelta,tsorttimey'''
   es=self.datetest()
   ess=self.dateteste()
  
  
  
   h=[]
   bds=[]
   aks=[]
   bbidamt=[]
   aaksamt=[]
   finlist=[]
   sufinlist=[]
   finlit=[]
   kkesh=[]
   finlista=[]
   klist=[]
   tm=''
   listtime=[]
   
  
   for s in range(len(kpag)):
     des=kpag[s]['Descr']
     if des =='win. All bets are void if any listed open runner with a winning chance of at least 2.5% withdraws or if there is a shared first place.':
  
       selfbids(kpag[s]['OrdBStr'],bds)
       self.asks(kpag[s]['OrdBStr'],aks)
       self.bidamt(kpag[s]['OrdBStr'],bbidamt)
       self.askamt(kpag[s]['OrdBStr'],aaksamt)
       e=self.datetest()
       racename=kpag[s]['Comp']
  
       idd=kpag[s]['ID']
       timestamp=self.sorttime(kpag[s]['Title'])
  
       timetogomin=self.tsortdelta(timestamp)
       timetogosec=self.tsorttimey(timestamp)
       for i in range(0,len(kpag[s]['Ru'])):
         hh=kpag[s]['Ru'][i]['Name']
       if not hh.endswith('CLOSED RUNNER'):
        #if 'CLOSED RUNNER' not in hh:
         h.append(hh)
       
       
       lh=len(h)
       lbid=len(bds)
       lask=len(aks)
       lbidamt=len(bbidamt)
       laksamt=len(aaksamt)
       if lh==lbid:
         if lask!=lbid:
           lba=lbid-lask
           for ib in range(lba):
             aks.append('0.0')
  
         if lbidamt!=laksamt:
           lbb=lbidamt-laksamt
           for ibb in range(lbb):
             aaksamt.append('0.0')
       for v in range(len(h)):    
  
         fffd=[racename,h[v],bds[v],aks[v],bbidamt[v],aaksamt[v],v,timetogosec,timetogomin,timestamp,idd,e]
         fffk=[timetogomin,v,h[v],bds[v],aks[v],bbidamt[v],aaksamt[v],timestamp,racename]
   
         finlist.append(fffd)
       sufinlist.append(finlist)
               #klist.append(fffk)
   for jj in sufinlist:
     if float(sufinlist[jj][0][2])<1.9:
       tm=float(sufinlist[jj][0][-5])
       listtime.append(tm)
   return listtime
  
  
  
  
  
  
  
  #######
  def filt(self):
   import json
   ulist=[]
   lista=[]
   with open('fairlay.txt','r') as wk:
     k=json.load(wk)
   tm=k['timestamp'][-1]
   for i in k[tm]:
     lista.append(i)
   ulist.append(k['loadp'])
   ulist.append(lista)
   ulist.append(k['release'])
   return ulist
  # if k['loadp']='':
  
  
  def filt1(self,fin):
   k=self.filt()
   if k[o]=='' and len(k[2])<1:
     self.foo8(fin,k[1])
  
  def filt2(self,finn):
   kk=self.filt()
   if kk[o]=='' and len(k[2])<1:
     self.foo1(finn,kk[1])
     self.foo3(finn,kk[1])
     self.foo4(finn,kk[1])
     self.foo5(finn,kk[1])
     self.foo6(finn,kk[1])
     #self.foo7(finn,kk[1])
  
  def filt3(self,finnn):
   kkk=self.filt()
   if kkk[o]=='' and len(k[2])<1:
     self.foo2(finnn,kkk[1])
     
     
  def filt4(self,fin):
   k=self.filt()
   if k[o]=='':
     self.clist(fin,k[1])
  ########
  
  
  def dumpp(self,listuk):
   import json
   with open('fairlay.txt','w') as dup:
     json.dump(listuk,dup)
  
  
  
  
  def checkmatched(self):
   import json
   al=''
   t=self.getmatched()
   tm=''
   release=''
   match=['matched','resolved',3,2,1]
   zp=''
   listp=[]
   bla=''
   listo=['openodd','closeodd']
   dictk={'back':0,'lay':1}
   with open('fairlay.txt','r') as fz:
     z=json.load(fz)
   tm=z['timestamp'][-1]
   zp=z['loadp']
  
   if t !=None and t !=[]:
     for j in zp:
       listp.append(j)
     bla=dictk[zp[listp[0]]['status']]
    
     for l in listo:
       if zp[listp[0]][l] !=[]:
         if l=='openodd':
           al=1
           for i in t:
             if bla==i['UserOrder']['BidOrAsk'] and i['UserOrder']['MarketID']==zp[listp[0][l][-1][-2]]:
               if i['status'] in match:
                 z[tm][listp[0]]=zp[listp[0]]
                 z['loadp']=''
                 z['lock']+=1
                 with open('fairlay.txt','w') as dt:
                   json.dump(z,dt)
                  
         if l=='closeodd':
           release=[z[tm]['closeodd'][-1][1],z[tm]['closeodd'][-1][2]]
           for i in t:
             if bla==i['UserOrder']['BidOrAsk'] and i['MarketID']==zp[listp[0][l][-1][-2]]:
               if i['status'] in match:
                 z[tm][listp[0]]=zp[listp[0]]
                 z['loadp']=''
                 z['release'].append(release)
                 if z['lock']>0:
                   z['lock']-=1
                 with open('fairlay.txt','w') as dtt:
                   json.dump(z,dtt)
  
     if z['loadp'] !='':
       z['loadp']=''
       with open('fairlay.txt','w') as dgg:
         json.dump(z,dgg)
  
  
  
  
  def checkfinal(self):
   #import checkmatch
   tm=''
   v=''
   with open('fairlay.txt','r') as dg:
     tm=f['timestamp'][-1]
     f=json.load(dg)
   if f['loadp'] !=v:
     self.checkmatched()
  
  
  def check1(self,ki,tm):
   listp=[]
   a=''
   b=''
   c=60*30
   listp=[]
   f=60*30
   h=60*90
   ho=60*60
   ho+=300
   mi=60*30
   
   a=tm+mi
   for i in ki:
     b=i-a
     if b<h:
       listp.append(1)
   return listp
  
  
  '''
  def addloadp(self):
   tm=''
   zp=''
   with open('fairlay.txt','r') as do:
     dok=json.load(do)
   tm=dok['timestamp'][-1]
   if dok['loadp'] !=[]:
     zp=dok['loadp']
     for i in zp:
       dok[tm][i]=zp[i]
     dok['loadp']=''
     self.dumpp(dok)
  '''
  
  def addloadp(self):
   tm=''
   zp=''
   with open('fairlay.txt','r') as do:
     dok=json.load(do)
   tm=dok['timestamp'][-1]
   if dok['loadp'] !=[]:
     zp=dok['loadp']
     for i in zp:
       dok[tm][i]=zp[i]
     dok['loadp']=''
     with open('fairlay.txt','w') as frrt:
       json.dump(dok,frrt)
  
  
  
  def verifyresponse(self, message):
   idx = message.find('|')
   if idx == -1:
     return True
  
   signed_message = message[:idx]
   original_message = message[idx+1:]
   key = RSA.importKey(self.serverkey)
   signer = PKCS1_v1_5.new(key)
   digest = SHA512.new()
   digest.update(original_message)
   if signer.verify(digest, base64.b64decode(signed_message + "=" * ((4 - len(signed_message) % 4) % 4))):
     return True
  
  def signmessage(self, message):
   key = RSA.importKey(self.privatekey)
   signer = PKCS1_v1_5.new(key)
   digest = SHA512.new()
   digest.update(message)
   sign = signer.sign(digest)
   return base64.b64encode(sign)
  
  
  
  
  def sendrequest(self,message, signed=False, tries=0):
   retur=''
   try:
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.connect((self.serverip, self.serverport))
     message_signature = ''
     if signed:
       message_signature = self.signmessage(message)
     message_to_send = '{}|{}<ENDOFDATA>'.format(message_signature, message)
     s.send(message_to_send)
     data = ''
     while True:
       new_data = s.recv(4096)
       if not new_data:
         break
       data += new_data
     s.close()
     response = gzip.GzipFile(fileobj=StringIO.StringIO(data)).read()
   except (socket.timeout, socket.error) as e:
     retur= None
  
   if not self.verifyresponse(response):
     retur= None
  
         
   response = response.split('|')[-1]
  
   if response.startswith('XError') or response.startswith('YError'):
        
     retur= None
              
   if retur !=None:
     retur= response
  
   return retur
  
  
  
  
  
  
  
  
  
  
  
  def placeorder(self,marketid,runner,backorlay,odds,amount):
   nonce = int(time.time())*1000
      #backorlay = {'back':1,'lay':0}
   userid= self.useridd
   #userid = 12445555556
   userid*=1000
   requestid=userid+62
   matchedsub='fairlay'
   ordertype=2
   message ='{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(nonce,userid,requestid,marketid,runner,backorlay,odds,amount,ordertype,matchedsub,6000)
  
   response = self.sendrequest(message, signed=True)
   return response
  
  
  
  def getmatched(self):
   import json
      #nonce = int(time.time())*1000
   nonce=(int(round((time.time())*1000)))
   ticks=self.timeinticks()
      #backorlay = {'back':1,'lay':0}
   userid = self.useridd
   userid*=1000
   requestid=userid+27
   matchedsub='fairlay'
      #ordertype=2
   message ='{}|{}|{}|{}'.format(nonce,userid,requestid,ticks)
  
   response = self.sendrequest(message, signed=True)
      
   try:
     return json.loads(response)
   except TypeError:
     return None
  
  
  
  def fetch(self):
   
   fixx=[]
   displaylist=[]
   h=[]
   bds=[]
   aks=[]
   bbidamt=[]
   aaksamt=[]
   finlist=[]
   finlit=[]
   kkesh=[]
   finlista=[]
   klist=[]
   timm=''
   stng=''
   flis=''
   fst=''
   fcd=''
   listta=''
   time=''
   p=''
   onlydate=''
   
   
   url='http://31.172.83.181:8080/free/markets/%7B%22Cat%22:7,%22TypeOr%22:[1,2],%22SoftChangedAfter%22:%222016-06-01T12:01:30%22,%22OnlyActive%22:true,%22NoZombie%22:true,%22ToID%22:10000%7D'
  
   url1='http://31.172.83.181:8080/free/time'
   pd=''
   space=''
   kkm=''
   listm=''
   
  
   p=str(datetime.datetime.utcnow())
   onlydate=self.dateteste()
  # print(p)
   time=datetime.datetime.utcnow()
   time=str(time)
   mo=re.compile(r'(\d+:\d+:\d+)')
   ba=mo.findall(time)
   ka=ba[0][0]+ba[0][1]
  #print(int(ka))
   if int(ka)>(1*10) and int(ka)<21:
  #  print('yes')
  # if h>11 and h<21:
    
     if not os.path.exists('fairlay.txt'):
       response=urllib2.urlopen(url1)
       page=zlib.decompress(response.read(),16+zlib.MAX_WBITS)
       page=page.decode()
       servertime=int(page)
      
       pd={'release1':[],'stake':2,'timestamp':[onlydate],'loadp':space,'release':[],'lock':0,onlydate:{'nonce':servertime}}
       with open('fairlay.txt','w') as dor:
         json.dump(pd,dor)
  
     else:
       with open('fairlay.txt','r') as dorr:
         m=json.load(dorr)
        
       for onam in m:
         listm.append(onam)
       if onlydate not in listm:
         m[onlydate]={'nonce':''}
        
        
       if onlydate not in m['timestamp']:
         m['timestamp'].append(onlydate)
       kkm=m['timestamp'][-1]
       if m[kkm]['nonce']=='':
      
         rresponse=urllib2.urlopen(url)
         ppage=zlib.decompress(rresponse.read(),16+zlib.MAX_WBITS)
         ppage=ppage.decode()
         sservertime=int(ppage)
      
         m[kkm]['nonce']=sservertime
         with open('fairlay.txt','w') as dord:
           json.dump(m,dord)
  
  
  
   
   
   
     #timt=[[300,2400,'>5<40'],[780,2160,'>13<36'],[300,1020,'>5<17'],[300,1260,'>5<21'],[3480,5460,'>58<1.31min'],[1680,3660,'>28<1.01min']]
  
    # url='http://31.172.83.181:8080/free/markets/%7B%22Cat%22:7,%22TypeOr%22:[1,2],%22SoftChangedAfter%22:%222016-06-01T12:01:30%22,%22OnlyActive%22:true,%22NoZombie%22:true,%22ToID%22:10000%7D'
  
   #url='http://31.172.83.181:8080/free/markets/%7B%22Cat%22:7,%22TypeOr%22:[1,2],%22SoftChangedAfter%22:%222016-06-01T12:01:30%22,%22OnlyActive%22:true,%22ToID%22:10000%7D'
   
   
     kresponse=urllib2.urlopen(url)
     kpage=zlib.decompress(kresponse.read(),16+zlib.MAX_WBITS)
     kpage=kpage.decode()
     if not kpage.startswith('XError') or page.startswith('YError'):
       kspage=self.subb(kpage)
       kpag=json.loads(kspage)
       if kpag !=[]:
       
         flis=self.flisttime(kpag)
         
         #es=datetest.datetest()
         #ess=dateteste.datetest()
  
         for s in range(len(kpag)):
           des=kpag[s]['Descr']
           if des =='win. All bets are void if any listed open runner with a winning chance of at least 2.5% withdraws or if there is a shared first place.':
           
             self.bids(kpag[s]['OrdBStr'],bds)
             self.asks(kpag[s]['OrdBStr'],aks)
             self.bidamt(kpag[s]['OrdBStr'],bbidamt)
             self.askamt(kpag[s]['OrdBStr'],aaksamt)
             e=self.datetest()
             racename=kpag[s]['Comp']
  
             idd=kpag[s]['ID']
             timestamp=self.sorttime(kpag[s]['Title'])
  
             timetogomin=self.tsortdelta(timestamp)
             timetogosec=self.tsorttimey(timestamp)
             for i in range(0,len(kpag[s]['Ru'])):
               hh=kpag[s]['Ru'][i]['Name']
             if not hh.endswith('CLOSED RUNNER'):
        #if 'CLOSED RUNNER' not in hh:
               h.append(hh)
       
       
             lh=len(h)
             lbid=len(bds)
             lask=len(aks)
             lbidamt=len(bbidamt)
             laksamt=len(aaksamt)
             if lh==lbid:
               if lask!=lbid:
                 lba=lbid-lask
                 for ib in range(lba):
                   aks.append('0.0')
  
               if lbidamt!=laksamt:
                 lbb=lbidamt-laksamt
                 for ibb in range(lbb):
                   aaksamt.append('0.0')
             for v in range(len(h)):    
  
               fffd=[racename,h[v],bds[v],aks[v],bbidamt[v],aaksamt[v],v,timetogosec,timetogomin,timestamp,idd,e]
               fffk=[timetogomin,v,h[v],bds[v],aks[v],bbidamt[v],aaksamt[v],timestamp,racename]
   
               finlist.append(fffd)
               klist.append(fffk)
  
               #fst=finlist[0]
               #scd=finlist[1]
         
             self.filt4(finlist)
  
             if '0.0' not in fst and '0.0' not in scd:
               timm=finlist[0][7]
               
               if timm<3660:
                 if flis !=5:
                   fhlis=self.check1(flis,timm)
                   if fhlis !=5:
                     
                     if timm<3660 and timm>1800:
                     
                       fst=finlist[0]
                       scd=finlist[1]
                       listta=self.funfste(fst,scd)
                       if float(fst[2])<1.9:
                         self.filt1(listta)
                 if flis !=5:
                   if flis !=5:
                     
                     if timm>780 and timm<3660:
                       fst=finlist[0]
                       scd=finlist[1]
                       listta=self.funfste(fst,scd)
  
                       self.filt2(listta)
  
                     if timm>300 and timm<960:
                       fst=finlist[0]
                       scd=finlist[1]
                       listta=self.funfste(fst,scd)
  
                       self.filt3(listta)
  
               
               
               
  
             #load.foo2(klist,'see')
           
  
          
           del h[:]
           del bds[:]
           del aks[:]
           del bbidamt[:]
           del aaksamt[:]
           del finlist[:]
           del finlista[:]
           del finlit[:]
           del klist[:]
           #self.checkfinal()
           self.settlevoid()
           self.settledtime()
           print('MODE: ON')
           if os.path.exists('fairlay.txt'):
             with open('fairlay.txt','r') as eedor:
               pkk=json.load(eedor)
               print(pkk)
  # for jl in range(60):
  #   print(jl)
   #  time.sleep(1)
  


  
  
  def foo1(self,lista,chlist):
   #import funuk,stake,load,dump
   target=''
   ckl=[62,72,82,85]
   
   kld=[1.6,0.8,0.4]#1
  
   time1=0
   time2=''
   with open('fairlay.txt','r') as dirr:
     listuk=json.load(dirr)
   stake=listuk['stake']
  
   nam=''
   lite=''
   nam=lista[1][-2]+'-'+lista[1][-1]
   if listuk['lock']<1000:
     if time1==0 and nam not in chlist:
   
       if lista[0][0]>2 and lista[0][0]<5:
         if lista[1][0]-lista[0][0]<2:
           if lista[0][1]<4 or lista[0][1]>7:
             if lista[1][1]<4 or lista[1][1]>7:
               if lista[1][5]<6 or lists[1][5]>7:
                 if lista[1][4]<6 and lista[1][2]>3.7:
                   sit=stake.foo(stake,ckl[int(lista[1][4])-2])
                   if sit[0]< lista[1][7]:
                     target=0
                     	#kld[int(lista[1][4])-3]
                     #target=kld[int(lista[0/1][0])-3])#back
  
                     lite={nam:{'target':target,'status':'lay','state':'open','openodd':[lista[1][6],sit[0],lista[1][8],lista[1][10]],'closeodd':[],'reserved':sit[1]+sit[2]}}
                     listuk['loadp']=lite
                     listuk['lock']+=1
                     listuk['release1'].append(lista[1][11],lista[1][12])
         
                     self.dumpp(listuk)
                     self.addloadp()
                     '''self.placeorder(lista[1][-1][-2],1,1,lista[1][6],sit[0])
                     time.sleep(6)
                     self.checkmatched'''
  
                     
  
  def foo2(self,lista,chlist):
  # import funuk,stake,load,dump
   target=''
   ckl=[62,72,82,85]
  
   kld=[0.65,0.3,0.06]#2*
  
  
   time1=0
   time2=''
   with open('fairlay.txt','r') as dirr:
     listuk=json.load(dirr)
   stake=listuk['stake']
  
  
   nam=''
   lite=''
   nam=lista[1][-2]+'-'+lista[1][-1]
   if listuk['lock']<1000:
     if time1==0 and nam not in chlist:
   
       if lista[0][0]<2 and lista[0][1]>4:
         if lista[1][0]-lista[0][0]<4:
           if lista[1][1]<7 and lista[1][1]>3:
              # if lista[1][5]<3 or lists[1][5]>7:
             if lista[1][0]<6 and lista[1][0]>2:
               sit=stake.foo(stake,ckl[int(lista[1][0])-2])
               if sit[1]< lista[1][3]:
               #target=kld[int(lista[0/1][4])-3])#lay
                 target=0
                 	#kld[int(lista[1][0])-3]#back
  
                 lite={nam:{'target':target,'status':'back','state':'open','openodd':[lista[1][2],sit[1],lista[1][8],lista[1][10]],'closeodd':[],'reserved':sit[0]+sit[2]}}
                 listuk['loadp']=lite
                 listuk['lock']+=1
                 listuk['release1'].append(lista[1][11],lista[1][12])
         
                 self.dumpp(listuk)
  
  
                 self.addloadp()
  
                     
                 '''self.placeorder(lista[1][-1][-2],1,0,lista[1][2],sit[1])
                 time.sleep(6)
                 self.checkmatched
  '''
  
  
  
  def foo3(self,lista,chlist):
   #import funuk,stake,load,dump
   target=''
   ckl=[62,72,82,85]
   
   
   kld=[1.6,0.8,0.4]
  
  
   time1=0
   time2=''
   with open('fairlay.txt','r') as dirr:
     listuk=json.load(dirr)
   stake=listuk['stake']
  
  
   nam=''
   lite=''
   nam=lista[1][-2]+'-'+lista[1][-1]
   if listuk['lock']<1000:
     if time1==0 and nam not in chlist:
   
       if lista[0][0]<2:
         if lista[1][0]-lista[0][0]<6:
           if lista[1][1]<3 or lista[1][1]>7:
             #  if lista[1][5]<3 or lists[1][5]>7:
             if lista[1][0]<7 and lista[1][0]>3:
               sit=stake.foo(stake,ckl[int(lista[1][4])-2])
               if sit[0]< lista[1][7]:
                 target=0
                 	#kld[int(lista[1][4])-3]#lay
                 #target=kld[int(lista[0/1][0])-3])#back
  
                 lite={nam:{'target':target,'status':'lay','state':'open','openodd':[lista[1][6],sit[0],lista[1][8],lista[1][10]],'closeodd':[],'reserved':sit[1]+sit[2]}}
                 listuk['loadp']=lite
                 listuk['lock']+=1
                 listuk['release1'].append(lista[1][11],lista[1][12])
         
                 self.dumpp(listuk)
  
                 #self.dumpp(listuk)
                 self.addloadp()
            
                 #self.placeorder(lista[1][-1][-2],1,1,lista[1][6],sit[0])
                 #time.sleep(6)
                 #self.checkmatched()
  
  
  
  def foo4(self,lista,chlist):
  # import funuk,stake,load,dump
   target=''
   ckl=[62,72,82,85]
   
  
   kld=[0.65,0.3,0.06]#x.9d
  
  
  
   time1=0
   time2=''
   with open('fairlay.txt','r') as dirr:
     listuk=json.load(dirr)
   stake=listuk['stake']
  
   nam=''
   lite=''
   nam=lista[1][-2]+'-'+lista[1][-1]
   if listuk['lock']<1000:
     if time1==0 and nam not in chlist:
     
     
       #if lista[0][0]<5:
  
       if lista[0][0]<5 and lista[0][0]>1:
       
         if lista[1][0]-lista[0][0]<5:
           if lista[0][1]>8 or lista[0][1]<3:
             if lista[1][1]<7 and lista[1][1]>3:
              # if lista[1][5]<3 or lists[1][5]>7:
               if lista[1][0]<7 and lista[1][0]>2:
                 sit=stake.foo(stake,ckl[int(lista[1][0])-2])
                 if sit[1]< lista[1][3]:
                 #target=kld[int(lista[0/1][4])-3])#lay
                   target=0
                   	#kld[int(lista[1][0])-3]#back
  
                   lite={nam:{'target':target,'status':'back','state':'open','openodd':[lista[1][2],sit[1],lista[1][8],lista[1][10]],'closeodd':[],'reserved':sit[0]+sit[2]}}
                   listuk['loadp']=lite
                   listuk['lock']+=1
                   listuk['release1'].append(lista[1][11],lista[1][12])
         
                   self.dumpp(listuk)
                   self.addloadp()
  
                     
                 '''  self.placeorder(lista[1][-1][-2],1,0,lista[1][2],sit[1])
                   time.sleep(6)
                   self.checkmatched
  '''
  
  
  def foo5(self,lista,chlist):
   #import funuk,stake,load,dump
   target=''
   ckl=[62,72,82,85]
   
  
   kld=[1.6,0.8,0.4]#x.4d
  
  
  
   time1=0
   time2=''
   with open('fairlay.txt','r') as dirr:
     listuk=json.load(dirr)
   stake=listuk['stake']
  
   nam=''
   lite=''
   nam=lista[1][-2]+'-'+lista[1][-1]
   if listuk['lock']<1000:
     if time1==0 and nam not in chlist:
   
       if lista[0][0]>1 and lista[0][0]<5:
         if lista[1][0]-lista[0][0]<4:
           if lista[1][1]>8 or lista[1][1]<3:
             if lista[0][1]<7 and lista[0][1]>2:
              # if lista[1][5]<3 or lists[1][5]>7:
               if lista[1][0]<7 and lista[1][0]>3:
                 sit=stake.foo(stake,ckl[int(lista[1][4])-2])
                 if sit[0]< lista[1][7]:
                   target=0
                   	#kld[int(lista[1][4])-3]#lay
                 #target=kld[int(lista[0/1][0])-3])#back
  
                   lite={nam:{'target':target,'status':'lay','state':'open','openodd':[lista[1][6],sit[0],lista[1][8],lista[1][10]],'closeodd':[],'reserved':sit[1]+sit[2]}}
                   listuk['loadp']=lite
                   listuk['lock']+=1
                   listuk['release1'].append(lista[1][11],lista[1][12])
         
                   self.dumpp(listuk)
                   self.addloadp()
  
                     
                 '''  self.placeorder(lista[1][-1][-2],1,1,lista[1][6],sit[0])
                   time.sleep(6)
                   self.checkmatched
  '''
  
  
  
  def foo6(self,lista,chlist):
   #import funuk,stake,load,dump
   target=''
   ckl=[62,72,82,85]
   
   
   kld=[1.6,0.8,0.4]#==1
  
  
   time1=0
   time2=''
  
   with open('fairlay.txt','r') as dirr:
     listuk=json.load(dirr)
   stake=listuk['stake']
  
   nam=''
   lite=''
   nam=lista[1][-2]+'-'+lista[1][-1]
   if listuk['lock']<1000:
     if time1==0 and nam not in chlist:
   
       if lista[0][0]>1 and lista[0][0]<4:
         if lista[1][0]-lista[0][0]==1:
           if lista[0][1]<7 and lista[0][1]>2:
             if lista[1][1]<7 and lista[1][1]>3:
              # if lista[1][5]<3 or lists[1][5]>7:
               if lista[1][0]<6:
                 sit=stake.foo(stake,ckl[int(lista[1][0])-2])
                 if sit[1]< lista[1][3]:
                 #target=kld[int(lista[0/1][4])-3])#lay
                   target=0
                   	#kld[int(lista[1][0])-3]#back
  
                   lite={nam:{'target':target,'status':'back','state':'open','openodd':[lista[1][2],sit[1],lista[1][8],lista[1][10]],'closeodd':[],'reserved':sit[0]+sit[2]}}
                   listuk['loadp']=lite
                   listuk['lock']+=1
                   listuk['release1'].append(lista[1][11],lista[1][12])
         
                   self.dumpp(listuk)
                   self.addloadp()
        
               '''    self.placeorder(lista[1][-1][-2],1,0,lista[1][2],sit[1])
                   time.sleep(6)
                   self.checkmatched
  '''
  
  
  
  '''def foo7(lista,chlist):
  # import funuk,stake,load,dump
   target=''
   ckl=[62,72,82,85]
   time1=0
   time2=''
   with open('fairlay.txt','r') as dirr:
     listuk=json.load(dirr)
   stake=listuk['stake']
  
   nam=''
   lite=''
   nam=lista[1][-2]+'-'+lista[1][-1]
   if listuk['lock']<1000:
     if time1==0 and nam not in chlist:
   
       if lista[0][0]>1 and lista[0][0]<5:
         if lista[1][0]-lista[0][0]==0:
           if lista[0][1]<7 or lista[0][1]>2:
             if lista[1][1]<7 or lista[1][1]>2:
              # if lista[1][5]<3 or lists[1][5]>7:
               if lista[1][5]<6:
                 sit=stake.foo(stake,ckl[int(lista[1][4])-2])
                 if sit[0]< lista[1][7]:
                   lite={nam:{'target':target,'status':'lay','state':'open','openodd':[lista[1][6],sit[0],lista[1][8],lista[1][10]],'closeodd':[],'reserved':sit[1]+sit[2]}}
                   listuk['loadp']=lite
                   listuk['lock']+=1
                   self.dumpp(listuk)
  '''
  
  
  
  def foo8(self,lista,chlist):
   #import funuk,stake,load,dump
   target=''
   ckl=[25,30,35,38,40]
  
   #kld=[4.7,4.1,3.6,3.2]
   kld=[2,4.7,4.1,3.6,3.2]
   
   time1=0
   time2=''
   with open('fairlay.txt','r') as dirr:
     listuk=json.load(dirr)
   stake=listuk['stake']
  
  
   nam=''
   lite=''
   nam=lista[0][-2]+'-'+lista[0][-1]
   if listuk['lock']<1000:
     if time1==0 and nam not in chlist:
   
       if lista[0][0]<2 and lista[0][2]<1.9:
         if lista[1][0]-lista[0][0]<6:
           if lista[1][1]<3 or lista[1][1]>7:
             #  if lista[1][5]<3 or lists[1][5]>7:
             if lista[0][1]>3 and lista[1][0]>3:
               sit=stake.foo(stake,ckl[int(lista[0][0])-4])
               if sit[0]< lista[1][7]:
               #target=kld[int(lista[0/1][4])-3])#lay
                 target=0
                 #	kld[int(lista[0][1])-4]#back
  
                 lite={nam:{'target':target,'status':'back','state':'open','openodd':[lista[0][2],sit[1],lista[0][8],lista[0][10]],'closeodd':[],'reserved':sit[0]+sit[2]}}
                 listuk['loadp']=lite
                 listuk['lock']+=1
                 listuk['release1'].append(lista[0][11],lista[0][12])
         
                 self.dumpp(listuk)
                 self.addloadp()
  
  
               '''  self.placeorder(lista[0][-1][-2],1,0,lista[0][2],sit[1])
                 time.sleep(6)
                 self.checkmatched
  '''



if __name__ == "__main__":
  serverkey= ''
  privatekey= ''
  useridd= ''


  h=''
  pk=''
       
  client = Client(serverkey,privatekey,useridd)


  for gi in range(604800):

    p=str(datetime.datetime.utcnow())
  #print(p)

  #onlydate=dateteste.datetest(p)

    mo=re.compile(r'(\d+):(\d+)')
    ba=mo.findall(p)
    #print(ba[0])
    #print(int(ba[0][0]))
    h=int(ba[0][0])
    if h>10 and h<21:
    
      


      star = client.fetch()
      time.sleep(12)
      #print(star)

    else:
      print('MODE: OFF')
      if os.path.exists('fairlay.txt'):
        with open('fairlay.txt','r') as edor:
          pk=json.load(edor)
          print(pk)
      time.sleep(12)