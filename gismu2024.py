import os
import json
from fastDamerauLevenshtein import damerauLevenshtein

def validate(word):
	if word[-1] in "ptcl":
		return ""
	#if not "a" in word:
	#	return ""
	#aspot=word.find("a")
	#if ("i" in word[:aspot]) or ("u" in word[:aspot]):
	#	return ""
	#if (word[aspot+1:]+" ")[0] in "aiu":
	#	return ""
	word=word.replace("an","aN").replace("in","iN").replace("un","uN")
	word=word.replace("na","Na").replace("ni","Ni").replace("nu","Nu")
	for forb in ["pp","cc","lp","lt","lc","lN","ll","n"]:
		if forb in word:
			return ""
	word=word.replace("N","n")
	return word

def calc(word):
	#print(word,end="\t")
	for v in "aiu":
		word=word.replace(v,v+".")
	if not word[-1]==".":
		word+="."
	#return len(word)
	for c1 in "ptcln":
		for c2 in "ptcln":
			word=word.replace(c1+c2,c1+"."+c2)
			word=word.replace(c1+c2,c1+"."+c2)
	for v in "aiu":
		word=word.replace(v+".n.",v+"n.")

	word=word.replace("a.i","aj")
	word=word.replace("a.u","aw")
	word=word.replace("u.i","oj")

	for v2 in "aiu":
		word=word.replace("ni."+v2,"nj"+v2)
		for v1 in "aiu":
			word=word.replace(v1+".i."+v2,v1+".j"+v2)


	for v2 in "aiu":
		for c in "ptcln":
			word=word.replace(c+"u."+v2,c+"w"+v2)
		for v1 in "aiu":
			word=word.replace(v1+".u."+v2,v1+".w"+v2)

	word=word.replace("t.l","tr")
	word=word.replace("p.l","pl")
	word=word.replace("c.l","cl")
	word=("0"+word).replace("0t.","0s")[1:]
	word=word.replace("a.t.","a.s")
	word=word.replace("i.t.","i.s")
	word=word.replace("u.t.","u.s")
	for c in "pct":
		for v in "aiu.":
			word=word.replace(c+".t"+v,c+"θ"+v)
	#0/0
	#print(word)
	aPos=word.find("a")
	if word[aPos+1]=="n" and word[aPos+2]==".":
		return len(word)*2-1
	if aPos>1 and word[aPos-1]=="l":
		if not word[aPos-2]=="t":
			return len(word)*2+1
	return len(word)*2

def VSimp(word):
	word="="+word
	oldWord=""
	while not oldWord == word:
		oldWord=word
		for c in "ptcln":
			word=word.replace("="+c,c+"=")

	word=word.replace("=","a=")

	oldWord=""
	while not oldWord == word:
		oldWord=word
		for c in "aiu":
			word=word.replace("="+c,"=")
	return word.replace("=","")

def tryAdd(array, word):
	word=validate(word)
	if not word=="":
		array.append(word)

maywords=[]
for p1 in "ptclnaiu":
	for p2 in "ptclnaiu":
		print(p1+p2,len(maywords))
		for p3 in "ptclnaiu":
			for p4 in "ptclnaiu":
				for p5 in "ptclnaiu":
					for p6 in "ptclnaiu":
						for p7 in "ptclnaiu":
							for p8 in "ptclnaiu":
								#for p9 in "ptclnaiu":
								#	for p10 in "ptclnaiu":
								#		tryAdd(maywords,p1+p2+p3+p4+p5+p6+p7+p8+p9+p10)
								#	tryAdd(maywords,p1+p2+p3+p4+p5+p6+p7+p8+p9)
								tryAdd(maywords,p1+p2+p3+p4+p5+p6+p7+p8)
							tryAdd(maywords,p1+p2+p3+p4+p5+p6+p7)
						tryAdd(maywords,p1+p2+p3+p4+p5+p6)
					tryAdd(maywords,p1+p2+p3+p4+p5)
				tryAdd(maywords,p1+p2+p3+p4)
			tryAdd(maywords,p1+p2+p3)
		tryAdd(maywords,p1+p2)
	tryAdd(maywords,p1)

minnedExclusion={}
forms={}
got=0
for p1 in maywords:
	word=validate(p1)
	simped=VSimp(word)
	if not word=="":
		score=len(word)#calc(word)
		if not score in forms:
			forms[score]=[]
		forms[score].append(word)
		got+=1
		if got%10000==0:
			print(got,word)
		
		scoreSimped=len(simped)#calc(word)
		if not scoreSimped in minnedExclusion:
			minnedExclusion[scoreSimped]={}
		minnedExclusion[scoreSimped][simped]=0
	#else:
	#	print(p1)

allSum=0
allSumSimp=0
for i in range(200):
	i+=1
	if i in forms:
		allSum+=len(forms[i])
		allSumSimp+=len(minnedExclusion[i])
		print(i,len(forms[i]),len(minnedExclusion[i]),len(minnedExclusion[i])/len(forms[i]),forms[i][0],allSum,allSumSimp,allSumSimp/allSum)
#0/0

