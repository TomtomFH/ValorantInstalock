import customtkinter #line:1
import json ,time #line:2
import requests #line:3
from valclient .client import Client #line:4
import os #line:5
import sys #line:6
import psutil #line:7
data ={"ran":False ,"region":"","hoverDelay":0 ,"lockDelay":0 ,"loopDelay":5 ,"agents":{"Jett":"add6443a-41bd-e414-f6ad-e58d267f4e95","Reyna":"a3bfb853-43b2-7238-a4f1-ad90e9e46bcc","Raze":"f94c3b30-42be-e959-889c-5aa313dba261","Yoru":"7f94d92c-4234-0a36-9646-3a87eb8b5c89","Phoenix":"eb93336a-449b-9c1b-0a54-a891f7921d69","Neon":"bb2a4828-46eb-8cd1-e765-15848195d751","Breach":"5f8d3a7f-467b-97f3-062c-13acf203c006","Skye":"6f2a04ca-43e0-be17-7f36-b3908627744d","Sova":"320b2a48-4d9b-a075-30f1-1f93a9b638fa","KAY/O":"601dbbe7-43ce-be57-2a40-4abd24953621","Killjoy":"1e58de9c-4950-5125-93e9-a0aee9f98746","Cypher":"117ed9e3-49f3-6512-3ccf-0cada7e3823b","Sage":"569fdd95-4d10-43ab-ca70-79becc718b46","Chamber":"22697a3d-45bf-8dd7-4fec-84a9e28c69d7","Omen":"8e253930-4c05-31dd-1b6c-968525494517","Brimstone":"9f0d8ba9-4140-b941-57d3-a7ad57c6b417","Astra":"41fb69c1-4189-7b37-f117-bcaf1e96f1bf","Viper":"707eab51-4836-f488-046a-cda6bf494859","Fade":"dade69b4-4f5a-8528-247b-219e5a1facd6","Harbor":"95b78ed7-4637-86d9-7e41-71ba8c293152","Gekko":"e370fa57-4757-3604-3648-499e1f642d3f","Deadlock":"cc8b64c8-4b25-4ff9-6e7f-37b4da43d235"},"maps":{"ascent":None ,"duality":None ,"foxtrot":None ,"canyon":None ,"triad":None ,"port":None ,"pitt":None ,"bonsai":None ,"jam":None ,"hurm_alley":None ,"hurm_bowl":None ,"hurm_yard":None ,"juliett":None },"codes":{"ascent":"Ascent","duality":"Bind","foxtrot":"Breeze","canyon":"Fracture","triad":"Haven","port":"Icebox","pitt":"Pearl","bonsai":"Split","jam":"Lotus","hurm_alley":"District","hurm_bowl":"Kasbah","hurm_yard":"Piazza","juliett":"Sunset"},"playedRounds":0 }#line:70
requirements ="""@echo off
pip install customtkinter
pip install pytube
pip install requests==2.26.0
pip install urllib3==1.26.6
pip install Colr~=0.9.1
pip install websocket-server==0.6.0
pip install websockets==10.3
pip install inquirerpy==0.3.4
pip install pypresence==4.2.1
pip install nest_asyncio==1.5.5
pip install rich==12.5.1
pip install socket
pip install pycryptodome
cls
if exist Valorant-Instalocker.exe start Valorant-Instalocker.exe
if exist Valorant-Instalocker.py start Valorant-Instalocker.py
if exist main.py start main.py
"""#line:89
def is_valorant_running ():#line:91
    for O00OO0OOOO0OO0O0O in psutil .process_iter (['name']):#line:92
        if O00OO0OOOO0OO0O0O .info ['name']=='VALORANT.exe':#line:93
            return True #line:94
    return False #line:95
if is_valorant_running ():#line:97
    print ("Valorant is open")#line:98
else :#line:99
    print ("Open Valorant first dumbass")#line:100
    time .sleep (10 )#line:101
    sys .exit ()#line:102
