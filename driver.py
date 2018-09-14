from functions import*
from xclWriter import*

#array of all the urls used
#0: alighten (1)
#1: alighten (2)
#2: alighten ()
#3: arisen
#4: awaken
#5: baken
#6: barken (1)
#7: barken (2)
#8: be
#9: bear
#10 beat
#11 become
#12 befolen not sure if this is the correct word
#13 begin
#14 begin (2)
#15 behold
#16 bellow
#17 bend (1)
#18 bend (2)
#19 beset
#20 bid
#21 bide
#22 bind
#23 bite
#24 bleed
# blend
#25 bow
#26 braid
#27 break
#28 breed
#29 brew
#30 bring
#31 build
#32 burn
#33 burst
#34 buy
#35 carve
#36 cast
#37 catch
#38 chew
#39 chide
#40 choose
#41 cleave
#42 climb
#43 cling
#44 come
#45 creep
#46 cringe
#47 crow
#48 cut
#49 dare
#50 deal
#51 delve
#52 dig
#53 dive
#54 do
#55 drag
#56 draw
#57 dream
#58 drink
#59 drip
#60 drive
#61 dwell
#62 eat
#63 fall
#64 fare
#65 feed
#66 feel
#67 fight
#68 find
#69 flay
#70 flee
#71 fling
#72 float
#73 fly
#74 fold
#75 forbid
#76 foretell
#77 forget
#78 forgo
#79 forsake
#80 freeze
#81 get
#82 give
#83 glide
#84 gnaw
#85 go
#86 grind
#87 grip (1)
#88 grip (2)
#89 grow
#90 hang
#91 have
#92 hear
#93 heave
#94 help
#95 hew
#96 hide
#97 hit
#98 hold
#99 hurt
#100 keep
#101 knead
#102 kneel
#103 knit
#104 know
#105 lead
#106 leap
#107 leave
#108 lend
#109 let
#110 lie (1)
#111 lie (2)
#112 light
#113 lock
#114 lose
#115 low
#116 make
#117 mean
#118 meet
#119 melt
#120 mislead
#121 mistake
#122 mourn
#123 plead
#124 prove
#125 put
#126 quit
#127 reach
#128 read
#129 reckon
#130 redden
#131 reek
#132 rend
#133 ride
#134 ring
#135 rise
#136 rue
#137 run
#138 rush
#139 say
#140 scrape
#141 see
#142 seek
#143 seethe
#144 sell
#145 send
#146 set
#147 shake
#148 shape
#149 shear
#150 shed
#151 shine
#152 shot
#153 shove
#154 show
#155 shrink
#156 shrive
#157 shut
#158 sigh
#159 sing
#160 sink
#161 sit
#161 slay
#162 sleep
#162 slide
#163 sling
#164 slink
#165 slip
#166 slit
#167 smite
#168 smoke
#169 sow
#170 speak
#171 speed
#172 spend
#173 spew
#174 spill
#175 spin
#176 split
#177 spread
#178 spring
#179 spurn
#180 stand
#181 starve
#182 steal
#183 step
#184 stick
#185 sting
#186 stink
#187 stretch
#188 strew
#189 stride
#190 strike
#191 string
#192 strive
#193 stroke
#194 suck
#195 sup
#196 swallow
#197 swear
#198 sweep
#199 swell
#200 swim
#201 swing
#202 take
#203 teach
#204 tear
#205 tell
#206 think
#207 throw
#208 thrust
#209 tread
#210 undergo
#211 understand
#212 upset
#213 wade
#214 wake
#215 walk
#216 wash
#217 warp
#218 wax
#219 wear
#220 weave
#221 wed
#222 weep
#223 weigh
#224 wet
#225 weld
#226 win
#227 wind
#228 withdraw
#229 withstand
#230 work
#231 wreak
#232 wring
#233 write
#234 writhe

urlArr = [
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED1123&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED1124&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED1127&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED2240&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED3233&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED3485&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED3677&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED3678&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4048&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4156&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4268&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED3910&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4371&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED852&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED18604&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4527&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4022&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4061&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4062&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4790&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4381&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4389&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4667&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4931&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED5144&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED5166&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED5755&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED5900&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED5908&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED5882&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED5973&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED6058&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4579&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4579&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED5928&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED5948&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED4411&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED24186&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED6914&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED6442&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED7513&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED7543&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED7483&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED8013&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED8034&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED8040&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED8522&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED9897&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED10271&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=byte&byte=36271184&egdisplay=compact&egs=36272419",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED9018&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED9266&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED12843&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED10945&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED11004&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED11609&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED12227&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED12367&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED12515&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED12537&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED12576&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED12654&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED12659&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED12668&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED12880&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED14578&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED15195&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED15284&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED15435&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED15520&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED15910&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED16004&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED16246&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED16271&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED16346&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED16407&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED16330&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED16538&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED16659&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED16889&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED17373&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED16958&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED17117&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED17695&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED17715&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED18489&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED53944&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED18785&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED18915&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED19078&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED19487&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED19500&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED19503&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED19597&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED21130&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED20173&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED20505&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED20701&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED20336&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED20684&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED20739&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED20906&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED20995&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED21544&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED24173&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED24400&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED24407&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED24435&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED24477&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED24960&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED25161&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED25339&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED25108&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED25257&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED25443&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED25444&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED25503&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED25943&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED26122&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED26188&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED26584&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED27327&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED27563&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED27266&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED27780&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED28140&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED28266&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED28664&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED33646&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED34581&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED35369&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED35686&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED36168&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED36308&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED36605&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED36309&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED36604&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED36764&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED37470&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED37595&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED37645&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED37273&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED36797&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED38146&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39209&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39021&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39393&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39128&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39635&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39312&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39404&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39654&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39745&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39782&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39893&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39826&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39953&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39905&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED40083&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39916&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED40132&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED40134&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED39905&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED40236&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED40448&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED40475&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED40572&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED40820&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED40832&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED40868&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED40897&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED40900&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED40910&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED40918&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED41102&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED41118&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED41215&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED41779&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42083&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42062&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42116&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42177&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42211&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42225&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42285&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42397&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42428&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42467&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED43062&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42877&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42759&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42814&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42939&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42971&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED42975&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED43228&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED43328&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED43338&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED43351&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED43289&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED43365&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED43378&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED41787&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED41832&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED44301&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED44145&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED44139&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED44109&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED44240&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED44253&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED44420&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED44633&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED44887&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED44693&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED45310&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED45567&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED45474&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED46887&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED48255&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED48362&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED50517&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED51479&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED51544&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED51581&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED51841&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED52306&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED51942&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED52256&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED52404&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED51968&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED52223&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED52021&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED52388&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED52094&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED52917&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED52864&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED53018&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED53147&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED52280&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED53617&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED53673&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED53691&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED53808&egs=all&egdisplay=open",
"https://quod.lib.umich.edu/cgi/m/mec/med-idx?type=id&id=MED53804&egs=all&egdisplay=open",
]

wb = xlwt.Workbook()
ws = wb.add_sheet("sheet 1")


for i in range(0,len(urlArr)):
    foo = main(urlArr[i])
    #write the headwords
    ws.write(0,i,returnHeadWord(urlArr[i]))

    #write the citations
    for j in range(len(foo)):
        ws.write(j+2,i,foo[j])
        print(foo[j])

wb.save("words.xls")

#addValue(0,0,str)
#printArr(main(urlArr[0:10]))