i=0
#refWords={
#	"pantluci":{
#		"tok":["pansuki"],
#		"jbo":["pancruki"],
#		"eng":["pæntʃɹuki"],
#	},
##0 159154 i the me i'm my myself mine i've i'll mi i'd im ive id we a us ourselves ourself our ours we're we've we'll an 
#	"we(incl)":{
#		"tok":["mi","mi en sina","sina en mi","mi e sina","sina e mi"],
#		"jbo":["ma'a","mi'o"],
#		"eng":["wi","əs","aʊɚsɛlvz","aʊɚsɛlf","aʊɚz","aʊɚ"],
#		
#		#"tok":["mi"],"jbo":["mi'o"],"eng":["wi"]
#	},
#	#second so that it can get "a"
#	"i/we(excl)":{
#		"tok":["mi"],
#		"jbo":["ma'a","mi","mi'a","mi'o"],
#		"eng":["aɪ","mi","maɪsɛlf","maɪn","maɪ","wi","əs","aʊɚsɛlvz","aʊɚsɛlf","aʊɚz","aʊɚ"],
#		
#		#"tok":["mi"],"jbo":["mi"],"eng":["aɪ"]
#	},
#	#"we(imp)":{
#	#	"tok":["mi o"],
#	#	"jbo":["ma'a ko'oi","mi'o ko'oi",
#	#	"mi e ko","ko e mi","ma'a e ko","ko e ma'a","mi'o e ko","ko e mi'o",
#	#	"mi je ko","ko je mi","ma'a je ko","ko je ma'a","mi'o je ko","ko je mi'o",
#	#	],
#	#	"eng":["lɛts","lɛt əs"],
#	#	#"tok":["mi o"],"jbo":["mi e ko"],"eng":["lɛts","lɛt əs"]
#	#},
##1 83150 it he him himself his hes he's she her herself shes she's itself its it's they them themself themselves theirs their they're it'll it'd that'd they'd they'll ni ona that there this that's there's thats theres
#	"it":{
#		"tok":["ona","ni"],
#		"jbo":["fo'a","fo'e","fo'i","fo'o","fo'u","ko'a","ko'e","ko'i","ko'o","ko'u","ra","ri","ru","ta","ti","tu","vo'a","vo'e","vo'i","vo'o","vo'u"],
#		"eng":["hi","hɪm","hɪmsɛlf","hɪz", "ʃi","hɝ","hɝsɛlf","hɝz","ɪt","ɪtsɛlf","ɪts","ðeɪ","ðɛm","ðɛmsɛlvz","ðɛmsɛlf","ðɛɚz","ðɛɚ","wən","wənsɛlf","wənz","ðɪs","ðæt"],
#		
#		#"tok":["ni"],"jbo":["ti"],"eng":["ʃi"]
#	},
##2 51377 is am was were are be being been exist exists 
#	"is":{
#		"tok":["li","sama"],
#		"jbo":["cu","du"],
#		"eng":["bi","æm","wəz","ɑɹ","wɝ","ɪz","biɪŋ","bɛn","ɛɡzɪst"],
#		
#		#"tok":["li"],"jbo":["du"],"eng":["bi"]
#	},
##3 37932 you your yourself yourselves yours you're thou thee thyself thine thy yall ya'll ya'll's you've you'd y'all you'll u youre 
#	"you":{
#		"tok":["sina"],
#		"jbo":["do","do'o"],
#		"eng":["ju","jɔɹsɛlf","jɔɹz","jɔɹ","jɔɹsɛlvz","jɔl","jɔlz"],
#		
#		#"tok":["sina"],"jbo":["do"],"eng":["jɔl"]
#	},
#	"you(imp)":{
#		"tok":["o","sina o"],
#		"jbo":["ko","do ko'oi","do'o ko'oi","ma'a ko'oi","mi'o ko'oi"],
#		"eng":["ju bɛɾɚ", "jud bɛɾɚ", "ju hæd bɛɾɚ", "jud bɛst", "ju hæd bɛst", "juv ɡɑɾə", "juv ɡɑt tu","kæn ju","kʊd ju","wʊd ju","ju mʌst"],
#	},
##4 35716 in if during around when on at 
#	"in":{
#		"tok":["lon","la"],
#		"jbo":["ca","bu'u","zvati","cabna","judri"],
#		"eng":["ɪf","dɜɹɪŋ","əɹaʊnd","wɪn","ɑn","æt","ɪn"]
#	},
##5 33742 not isn't don't no can't doesn't aren't wouldn't haven't didn't won't wasn't shouldn't couldn't hasn't weren't isnt dont nah non doesnt nope cant 
#	"not":{
#		"tok":["ala"],
#		"jbo":["natfe","na","na'e","na'i","nai"],
#		"eng":["ɪzənt","ɪznt","nɑt","doʊnt","noʊ","dʌzənt","ɑɹnt","ɑɹənt","wʊdnt","hævnt","nɑ","noʊp"]
#	},
##6 30823 and but 
#	"and":{
#		"tok":["li","en","e","lon poka"],
#		"jbo":["kanxe","bi'i","ce","e","ge","gi'e","gu'e","je","joi"],
#		"eng":["ænd","ən","n","bʌt"]
#	},
##7 30519 to toward towards 
#	"to":{
#		"tok":["tawa"],
#		"jbo":["farna","fa'a"],
#		"eng":["tu","æt","tʊwɔɹdz","tɔɹdz","toʊɚdz"]
#	},
##8 28229 use uses using used for help with how how's helps helping 
#	"help":{
#		"tok":["kepeken","tan","nasin","ilo"],
#		"jbo":["pilno","pi'o","va'u","sidju"],
#		"eng":["juz","fɔɹ","hɛlp","wɪθ","haʊ"]
#	},
##9 20580 like as likes 
#	"similar":{
#		"tok":["sama"],
#		"jbo":["simsa","si'a","ckini"],
#		"eng":["laɪk","æz","ʌkɪn","sɪməlɚ"]
#	},
##10 19868 of from 
#	"of":{
#		"tok":["tan"],
#		"jbo":["ra'i","zei"],
#		"eng":["ʌv","ə","fɹʌm","s"]
#	},
##11 19012 make makes making made do does doing did 
#	"do":{
#		"tok":["pali"],
#		"jbo":["gasnu","zbasu"],
#		"eng":["meɪk","meɪd","du","dɪd"]
#	},
##12 16367 yes go'i yeah sure yee agree very yup really agreed real actual 
#	"real":{
#		"tok":["lon"],
#		"jbo":["go'i","tugni","mutce","je'a","ja'a","jo'a"],
#		"eng":["jɛs","jɛ","jɛə","ʃʊɹ","ji","əɡɹi","vɛɹi","jʌp","ɹɪli","ɹɪəli","ɹil","ɹijəl","æktʃuəl"]
#	},
##13 13990 so therefore because 
#	"therefore":{
#		"tok":["tan","la"],
#		"jbo":["ja'e","ki'u","mu'i","ni'i","ri'a"],
#		"eng":["soʊ","ðɛɚfɔɹ","bikɔz"]
#	},
##14 13496 have having has had 
#	"have":{
#		"tok":["jo","lon insa"],
#		"jbo":["tolcau","ponse","ralte"],
#		"eng":["hæv","hæz","hæd"]
#	},
##15 10623 thing things something anything stuff stuffs co'e 
#	"something":{
#		"tok":["ijo"],
#		"jbo":["da","de","di","co'e"],
#		"eng":["θɪŋ","sʌmθɪŋ","stʌf"]
#	},
##16 9933 just 
##UIVLA
##17 9496 well good pona great 
#	"good":{
#		"tok":["pona"],
#		"jbo":["xamgu","kanro","vrude"],
#		"eng":["wɛl","ɡʊd","ɡɹeɪt","bɛɾɚ","bɛst"]
#	},
##18 8486 what what's whats whatcha 
#	"what":{
#		"tok":["seme"],
#		"jbo":["ma","mo"],
#		"eng":["ʍʌt"]
#	},
##19 7992 thought thoughts think thinks thinking 
#	"think":{
#		"tok":["pilin","toki insa"],
#		"jbo":["pensi","jinvi"],
#		"eng":["θɪŋk","θɔt"]
#	},
##20 7678 know knows knowing idk dunno afaik 
#	"know":{
#		"tok":["sona"],
#		"jbo":["djuno","du'o"],
#		"eng":["noʊ"]
#	},
##21 7322 can able 
#	"can":{
#		"tok":["ken"],
#		"jbo":["ka'e","kakne"],
#		"eng":["can"]
#	},
##22 6969 or 
#	"or":{
#		"tok":["anu"],
#		"jbo":["a","ja","ga","gi'a","gu'a"],
#		"eng":["ɔɹ","ksoɹ","ænd ɔɹ"]
#	},
##23 5363 about 
##uneeded?
##24 5203 get gets getting 
#	"get":{
#		"tok":["kama jo"],
#		"jbo":["cpacu","lebna"],
#		"eng":["ɡɛt"]
#	},
##25 5168 all every each
#	"all":{
#		"tok":["ali","ale"],
#		"jbo":["ro"],
#		"eng":["ɔl","ɛvɹi","ɛvəɹi","itʃ"]
#	},
##26 4812 more worse best 
#	"more":{
#		"tok":["mute"],
#		"jbo":["zmadu","za'u","mau","bancu","traji"],
#		"eng":["mɔɹ","moʊst"]
#	},
##27 4799 talk talking toki hi tell discuss telling told hey 
#	"talk":{
#		"tok":["toki"],
#		"jbo":["tavla","casnu","skicu","ciksi"],
#		"eng":["tɔk","tɛl","dɪskʌs","toʊld"]
#	},
##28 4441 mean means meaning meanings 
#	"meaning":{
#		"tok":["kon"],
#		"jbo":["smuni","sinxa","valsi"],
#		"eng":["minɪŋ","min"]
#	},
##29 4380 say says saying said 
#	"say":{
#		"tok":["toki","toki e ni"],
#		"jbo":["cusku","bacru","pinka"],
#		"eng":["seɪ","sɛd"]
#	},
##30 4358 would hypothetically 
#	"would":{
#		"tok":["ken la"],
#		"jbo":["da'i"],
#		"eng":["wʊd","haɪpəθɛtɪkli"]
#	},
##31 4290 go goes going 
#	"go":{
#		"tok":["tawa"],
#		"jbo":["klama","litru","muvdu","ka'a"],
#		"eng":["ɡoʊ","wɛnt"]
#	},
##32 3852 lang langs language languages natlangs natlang loglang conlang conlangs loglangs conlanging  
#	"language":{
#		"tok":["toki"],
#		"jbo":["bangu","bau"],
#		"eng":["leɪŋ","læŋɡwɪdʒ","tʌŋ"]
#	},
##33 3551 want wants wanting wanna  
#	"want":{
#		"tok":["wile"],
#		"jbo":["djica","pacna"],
#		"eng":["wɑnt"]
#	},
##34 3527 word words 
#	"word":{
#		"tok":["nimi"],
#		"jbo":["valsi","cmene"],
#		"eng":["wɝd","neɪm"]
#	},
##35 3474 see seeing 
#	"see":{
#		"tok":["lukin"],
#		"jbo":["viska","catlu","jvinu","zgana","ganse"],
#		"eng":["si","lʊk æt"]
#	},
##36 3407 oh o 
##uivla
##37 3335 people 
#	"people":{
#		"tok":["jan"],
#		"jbo":["prenu","zukte"],
#		"eng":["pɝsən","pipəl"]
#	},
##38 3209 why y 
#	"why":{
#		"tok":["tan seme"],
#		"jbo":["ki'u ma","mu'i ma","ni'i ma","ri'a ma"],
#		"eng":["ʍaɪ"]
#	},
##39 3176 up  
##handle later
##	"up":{
##		"tok":["sewi","anpa"],
##		"jbo":["galtu","ni'a","ga'u","cnita"],
##		"eng":["ʌp","ʌpwɚdz","əbʌv","daʊn","daʊnwɚdz","bɪloʊ"]
##	},
##40 3165 need needs  
#	"need":{
#		"tok":["wile"],
#		"jbo":["nitcu"],
#		"eng":["nid"]
#	},
##41 3135 hmm n m hmmm huh h 
##uivla
##42 3116 out 
##handle later
##	"out":{
##		"tok":["selo","weka"],
##		"jbo":["bartu"],
##		"eng":["aʊt","aʊtsaɪd"]
##	},
##43 3024 will willing gonna
#	"future":{
#		"tok":["tenpo kama","kama"],
#		"jbo":["balvi","ba"],
#		"eng":["wɪɫ","fjutʃəɹ","ɡənə"]
#	},
##44 2957 work works working 
#	"work":{
#		"tok":["pali"],
#		"jbo":["jerna","gunka","jibri"],
#		"eng":["wɝk","leɪbɚ"]
#	},
##45 2909 then
#	"past":{
#		"tok":["tenpo pini","pini"],
#		"jbo":["purci","pu"],
#		"eng":["ðɛn","pæst"]
#	},
##46 2815 now  
#	"now":{
#		"tok":["tenpo ni","ni"],
#		"jbo":["cabna","ca"],
#		"eng":["naʊ","kɝɪnt","pɹɛzənt"]
#	},
##47 2759 time times 
#	"time":{
#		"tok":["tenpo"],
#		"jbo":["detri","temci"],
#		"eng":["taɪm"]
#	},
##48 2747 should 
##uneeded
##49 2680 some 
#	"some":{
#		"tok":["mute"],
#		"jbo":["su'o"],
#		"eng":["sʌm"]
#	},
##50 2641 also 
##uivla
##51 2618 right
##nah we doing cardinal direcrtions
##pair with left
#	#"left":{
#	#	"tok":["lon poka","lon ni","poka"],
#	#	"jbo":["zunle","zu'a"],
#	#	"eng":["lɛft"]
#	#},
#	"north":{
#		"tok":["poka lete","tawa lete","nasin lete","lon poka","lon ni","poka","lete","lon poka ni","poka ni"],
#		"jbo":["berti","be'a"],
#		"eng":["noɹθ"]
#	},
#	"east":{
#		"tok":["kama suno","lon poka","lon ni","poka","lon poka ni","poka ni"],
#		"jbo":["stuna","du'a"],
#		"eng":["ist"]
#	},
#	"south":{
#		"tok":["poka seli","tawa seli","nasin seli","lon poka","lon ni","poka","seli","lon poka ni","poka ni"],
#		"jbo":["snanu","ne'u"],
#		"eng":["saʊθ"]
#	},
#	"west":{
#		"tok":["tawa suno","lon poka","lon ni","poka","lon poka ni","poka ni"],
#		"jbo":["stici","vu'a"],
#		"eng":["wɛst"]
#	},
##52 2617 could 
##later
##	"could":{
##		"tok":["ken la","ken"],
##		"jbo":["la'acu'i"],
##		"eng":["kʊd"]
##	},
#53 2609 /j j zo'o lol 
#uivla
#54 2577 way ways 
#55 2543 any 
#56 2448 probably 
#57 2380 than 
#58 2359 too 
#59 2359 only 
#60 2276 feel feels feeling feelings 
#61 2276 which 
#62 2237 look looks looking 
#63 2185 other others 
#64 2137 tho though 
#65 2102 person someone 
#66 2074 alright 
#67 2001 fair 
#68 1996 much 
#69 1939 love wuv 
#70 1863 still 
#71 1861 okay okey k 
#72 1836 by 
#73 1810 sorry u'u 
#74 1758 actually 
#75 1718 sound sounds sounding 
#76 1667 same 
#77 1646 try trying 
#78 1626 where 
#79 1616 idea ideas 
#80 1581 problem problems 
#81 1576 here here's 
#82 1569 better 
#83 1505 enough 
#84 1480 who who's 
#85 1457 bad 
#86 1435 most 
#87 1431 got 
#88 1430 even 
#89 1429 bit bits 
#90 1422 into 
#91 1405 first 
#92 1393 cool 
#93 1331 take takes taking 
#94 1331 maybe mayhaps perhaps perchance 
#95 1325 wait waiting 
#96 1290 point points 
#97 1282 number numbers 
#98 1258 sleep sleeping 
#99 1232 lojban 
#100 1231 system systems 
#101 1178 :p p 
#102 1164 might 
#103 1161 dolphin dolphinnnnn 
#104 1149 lot lots 
#105 1148 those 
#106 1136 english 
#107 1098 doubt x 
#108 1097 example examples 
#109 1086 call calling called 
#110 1044 before 
#111 1041 always 
#112 1029 hear hearing heard 
#113 1021 basically basic 
#114 1014 back 
#115 1009 nice 
#116 1003 sense 
#117 989 pretty 
#118 982 question questions 
#119 976 new 
#120 973 different 
#121 972 start starts starting 
#122 972 never 
#123 959 least 
#124 953 long 
#125 951 over 
#126 944 ah 
#127 937 reason reasons reasoning 
#128 932 off 
#129 930 come comes coming came 
#130 922 weird 
#131 919 vowel vowels 
#132 914 thank thanks 
#133 912 ask asking 
#134 912 interest interesting 
#135 910 either 
#136 901 understand understanding je'e 
#137 896 sec second 
#138 893 honestly tbh 
#139 889 change changes changing 
#140 880 part parts 
#141 866 day days 
#142 854 far 
#143 854 big 
#144 853 few 
#145 851 both 
#146 844 happen happens happening 
#147 818 btw 
#148 818 opinion opinions imo pe'i 
#149 817 case cases 
#150 816 may 
#151 816 read reading 
#152 816 true 
#153 814 many 
#154 811 find finding 
#155 792 name names 
#156 782 down 
#157 782 type types typing 
#158 781 wrong 
#159 780 each 
#160 779 possible 
#161 776 already 
#162 766 while 
#163 763 done 
#164 761 learn learning 
#165 761 definitely 
#166 755 fun 
#167 750 since 
#168 741 hard 
#169 738 give gives giving 
#170 736 kinda somewhat 
#171 735 oof 
#172 730 less 
#173 724 grammar 
#174 718 color colors 
#175 714 keep keeping 
#176 712 rip f 
#177 712 friend friends 
#178 710 write writing 
#179 708 without 
#180 703 art 
#181 701 hug 
#182 698 seem seems 
#183 697 ever 
#184 696 😉 
#185 694 cat cats 
#186 688 these 
#187 681 /s s 
#188 678 yet 
#189 668 whole 
#190 664 anyone 
#191 657 figure 
#192 656 after 
#193 655 let 
#194 652 add adds adding 
#195 647 stop stops 
#196 644 guess 
#197 640 everything 
#198 630 put putting 
#199 627 end ends 
#200 626 show shows showing 
#201 618 between 
#202 616 today 
#203 607 play playing 
#204 592 mind 
#205 591 place places 
#206 589 class classes 
#207 587 line lines 
#208 587 nothing 
#209 582 seen 
#210 574 else 
#211 571 exactly 
#212 568 game games 
#213 566 😅 
#214 565 vs versus 
#215 564 once 
#216 560 hope hoping 
#217 557 rather 
#218 555 rule rules 
#219 553 set sets 
#220 545 remember 
#221 543 pet 
#222 543 verb verbs 
#223 539 image images jpg 
#224 539 everyone 
#225 538 life 
#226 537 dog dogs 
#227 533 wish 
#228 531 plan plans planning 
#229 530 card cards 
#230 528 turn turns 
#231 528 sorta 
#232 528 cause 
#233 525 quite 
#234 520 pls please 
#235 518 cute 
#236 515 matter matters 
#237 512 draw drawing 
#238 511 based 
#239 511 whatever 
#240 509 such 
#241 508 next 
#242 501 assume assuming 
#243 495 last 
#244 494 ok 
#245 493 instead 
#246 493 syllable syllables sylables 
#247 492 little 
#248 487 until 
#249 483 term terms 
#250 479 year years 
#251 475 sometime sometimes 
#252 469 boy 
#253 466 hair 
#254 465 text 
#255 465 sentence sentences 
#256 458 important 
#257 453 dream dreams dreaming 
#258 452 etc 
#259 452 noun nouns 
#260 443 fine 
#261 442 imagine 
#262 441 form forms 
#263 440 close 
#264 437 almost 
#265 436 issue issues 
#266 433 phrase phrases 
#267 432 space spaces 
#268 424 believe 
#269 424 through 
#270 424 currently 
#271 422 speak speaking 
#272 417 option options 
#273 416 watch watching 
#274 414 own 
#275 412 head 
#276 412 care 
#277 412 group groups 
#278 411 level 
#279 411 anyway 
#280 409 again 
#281 408 together 
#282 405 phone 
#283 405 specific 
#284 403 depend depends depending 
#285 402 math 
#286 401 pantluci hy'yban 
#287 396 hand hands 
#288 395 often 
#289 395 phoneme phonemes 
#290 394 hour hours 
#291 394 common 
#292 393 another 
#293 392 wow 
#294 391 free 
#295 391 miss missing 
#296 388 eat eating 
#297 387 small 
#298 383 let's lets 
#299 382 easy 
#300 379 sick ill 
#301 377 valid 
#302 377 slightly 
#303 376 goal goals 
#304 375 letter letters 
#305 374 human humans 
#306 374 version 
#307 371 become becomes 
#308 369 wonder 
#309 364 red 
#310 362 useful 
#311 360 unless 
#312 359 meant 
#313 359 likely 
#314 359 proposal proposals 
#315 358 deal 
#316 358 order 
#317 358 tired 
#318 358 youtube youtu 
#319 357 happy 
#320 356 consonant consonants 
#321 352 top 
#322 350 face 
#323 350 list 
#324 350 completely 
#325 348 code 
#326 344 super 
#327 341 difference 
#328 340 soon 
#329 340 gotta 
#330 339 joke joking 
#331 339 explain 
#332 337 ooh 
#333 337 sort 
#334 335 vocab 
#335 335 however 
#336 334 bed 
#337 334 live living 
#338 332 concept concepts 
#339 330 half 
#340 328 book books 
#341 328 state states 
#342 328 brain 
#343 327 supposed 
#344 326 left 
#345 326 plus 
#346 326 wanted 
#347 325 specifically 
#348 324 share sharing 
#349 324 normally 
#350 320 course 
#351 320 consider considering 
#352 317 general 
#353 316 act acts acting 
#354 315 video videos 
#355 314 wear wearing 
#356 313 found 
#357 312 base 
#358 312 discord 
#359 306 root roots 
#360 304 perfect 
#361 302 room 
#362 302 length 
#363 300 old 
#364 299 family 
#365 298 result results 
#366 297 argument arguments 
#367 295 confused 
#368 293 blue 
#369 292 move moving 
#370 291 easier 
#371 291 realized 
#372 290 high 
#373 289 minute minutes 
#374 288 eye eyes 
#375 287 hot 
#376 287 interested 
#377 287 especially 
#378 286 amount 
#379 286 normal 
#380 285 went 
#381 285 allow allows 
#382 282 home 
#383 279 past 
#384 278 conversation 
#385 277 style 
#386 276 man 
#387 276 worry 
#388 276 build building 
#389 276 information 
#390 273 run running 
#391 273 side 
#392 273 night 
#393 270 girl girls 
#394 270 voice 
#395 269 follow following 
#396 266 yay u'i 
#397 266 worth 
#398 265 page pages 
#399 265 hurt hurts 
#400 265 pronoun pronouns 
#401 263 full 
#402 263 body 
#403 263 multiple 
#404 258 food 
#405 258 context 
#406 257 tone tones 
#}
refWords={
	"love":{
		"tok":["olin"],
		"jbo":["prami","iu"],
		"eng":["lʌv","ədɔɹ","tʃɛɹɪʃ"]
	},
	"sleep":{
		"tok":["lape"],
		"jbo":["sipna"],
		"eng":["slip"]
	},
	#minecraft primary colors
	"red":{
		"tok":["loje"],
		"jbo":["xunre"],
		"eng":["ɡulz","ɹɛd"]
	},
	"green":{
		"tok":["laso","laso kasi"],
		"jbo":["crino"],
		"eng":["vɝt","ɡɹin"]
	},
	"yellow":{
		"tok":["jelo"],
		"jbo":["pelxu"],
		"eng":["oɹ","jɛloʊ","ɡoʊld"]
	},
	"blue":{
		"tok":["laso","laso telo"],
		"jbo":["blanu"],
		"eng":["æzjʊɹ","blu"]
	},
	"black":{
		"tok":["pimeja"],
		"jbo":["xekri","manku"],
		"eng":["seɪbəl","blæk","dɑɹk","toʊnɚ"]
	},
	"brown":{
		"tok":["kule ma", "pi kule ma", "loje ma", "jelo ma", "loje pimeja", "jelo pimeja", "jelo", "loje", "pimeja"],
		"jbo":["bunre"],
		"eng":["bɹaʊn"]
	},
	"white":{
		"tok":["walo"],
		"jbo":["blabi"],
		"eng":["ɑɹdʒənt","waɪt","sɪlvɚ"]
	},
	#minecraft secondary colors
	"purple":{
		"tok":["laso loje", "loje laso", "laso", "loje"],
		"jbo":["zirpu"],
		"eng":["pɝpəl"]
	},
	"cyan":{
		"tok":["laso walo", "laso sewi", "laso"],
		"jbo":["cicna"],
		"eng":["saɪæn"]
	},
	#"light grey":{
	#	"tok":["walo pimeja", "walo"],
	#	"jbo":["labgrusi"],
	#	"eng":["laɪt ɡɹeɪ","sɛndɹeɪ","ɡɹeɪ"]
	#},
	"grey":{
		"tok":["walo pimeja", "pimeja walo", "pimeja", "walo"],
		"jbo":["grusi"],
		"eng":["ɡɹeɪ","sɛndɹeɪ"]
	},
	"pink":{
		"tok":["loje walo","loje"],
		"jbo":["penku"],
		"eng":["pɪŋk","ɹoʊz"]
	},
	"lime":{
		"tok":["laso walo", "laso walo kasi","laso","laso kasi","laso kasi walo"],
		"jbo":["pelri'o"],
		"eng":["laɪm"]
	},
	#"light blue":{
	#	"tok":["laso walo", "laso walo telo", "laso", "laso telo", "laso telo walo"],
	#	"jbo":["labybla"],
	#	"eng":["laɪt blu","səlɛst","blu səlɛst","blu"]
	#},
	"magenta":{
		"tok":["laso loje", "loje laso", "laso", "loje"],
		"jbo":["nukni"],
		"eng":["mədʒɛntə"]
	},
	"orange":{
		"tok":["loje jelo","jelo loje","loje","jelo"],
		"jbo":["narju"],
		"eng":["ɔɹɪndʒ","kɑpɚ"]
	},
	#other
	#"undyed":{
	#	#"fra":["bʁyt","betɔ̃ bʁyt"],
	#	"eng":["pɹɑpɚ","ɹɑ","ɛkɹu","ʌndaɪd"],
	#	"jbo":["mipcau"],
	#	"tok":["kule ala"]
	#},
	#materials
	"stone":{
		"tok":["kiwen"],
		"jbo":["rokci"],
		"eng":["stoʊn","ɹɑk","kɑŋkɹit"]
	},
	"bone":{
		"tok":["palisa","palisa insa"],
		"jbo":["bongu","greku"],
		"eng":["boʊn","skɛlətən"]
	},
	"brick":{
		"tok":["leko","kiwen","leko kiwen"],
		"jbo":["bliku","kliti"],
		"eng":["bɹɪk"]
	},
	#"plastic":{
	#	"tok":["kiwen"],
	#	"jbo":["slasi","ckabu"],
	#	"eng":["plæstɪk","pi i ti","pi ɛl eɪ","eɪ bi ɛs","pi vi si","pɑlɪmɚ"]
	#},
	#pets
	"dog":{
		"tok":["soweli"],
		"jbo":["gerku","lorxu","labno"],
		"eng":["pʌpi","wʊf","aɹf","bɑɹk"]
	},
	"cat":{
		"tok":["soweli"],
		"jbo":["mlatu","tirxu","cinfo"],
		"eng":["kæt","kɪti","kɪtən","filaɪn","mjaʊ","mju"]
	},
	#gender
	"boy":{
		"tok":["mije"],
		"jbo":["nanla","nanmu"],
		"eng":["bɔɪ"]
	},
	"girl":{
		"tok":["meli"],
		"jbo":["nixli","ninmu"],
		"eng":["ɡɝl","ɡɝəl"]
	},
	"enby":{
		"tok":["tonsi"],
		"jbo":["vepre","nunmu"],
		"eng":["ɛnbi"]
	},
	#materials pt. 2
	"blood":{
		"tok":["loje","telo loje","telo insa"],
		"jbo":["ciblu"],
		"eng":["blʌd"]
	},
	"wood":{
		"tok":["kasi","kasi suli"],
		"jbo":["mudri","stani","tricu"],
		"eng":["wʊd","tɹi","lʌmbɚ","tɹʌŋk"]
	},
	"water":{
		"tok":["telo"],
		"jbo":["djacu","cilmo"],
		"eng":["wɔtəɹ","wɛt","ækwə"]
	},
}