VERSION =1.1 #line:104
valid =False #line:105
running =True #line:106
start =False #line:107
seenMatches =[]#line:108
def updateCheck (OO0000O0O0O00OO00 ):#line:110
    print ("Checking For Updates")#line:111
    OOOO0O000O00000O0 ="https://pastebin.com/raw/G4A7JSY4"#line:112
    O0O0000OO0O0O00OO =requests .get (OOOO0O000O00000O0 )#line:113
    if O0O0000OO0O0O00OO .status_code ==200 :#line:115
        O0000O0O00000O0O0 =O0O0000OO0O0O00OO .text .strip ()#line:116
        try :#line:118
            O0000O0O00000O0O0 =float (O0000O0O00000O0O0 )#line:119
            if O0000O0O00000O0O0 >OO0000O0O0O00OO00 :#line:121
                OOOO000000O0OOOO0 =f"You are using version {OO0000O0O0O00OO00}. Please update to {O0000O0O00000O0O0}. " f"https://github.com/TomtomFH/ValorantInstalock/releases"#line:123
                print (OOOO000000O0OOOO0 )#line:124
                time .sleep (30 )#line:125
                sys .exit ()#line:126
            else :#line:127
                print ("You have the latest version.")#line:128
        except ValueError :#line:129
            print ("Invalid version number in remote code.")#line:130
    else :#line:131
        print ("Failed to fetch latest version")#line:132
updateCheck (VERSION )#line:134
customtkinter .deactivate_automatic_dpi_awareness ()#line:136
def save_data ():#line:138
    print ("Saving")#line:139
    with open ("data.json","w")as OOOOOO00O0OO0OO00 :#line:140
        data ["maps"]=maps #line:141
        data ["ran"]=True #line:142
        data ["region"]=region #line:143
        data ["playedRounds"]=playedRounds #line:144
        json .dump (data ,OOOOOO00O0OO0OO00 )#line:145
        print ("Saved")#line:146
loopDelay =5 #line:148
lockDelay =0 #line:149
hoverDelay =0 #line:150
maps ={}#line:151
agents ={}#line:152
mapCodes ={}#line:153
region ="na"#line:154
playedRounds =0 #line:155
client =Client (region =region )#line:156
def add_map_options (OOO0O0OO0O0000O00 ,OO0O00O0O00OOO00O ,OO000000000OOOOO0 ,O00OO00OO00O00O0O ,O00OO000O00OO000O ):#line:158
    O00000O0O0000O0O0 =["none"]+list (O00OO00OO00O00O0O .keys ())#line:159
    OO0O0O0000OO0OO00 =customtkinter .CTkLabel (app ,text =O00OO000O00OO000O [OO0O00O0O00OOO00O ])#line:160
    OO0O0O0000OO0OO00 .grid (column =0 ,row =OOO0O0OO0O0000O00 +3 )#line:161
    O0000OOO0O00OOOOO =customtkinter .CTkOptionMenu (app ,values =O00000O0O0000O0O0 )#line:162
    O0000OOO0O00OOOOO .grid (column =1 ,row =OOO0O0OO0O0000O00 +3 ,padx =1 ,pady =1 )#line:163
    OOOOO0O0OO0O0OO0O ="none"#line:164
    if OO0O00O0O00OOO00O in OO000000000OOOOO0 and OO000000000OOOOO0 [OO0O00O0O00OOO00O ]is not None and "agent"in OO000000000OOOOO0 [OO0O00O0O00OOO00O ]:#line:165
        OOOOO0O0OO0O0OO0O =OO000000000OOOOO0 [OO0O00O0O00OOO00O ]["agent"]#line:166
    OOO0000OO0O00O00O =customtkinter .StringVar (value =OOOOO0O0OO0O0OO0O )#line:167
    def OO00OOO0OO00O0O00 (O0O0O0OOOOOO0O0OO ):#line:168
        if O0O0O0OOOOOO0O0OO in O00OO00OO00O00O0O .keys ():#line:169
            OO000000000OOOOO0 [OO0O00O0O00OOO00O ]={"agent":O0O0O0OOOOOO0O0OO ,"key":O00OO00OO00O00O0O [O0O0O0OOOOOO0O0OO ]}#line:170
            print ("Selected Agent",O0O0O0OOOOOO0O0OO .capitalize (),"for the Map",O00OO000O00OO000O [OO0O00O0O00OOO00O ].capitalize ())#line:171
        elif O0O0O0OOOOOO0O0OO =="none":#line:172
            OO000000000OOOOO0 [OO0O00O0O00OOO00O ]=None #line:173
        else :#line:174
            print ("Invalid Agent")#line:175
    O0000OOO0O00OOOOO .configure (command =OO00OOO0OO00O0O00 ,variable =OOO0000OO0O00O00O )#line:177
