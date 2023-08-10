# kata_caesars
Caesar Cipher and Caesar Hacker kata

## Installation
Use your preferred package manager for this.  This project is Poetry ready, but if you want to use pip:
```
pip install -r requirements.txt
```

## Running
```
python caesar.py 12 "this is the song that wouldn't end"
python caesar.py --d 12 "ftue ue ftq eazs ftmf iagxpz'f qzp"
python .\hack_caesar.py "ftue ue ftq eazs ftmf iagxpz'f qzp"
```
### `caesar.py`
The KEY for a Caesar cipher is a number between 0 and 26.

To encrypt:
```
python caesar.py KEY "MESSAGE"
```

To decrypt:
```
python caesar.py --d KEY "MESSAGE"
```
### `hack_caesar.py`
Because there are only 26 possible keys in a standard Caesar cipher, the simplest way to crack a message is to simply decrypt it with each possible key and eyeball the results.  That is what the `hack_caesar.py` does.  Example run:

```
python .\hack_caesar.py "ftue ue ftq eazs ftmf iagxpz'f qzp"                      
0: ftue ue ftq eazs ftmf iagxpz'f qzp
1: estd td esp dzyr esle hzfwoy'e pyo
2: drsc sc dro cyxq drkd gyevnx'd oxn
3: cqrb rb cqn bxwp cqjc fxdumw'c nwm
4: bpqa qa bpm awvo bpib ewctlv'b mvl
5: aopz pz aol zvun aoha dvbsku'a luk
6: znoy oy znk yutm zngz cuarjt'z ktj
7: ymnx nx ymj xtsl ymfy btzqis'y jsi
8: xlmw mw xli wsrk xlex asyphr'x irh
9: wklv lv wkh vrqj wkdw zrxogq'w hqg
10: vjku ku vjg uqpi vjcv yqwnfp'v gpf
11: uijt jt uif tpoh uibu xpvmeo'u foe
12: this is the song that wouldn't end
13: sghr hr sgd rnmf sgzs vntkcm's dmc
14: rfgq gq rfc qmle rfyr umsjbl'r clb
15: qefp fp qeb plkd qexq tlriak'q bka
16: pdeo eo pda okjc pdwp skqhzj'p ajz
17: ocdn dn ocz njib ocvo rjpgyi'o ziy
18: nbcm cm nby miha nbun qiofxh'n yhx
19: mabl bl max lhgz matm phnewg'm xgw
20: lzak ak lzw kgfy lzsl ogmdvf'l wfv
21: kyzj zj kyv jfex kyrk nflcue'k veu
22: jxyi yi jxu iedw jxqj mekbtd'j udt
23: iwxh xh iwt hdcv iwpi ldjasc'i tcs
24: hvwg wg hvs gcbu hvoh kcizrb'h sbr
25: guvf vf gur fbat gung jbhyqa'g raq
26: ftue ue ftq eazs ftmf iagxpz'f qzp
```
You can see that key 12 results in the proper output.