def lang2pantluci(word, lang):
	if lang=="fra":
		pairs={
			" ":"",

			"ʁ":"l",

			"b":"n",

			"ɔ̃":"on",
		}
	if lang=="tok":
		pairs={
			"k":"c",

			"j":"i",

			"m":"n",

			"s":"t",

			"w":"u",

			" ":"",
		}
	if lang=="jbo":
		pairs={
			"c":"ʃ",
			"y":"ə",

			"ə":"a",

			"k":"c",
			"x":"c",
			"g":"c",
			
			"j":"l",
			"d":"l",
			"r":"l",

			"b":"n",
			"m":"n",
			"v":"n",

			"f":"p",

			"z":"t",
			"ʃ":"t",
			"s":"t",
			
			"'":"",
			" ":"",
		}
	if lang=="eng":
		pairs={
			"ʌ":"a",
			"æ":"a",
			"ɑ":"a",
			"ə":"a",
			"ɔ":"a",
			"ɜ":"a",

			"ɡ":"c",
			"k":"c",

			"ɛ":"e",

			"ɝ":"el",

			"j":"i",
			"ɪ":"i",

			"d":"l",
			"ɹ":"l",
			"ɾ":"l",
			"ɚ":"l",
			"ð":"l",
			"ɫ":"l",
			"ʒ":"l",

			"b":"n",
			"ŋ":"n",
			"m":"n",
			"v":"n",

			"f":"p",

			"θ":"t",
			"ʃ":"t",
			"s":"t",
			"z":"t",
			#"ʧ":"t",

			"ʊ":"u",
			"w":"u",
			"ʍ":"u",

			"h":"",
			" ":"",
		}
		word=word.replace("tʃ","ʧ")
		#word=word.replace("dʒ","ʤ")
	for p in pairs:
		word=word.replace(p,pairs[p])

	if lang=="eng":
		word=word.replace("ʧl","tl")
		word=word.replace("ʧ","tl")
		word=word.replace("ʤl","ll")
		word=word.replace("ʤ","ll")

	for l in word:
		if not l in "ptclnaiueoy":
			print(word,l,lang)
			0/0
	return word