def MainProgram ():#line:179
    global loopDelay #line:180
    global lockDelay #line:181
    global hoverDelay #line:182
    global maps #line:183
    global mapCodes #line:184
    global region #line:185
    global playedRounds #line:186
    global save_data #line:187
    O0000O00000OOO00O =Client (region =region )#line:188
    try :#line:189
        O0000O00000OOO00O .activate ()#line:190
    except Exception as O000OOO000O00O00O :#line:191
        print ("Open Valorant first dumbass")#line:192
    os .system ("cls")#line:193
    print ("Waiting for Agent Select")#line:194
    while running :#line:196
        time .sleep (loopDelay )#line:197
        try :#line:198
            OOO0OOOOO0OO00000 =O0000O00000OOO00O .fetch_presence (O0000O00000OOO00O .puuid )["sessionLoopState"]#line:199
            OOOO0O00OOOOOOOO0 =O0000O00000OOO00O .pregame_fetch_match ()["ID"]#line:200
            if OOO0OOOOO0OO00000 =="PREGAME"and OOOO0O00OOOOOOOO0 not in seenMatches :#line:202
                seenMatches .append (OOOO0O00OOOOOOOO0 )#line:203
                O0O0OOO000O0000O0 =O0000O00000OOO00O .pregame_fetch_match (OOOO0O00OOOOOOOO0 )#line:204
                O0O00000O00O00O00 =O0O0OOO000O0000O0 ["MapID"].split ("/")[-1 ].lower ()#line:205
                OOOO00OO0O000OO0O =(lambda OO0O000OO0OO0OO00 :"Defending"if OO0O000OO0OO0OO00 =="Blue"else "Attacking")#line:208
                with open ("data.json","r")as OOO00000OOO00OO00 :#line:209
                    O00O0O0OOOOO000O0 =json .load (OOO00000OOO00OO00 )#line:210
                playedRounds =playedRounds +1 #line:211
                save_data ()#line:212
                os .system ("cls")#line:213
                print ("----------------------")#line:214
                print (f"       Match {playedRounds}")#line:215
                print ("  Agent Select Found")#line:216
                print (f"{mapCodes[O0O00000O00O00O00].capitalize()} - "+OOOO00OO0O000OO0O (O0O0OOO000O0000O0 ["Teams"][0 ]["TeamID"])+" first")#line:217
                if maps [O0O00000O00O00O00 ]!=None :#line:218
                    time .sleep (hoverDelay )#line:219
                    O0000O00000OOO00O .pregame_select_character (maps [O0O00000O00O00O00 ]["key"])#line:220
                    time .sleep (lockDelay )#line:221
                    O0000O00000OOO00O .pregame_lock_character (maps [O0O00000O00O00O00 ]["key"])#line:222
                    print ("  Agent Locked - "+list (agents .keys ())[list (agents .values ()).index (maps [O0O00000O00O00O00 ]["key"])].capitalize ())#line:223
                    print ("----------------------")#line:224
        except Exception as O000OOO000O00O00O :#line:226
            if "pre-game"not in str (O000OOO000O00O00O ):#line:227
                print ("An error occurred:",O000OOO000O00O00O )#line:228
def run ():#line:230
    global start #line:231
    start =True #line:232
    global app #line:233
    app .destroy ()#line:234