for word in refWords:
	for lang in refWords[word]:
		for i in range(len(refWords[word][lang])):
			refWords[word][lang][i]=lang2pantluci(refWords[word][lang][i],lang)

#print(refWords)
#0/0

def breakdown(word):
	out=[""]
	while len(word)>0:
		if word[0] in "yoeaiu":
			if word[0] == "y":
				for t in range(len(out)):
					out.append(out[t]+"i")
					out[t]+="u"
			if word[0] == "o":
				for t in range(len(out)):
					out.append(out[t]+"a")
					out[t]+="u"
			if word[0] == "e":
				for t in range(len(out)):
					out.append(out[t]+"i")
					out[t]+="a"
			if word[0] == "a":
				for t in range(len(out)):
					out.append(out[t]+"a")
					out[t]+="a"
			if word[0] == "i":
				for t in range(len(out)):
					out.append(out[t]+"i")
					out[t]+="i"
			if word[0] == "u":
				for t in range(len(out)):
					out.append(out[t]+"u")
					out[t]+="u"
		else:
			for t in range(len(out)):
				out[t]+=word[0]
		word=word[1:]
	return out


Version2=True
#['a', 'na', 'nata', 'ta', 'la', 'ala', 'ca', 'an']
#['a', 'nata', 'na', 'ta', 'la', 'ala', 'ca', 'an']
Version2=False
insertWeight, replaceWeight, swapWeight, deleteWeight = 6, 4, 3, 5
#{'na': 'we(incl)', 'a': 'i/we(excl)', 'ta': 'it', 'la': 'is', 'ala': 'you', 'ca': 'you(imp)', 'an': 'in'}

#insertWeight, replaceWeight, swapWeight, deleteWeight = 30, 1, 1, 1
#{'na': 'we(excl)', 'nan': 'we(incl)', 'ta': 'it', 'la': 'is', 'tala': 'you', 'canau': 'you(imp)', 'a': 'in'}

smoothLevelBase=20
insertWeight, replaceWeight, swapWeight, deleteWeight = 100*smoothLevelBase, smoothLevelBase+1, smoothLevelBase, smoothLevelBase+2

#1  we(incl)-na i/we(excl)-an it-ana is-la you-ala  you(imp)-tcanui in-ta  not-ani and-a  to-talua
#2  we(incl)-na i/we(excl)-a  it-ta  is-la you-ala  you(imp)-canau  in-an  not-ana and-ca to-talua
#3+ we(incl)-na i/we(excl)-a  it-ta  is-la you-tala you(imp)-canau  in-lan not-ana and-an to-talua


print(damerauLevenshtein("ui","niu",Version2,insertWeight=insertWeight,replaceWeight=replaceWeight,swapWeight=swapWeight,deleteWeight=deleteWeight))
print(damerauLevenshtein("niu","ui",Version2,insertWeight=insertWeight,replaceWeight=replaceWeight,swapWeight=swapWeight,deleteWeight=deleteWeight))
print(damerauLevenshtein("-ui-","-niu-",Version2,insertWeight=insertWeight,replaceWeight=replaceWeight,swapWeight=swapWeight,deleteWeight=deleteWeight))
print(damerauLevenshtein("-niu-","-ui-",Version2,insertWeight=insertWeight,replaceWeight=replaceWeight,swapWeight=swapWeight,deleteWeight=deleteWeight))
print(damerauLevenshtein("ui","nui",Version2,insertWeight=insertWeight,replaceWeight=replaceWeight,swapWeight=swapWeight,deleteWeight=deleteWeight))
print(damerauLevenshtein("nui","ui",Version2,insertWeight=insertWeight,replaceWeight=replaceWeight,swapWeight=swapWeight,deleteWeight=deleteWeight))
print(damerauLevenshtein("-ui-","-nui-",Version2,insertWeight=insertWeight,replaceWeight=replaceWeight,swapWeight=swapWeight,deleteWeight=deleteWeight))
print(damerauLevenshtein("-nui-","-ui-",Version2,insertWeight=insertWeight,replaceWeight=replaceWeight,swapWeight=swapWeight,deleteWeight=deleteWeight))
#0/0