def MainUI (O0OOO0OO0O00OOO00 ):#line:236
    global loopDelay #line:237
    global lockDelay #line:238
    global hoverDelay #line:239
    global maps #line:240
    global agents #line:241
    global start #line:242
    global mapCodes #line:243
    global playedRounds #line:244
    global data #line:245
    if not os .path .exists ("requirements.bat"):#line:246
        with open ("requirements.bat","w")as OOO00OOOOOOOO00O0 :#line:247
            OOO00OOOOOOOO00O0 .write (requirements )#line:248
            print ("requirements.bat created")#line:249
    if not os .path .exists ("data.json"):#line:250
        with open ("data.json","w")as OOO00OOOOOOOO00O0 :#line:251
            json .dump (data ,OOO00OOOOOOOO00O0 )#line:252
            print ("data.json created")#line:253
    with open ("data.json","r")as OOO00OOOOOOOO00O0 :#line:255
        global save_data #line:256
        data =json .load (OOO00OOOOOOOO00O0 )#line:257
        agents =data ["agents"]#line:258
        maps =data ["maps"]#line:259
        O000OOO0000OO0O00 =data ["ran"]#line:260
        mapCodes =data ["codes"]#line:261
        OO00000O00OO00O0O =data ["region"]#line:262
        hoverDelay =data ["hoverDelay"]#line:263
        lockDelay =data ["lockDelay"]#line:264
        loopDelay =data ["loopDelay"]#line:265
        playedRounds =data ["playedRounds"]#line:266
        if not O000OOO0000OO0O00 :#line:268
            print ("First time running script")#line:269
            print ("Installing requirements")#line:270
            os .startfile ('requirements.bat')#line:271
            O000OOO0000OO0O00 =True #line:272
            save_data ()#line:273
            sys .exit ()#line:274
        customtkinter .set_appearance_mode ("System")#line:276
        customtkinter .set_default_color_theme ("dark-blue")#line:277
        O000O0OO0O0OO0OO0 =customtkinter .CTkLabel (O0OOO0OO0O00OOO00 ,text ="Valorant Instalock Script by TomtomFH")#line:279
        O000O0OO0O0OO0OO0 .grid (row =0 ,column =0 ,columnspan =2 )#line:280
        O0O00OO00OOO000OO =customtkinter .CTkLabel (O0OOO0OO0O00OOO00 ,text ="Region")#line:282
        O0O00OO00OOO000OO .grid (row =1 ,column =0 ,columnspan =2 )#line:283
        OO0000O0OOO000OO0 =customtkinter .CTkOptionMenu #line:285
        def O0000O0OO0O0OOO00 (OOO0O0OOOO0000O00 ):#line:287
            global region #line:288
            region =OOO0O0OOOO0000O00 #line:289
            print ("Region selected:",OOO0O0OOOO0000O00 )#line:290
        O000O00OOOO0O0000 =customtkinter .StringVar (value =OO00000O00OO00O0O )#line:292
        OO0000O0OOO000OO0 =customtkinter .CTkOptionMenu (O0OOO0OO0O00OOO00 ,values =["eu","na","latam","br","ap","kr","pbe"],command =O0000O0OO0O0OOO00 ,variable =O000O00OOOO0O0000 ,)#line:298
        OO0000O0OOO000OO0 .grid (row =2 ,column =0 ,columnspan =2 ,padx =10 ,pady =10 )#line:299
        O0O0OOO00OO0O0O00 =0 #line:301
        for OO0OOOOOO0OO0OO00 in maps .keys ():#line:302
            add_map_options (O0O0OOO00OO0O0O00 ,OO0OOOOOO0OO0OO00 ,maps ,agents ,mapCodes )#line:304
            O0O0OOO00OO0O0O00 =O0O0OOO00OO0O0O00 +1 #line:305
        O000O0O00O0OO00O0 =customtkinter .CTkButton (O0OOO0OO0O00OOO00 ,text ="Start",command =run ,fg_color ="#009933")#line:307
        O000O0O00O0OO00O0 .grid (row =O0O0OOO00OO0O0O00 +3 ,column =0 ,columnspan =2 ,padx =10 ,pady =10 )#line:308
app =customtkinter .CTk ()#line:310
app .title ("Valorant Instalock script by TomtomFH")#line:311
MainUI (app )#line:312
app .mainloop ()#line:313
while True :#line:315
    time .sleep (1 )#line:316
    if start :#line:317
        start =False #line:318
        save_data ()#line:319
        print ("Starting")#line:320
        MainProgram ()