i=0
used={'pantluci': 'pantluci', 'na': 'we(incl)', 'a': 'i/we(excl)', 'ta': 'it', 'la': 'is', 'tala': 'you', 'canau': 'you(imp)', 'lan': 'in', 'ana': 'not', 'an': 'and', 'talua': 'to', 'pla': 'help', 'atia': 'similar', 'tan': 'of', 'pnali': 'do', 'ca': 'real', 'atu': 'therefore', 'panti': 'have', 'tna': 'something', 'canla': 'good', 'tana': 'what', 'patni': 'think', 'lana': 'know', 'can': 'can', 'alu': 'or', 'canaia': 'get', 'ala': 'all', 'natu': 'more', 'tacti': 'talk', 'cnani': 'meaning', 'taci': 'say', 'canli': 'would', 'cana': 'go', 'tani': 'language', 'anta': 'want', 'tnani': 'word', 'lacta': 'see', 'panu': 'people', 'antina': 'why', 'natlu': 'need', 'acna': 'future', 'lali': 'work', 'pani': 'past', 'nan': 'now', 'tanpi': 'time', 'tata': 'some', 'nala': 'north', 'ata': 'east', 'tatu': 'south', 'aca': 'west'}
mult=-1
if Version2:
	mult=1

for w in refWords:
	i+=1
	bigWord={}
	biggest=-9999999999999999
	test={}
	testUnrefined={}
	maxLen =0	
	for lang in refWords[w]:
		test[lang]=[]
		testUnrefined[lang]=[]
		for bit in refWords[w][lang]:
			for word in breakdown(bit):
				if not word in test[lang]:
					test[lang].append(word)
				testUnrefined[lang].append(word)

		for bit in test[lang]:
			maxLen =max(len(bit),maxLen)

	#if maxLen>len(forms):
	#	print(len(forms))
	#	0/0

	for score1 in forms:
		if score1<=maxLen:
			print(score1)
			for wTest in forms[score1]:
				VSimpwTest=VSimp(wTest)
				bests={}
				scores={}

				for lang in refWords[w]:
					bests[lang] = []
					scores[lang]=-999999999
					for bit in test[lang]:
						sTemp=mult*damerauLevenshtein("-"+wTest+"-","-"+bit+"-",Version2,insertWeight=insertWeight,replaceWeight=replaceWeight,swapWeight=swapWeight,deleteWeight=deleteWeight)
						if sTemp==scores[lang]:
							bests[lang].append(bit)
						if sTemp>scores[lang]:
							bests[lang]=[bit]
							scores[lang]=sTemp

				score=0
				for lang in refWords[w]:
					score += scores[lang]

				#print(w,wTest,score1,tokscore,jboscore,engscore, "/".join(tokb), "/".join(jbob), "/".join(engb))
				if score>=biggest and (not VSimpwTest in used):
					print(i, score1, w, wTest, score, bests, scores, len(bigWord))
					if score>biggest:
						bigWord={}
						biggest=score
					bigWord[wTest]=[]
					for lang in refWords[w]:
						bigWord[wTest].append(bests[lang])
	print("~"*30)
	print(bigWord)
	print("~"*30)
	RAMbest=[]
	RAMnum=0

	for word in bigWord:
		total=1
		for n in range(len(bigWord[word])):
			total*=len(bigWord[word][n])

		if total==RAMnum and not word in RAMbest:
			RAMbest.append(word)

		if total>RAMnum:
			RAMnum=total
			RAMbest=[word]

	if len(RAMbest)>1:
		tourney={}
		keys=[[]]
		for lang in refWords[w]:
			#print(lang,)
			oldkeys=keys.copy()
			keys=[]
			for k in oldkeys.copy():
				#print(k)
				for bit in testUnrefined[lang]:
					#print(bit)
					keys.append(k.copy())
					keys[-1].append(bit)
					#print("a",keys)
			#0/0
		print(len(keys))
		for wTest in RAMbest:
			tourney[wTest]=[]
			for k in keys:
				score=0
				for kp in k:
					score+=mult*damerauLevenshtein("-"+wTest+"-","-"+kp+"-",Version2,insertWeight=insertWeight,replaceWeight=replaceWeight,swapWeight=swapWeight,deleteWeight=deleteWeight)
				
				tourney[wTest].append(score)
			tourney[wTest].sort(reverse = True)
			#if len(used)>=50:
			#	tourney[wTest].append(wTest.count("n"))#phoible m 2914
			#	tourney[wTest].append(wTest.count("i"))#phoible i 2779
			#	tourney[wTest].append(wTest.count("c"))#phoible k 2730
			#	tourney[wTest].append(wTest.count("u"))#phoible u 2646
			#	tourney[wTest].append(wTest.count("a"))#phoible a 2600
			#	tourney[wTest].append(wTest.count("p"))#phoible p 2594
			#	tourney[wTest].append(wTest.count("t"))#phoible t 2064
			#	tourney[wTest].append(wTest.count("l"))#phoible l 2044
		ID=-1
		same=True
		bestest=""
		while same:
			sameTest=[]
			ID+=1
			best=-999999999
			for wTest in RAMbest:
				Vreduced=VSimp(wTest)
				if not Vreduced in sameTest:
					sameTest.append(Vreduced)
				if tourney[wTest][ID]==best:
					same=True
				if tourney[wTest][ID]>best:
					same=False
					best=tourney[wTest][ID]
					bestest=wTest
				print(tourney[wTest][ID],ID,wTest,bestest)
				#print(Vreduced)

			for wTest in RAMbest.copy():
				if tourney[wTest][ID]<best:
					RAMbest.remove(wTest)

			if len(sameTest)==1:
				RAMbest.remove(wTest)
			print()
		RAMbest=[bestest]
			

	used[VSimp(RAMbest[0])]=w
	print(used)
	print(len(used)-1,"\n:3\n")
print(len(used))

thisLen=0
tally=0
keys = list(used.keys())
keys.sort(key=lambda x: len(x))
for u in keys:
	if len(u)>thisLen:
		print()
		if thisLen in forms:
			print(len(u),len(minnedExclusion[thisLen]),tally,str(int(10000*tally/len(minnedExclusion[thisLen]))/100)+"%")
		thisLen=len(u)
		tally=0
	tally+=1
	print(str(used[u])+"-"+str(u),end=" ")