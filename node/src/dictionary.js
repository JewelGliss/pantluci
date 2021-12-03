module.exports.dictionary_en = require('../../dictionary/en.yaml');

const alphabet = 'abcdefghıȷklmnoprstuvwxyz ́'; //acute is final letter

let symbol_indices = {};

for (i = 0; i < alphabet.length; i++) {
    symbol_indices[alphabet[i]] = i;
}

//console.log({symbol_indices});

function compare_words(x, y) {
	
	x=x.replaceAll("á","á")
	x=x.replaceAll("é","é")
	x=x.replaceAll("í","ı́")
	x=x.replaceAll("ó","ó")
	x=x.replaceAll("ú","ú")
	x=x.replaceAll("ý","ý")
	x=x.replaceAll("ṕ","ṕ")
	x=x.replaceAll("ḱ","ḱ")
	x=x.replaceAll("ǵ","ǵ")
	x=x.replaceAll("ś","ś")
	
	y=y.replaceAll("á","á")
	y=y.replaceAll("é","é")
	y=y.replaceAll("í","ı́")
	y=y.replaceAll("ó","ó")
	y=y.replaceAll("ú","ú")
	y=y.replaceAll("ý","ý")
	y=y.replaceAll("ṕ","ṕ")
	y=y.replaceAll("ḱ","ḱ")
	y=y.replaceAll("ǵ","ǵ")
	y=y.replaceAll("ś","ś")
	
	if ("aeıouy".includes(x.charAt(0))){
		x=" "+x
	}
	if ("aeıouy".includes(y.charAt(0))){
		y=" "+y
	}
    if (x == y) {
        return 0;
    }

    for(i = 0; i < x.length; i++) {
        if (i >= y.length) {
            return 1; // y is shorter and 
        }

        let sx = symbol_indices[x[i]];
        let sy = symbol_indices[y[i]];

        // earlier in the alphabet => first to appear
        if (sx < sy) {
            return -1;
        } else if (sx > sy) {
            return 1;
        }
    }
}

module.exports.compare_words = compare_words;

function dupl_converter(x) {
	while(x.includes("__")){
		x=x.replaceAll("__","_")
	}
	x=x.replaceAll("ṕ","p\u{1bC77}")
    x=x.replaceAll("t́","t\u{1bC77}")
	x=x.replaceAll("ḱ","k\u{1bC77}")
	
	x=x.replaceAll("ś","s\u{1bC77}")
	
    x=x.replaceAll("b́","b\u{1bC77}")
	x=x.replaceAll("d́","d\u{1bC77}")
	x=x.replaceAll("ǵ","g\u{1bC77}")
	
    x=x.replaceAll("aá","a\u{1bC76}")
	x=x.replaceAll("eé","e\u{1bC76}")
	x=x.replaceAll("ıı́","ı\u{1bC76}")
	x=x.replaceAll("oó","o\u{1bC76}")
	x=x.replaceAll("uú","u\u{1bC76}")
	x=x.replaceAll("yý","y\u{1bC76}")

	x=x.replaceAll("áa","a\u{1bC77}")
	x=x.replaceAll("ée","e\u{1bC77}")
	x=x.replaceAll("ı́ı","ı\u{1bC77}")
	x=x.replaceAll("óo","o\u{1bC77}")
	x=x.replaceAll("úu","u\u{1bC77}")
	x=x.replaceAll("ýy","y\u{1bC77}")

	x=x.replaceAll("á","a\u{1bC74}")
	x=x.replaceAll("é","e\u{1bC74}")
	x=x.replaceAll("ı́","ı\u{1bC74}")
	x=x.replaceAll("ó","o\u{1bC74}")
	x=x.replaceAll("ú","u\u{1bC74}")
	x=x.replaceAll("ý","y\u{1bC74}")

	x=x.replaceAll("a","\u{1BC41}\u{1BC71}")
	x=x.replaceAll("y","\u{1BC57}\u{1BC71}")
	x=x.replaceAll("e","\u{1BC41}\u{1BC46}\u{1BC71}")
	x=x.replaceAll("o","\u{1BC42}\u{1BC46}\u{1BC71}")
	x=x.replaceAll("ı","\u{1BC41}\u{1BC51}\u{1BC71}")
	x=x.replaceAll("u","\u{1BC42}\u{1BC51}\u{1BC71}")
	
	x=x.replaceAll("\u{1BC42}","\u{1BC57}")

	x=x.replaceAll("\u{1BC71}\u{1BC76}","\u{1BC76}")
	x=x.replaceAll("\u{1BC71}\u{1BC77}","\u{1BC77}")
	x=x.replaceAll("\u{1BC71}\u{1BC74}","\u{1BC74}")

	x=x.replaceAll("b","\u{1BC07}")
	x=x.replaceAll("c","\u{1BC1B}")
	x=x.replaceAll("d","\u{1BC08}")
	x=x.replaceAll("f","\u{1BC04}")
	x=x.replaceAll("g","\u{1BC0A}")
	x=x.replaceAll("h","\u{1BC33}")
	x=x.replaceAll("ȷ","\u{1BC3A}")
	x=x.replaceAll("k","\u{1BC05}")
	x=x.replaceAll("l","\u{1BC06}")
	x=x.replaceAll("m","\u{1BC19}")
	x=x.replaceAll("n","\u{1BC1A}")
	x=x.replaceAll("p","\u{1BC02}")
	x=x.replaceAll("r","\u{1BC0B}")
	x=x.replaceAll("s","\u{1BC1C}")
	x=x.replaceAll("t","\u{1BC03}")
	x=x.replaceAll("v","\u{1BC09}")
	x=x.replaceAll("w","\u{1BC3C}")
	x=x.replaceAll("x","\u{1BC31}")
	x=x.replaceAll("z","\u{1BC2A}")

	x=x.replaceAll("\u{1BC46}\u{1BC76}","\u{1BC76}\u{1BC46}")
	x=x.replaceAll("\u{1BC46}\u{1BC77}","\u{1BC77}\u{1BC46}")
	x=x.replaceAll("\u{1BC46}\u{1BC71}","\u{1BC71}\u{1BC46}")
	x=x.replaceAll("\u{1BC46}\u{1BC74}","\u{1BC74}\u{1BC46}")

	x=x.replaceAll("\u{1BC51}\u{1BC76}","\u{1BC76}\u{1BC51}")
	x=x.replaceAll("\u{1BC51}\u{1BC77}","\u{1BC77}\u{1BC51}")
	x=x.replaceAll("\u{1BC51}\u{1BC71}","\u{1BC71}\u{1BC51}")
	x=x.replaceAll("\u{1BC51}\u{1BC74}","\u{1BC74}\u{1BC51}")
	
	x=x.replaceAll("\u{1BC71}","")
	
	x=x.replaceAll("\u{1BC57}","\u{1BC57}<69105>")
	x=x.replaceAll("<69105>","<69105>")
	x=x.replaceAll("<69105>\u{1BC71}","\u{1BC71}<69105>")
	x=x.replaceAll("<69105>\u{1BC74}","\u{1BC74}<69105>")
	x=x.replaceAll("<69105>\u{1BC76}","\u{1BC76}<69105>")
	x=x.replaceAll("<69105>\u{1BC77}","\u{1BC77}<69105>")
	x=x.replaceAll("<69105>\u{1BC51}","\u{1BC51}<69105>")
	x=x.replaceAll("<69105>\u{1BC46}","\u{1BC46}<69105>")
	x=x.replaceAll("\u{1BC51}<69105>","\u{1BC52}")
	x=x.replaceAll("\u{1BC46}<69105>","\u{1BC47}")
	x=x.replaceAll("\u{1BC52}<69105>","\u{1BC51}")
	x=x.replaceAll("\u{1BC47}<69105>","\u{1BC46}")
	x=x.replaceAll("<69105>","")
	
	return x
}

module.exports.dupl_converter = dupl_converter;

function ipa_converter(x) {
	x="."+x
	//seperate underscores
	x=x.replaceAll("_ _","_._")
	
	//glottal stop new lines
	x=x.replaceAll("\n","\n ")
	
	//convert to phonemes and segment
	x=x.replaceAll(" a",".ʔa")
	x=x.replaceAll(" e",".ʔe")
	x=x.replaceAll(" ı",".ʔı")
	x=x.replaceAll(" o",".ʔo")
	x=x.replaceAll(" u",".ʔu")
	x=x.replaceAll(" y",".ʔy")
	
	x=x.replaceAll(" ","")
	
    x=x.replaceAll("aá","ä˨.ä˦.")
	x=x.replaceAll("eé","ɛ˨.ɛ˦.")
	x=x.replaceAll("ıı́","i˨.i˦.")
	x=x.replaceAll("oó","o˨.o˦.")
	x=x.replaceAll("uú","u˨.u˦.")
	x=x.replaceAll("yý","ə˨.ə˦.")
	
    x=x.replaceAll("áa","ä˦.ä˨.")
	x=x.replaceAll("ée","ɛ˦.ɛ˨.")
	x=x.replaceAll("ı́ı","i˦.i˨.")
	x=x.replaceAll("óo","o˦.o˨.")
	x=x.replaceAll("úu","u˦.u˨.")
	x=x.replaceAll("ýy","ə˦.ə˨.")

    x=x.replaceAll("á","ä˦.")
	x=x.replaceAll("é","ɛ˦.")
	x=x.replaceAll("ı́","i˦.")
	x=x.replaceAll("ó","o˦.")
	x=x.replaceAll("ú","u˦.")
	x=x.replaceAll("ý","ə˦.")
	
    x=x.replaceAll("a","ä?")
	x=x.replaceAll("e","ɛ?")
	x=x.replaceAll("ı","i?")
	x=x.replaceAll("o","o?")
	x=x.replaceAll("u","u?")
	x=x.replaceAll("y","ə?")

	x=x.replaceAll("?˦","˦")
	x=x.replaceAll("?˨","˨")
	x=x.replaceAll("?","˨.")
	
	x=x.replaceAll("n","n?")
	
    x=x.replaceAll("?ä","ä")
	x=x.replaceAll("?ɛ","ɛ")
	x=x.replaceAll("?i","i")
	x=x.replaceAll("?o","o")
	x=x.replaceAll("?u","u")
	x=x.replaceAll("?ə","ə")
	
	x=x.replaceAll(".n?","n.")
	
	x=x.replaceAll(".ä",".ʔä")
	x=x.replaceAll(".ɛ",".ʔɛ")
	x=x.replaceAll(".i",".ʔi")
	x=x.replaceAll(".o",".ʔo")
	x=x.replaceAll(".u",".ʔu")
	x=x.replaceAll(".ə",".ʔə")
	
	x=x.replaceAll("ä˦.ʔä","ä˦.ä")
	x=x.replaceAll("ä˨.ʔä","ä˨.ä")
	x=x.replaceAll("ɛ˦.ʔɛ","ɛ˦.ɛ")
	x=x.replaceAll("ɛ˨.ʔɛ","ɛ˨.ɛ")
	x=x.replaceAll("i˦.ʔi","i˦.i")
	x=x.replaceAll("i˨.ʔi","i˨.i")
	x=x.replaceAll("o˦.ʔo","o˦.o")
	x=x.replaceAll("o˨.ʔo","o˨.o")
	x=x.replaceAll("u˦.ʔu","u˦.u")
	x=x.replaceAll("u˨.ʔu","u˨.u")
	x=x.replaceAll("ə˦.ʔə","ə˦.ə")
	x=x.replaceAll("ə˨.ʔə","ə˨.ə")
	
	x=x.replaceAll("ä˦.ä˦","ä˦.ʔä˦")
	x=x.replaceAll("ä˨.ä˨","ä˨.ʔä˨")
	x=x.replaceAll("ɛ˦.ɛ˦","ɛ˦.ʔɛ˦")
	x=x.replaceAll("ɛ˨.ɛ˨","ɛ˨.ʔɛ˨")
	x=x.replaceAll("i˦.i˦","i˦.ʔi˦")
	x=x.replaceAll("i˨.i˨","i˨.ʔi˨")
	x=x.replaceAll("o˦.o˦","o˦.ʔo˦")
	x=x.replaceAll("o˨.o˨","o˨.ʔo˨")
	x=x.replaceAll("u˦.u˦","u˦.ʔu˦")
	x=x.replaceAll("u˨.u˨","u˨.ʔu˨")
	x=x.replaceAll("ə˦.ə˦","ə˦.ʔə˦")
	x=x.replaceAll("ə˨.ə˨","ə˨.ʔə˨")
	
	x=x.replaceAll("ṕ","pʼ")
	x=x.replaceAll("t́","tʼ")
	x=x.replaceAll("ḱ","kʼ")
	x=x.replaceAll("ś","ɬ")
	x=x.replaceAll("b́","ɓ")
	x=x.replaceAll("d́","ɗ")
	x=x.replaceAll("ǵ","ɠ")
	x=x.replaceAll("c","ʃ")
	x=x.replaceAll("h","ç")
	x=x.replaceAll("r","ɾ")
	x=x.replaceAll("ȷ","j")
	//j/ is realized as [ʒ] before /i/ or /ɛ/.
	x=x.replaceAll("jɛ","ʒɛ")
	x=x.replaceAll("ji","ʒi")
	//i˨.i˦/ is realized as [jiː˨˦] unless it follows /ʔ/, /pʼ/, /z/, /s/, /x/, /ɾ/, /l/, or /w/.
	//i˨.i˦/ is realized as [iː˨˨˦] when follows /ʔ/, /pʼ/, /z/, /s/, /x/, /ɾ/, /l/, or /w/.
	x=x.replaceAll("i˨.i˦","?")
	var whenFollowing=['ʔ','pʼ','z','s','ɬ','x','ɾ','l','w']
	for (var i = 0; i < whenFollowing.length; i++) {
		x=x.replaceAll(whenFollowing[i]+"?",whenFollowing[i]+"iː˨˨˦")
	}
	x=x.replaceAll("?","ji˨˦")
	//i˦.i˨/ is realized as [jə˦˨] unless it follows /ʔ/, /ɾ/, or /l/.
	x=x.replaceAll("i˦.i˨","?")
	var whenFollowing=["ʔ","ɾ","l"]
	for (var i = 0; i < whenFollowing.length; i++) {
		x=x.replaceAll(whenFollowing[i]+"?",whenFollowing[i]+"i˦.i˨")
	}
	x=x.replaceAll("?","jə˦˨")
	//ä˨.ä˦/ is realized as [äi̯˨˦].
	x=x.replaceAll("ä˨.ä˦","äi̯˨˦")
	//ä˦.ä˨/ is realized as [äu̯˦˨].
	x=x.replaceAll("ä˦.ä˨","äu̯˦˨")
	//ɛ˨.ɛ˦/ is realized as [ɛi̯˨˦].
	x=x.replaceAll("ɛ˨.ɛ˦","ɛi̯˨˦")
	//[tj] is realized as [t͡ʃ].
	x=x.replaceAll("tj","t͡ʃ")
	//[tʼj] is realized as [t͡ʃʼ].
	x=x.replaceAll("tʼj","t͡ʃʼ")
	//[dj] is realized as [d͡ʒ].
	x=x.replaceAll("dj","d͡ʒ")
	//[nj] is realized as [ɲ].
	x=x.replaceAll("nj","ɲ")
	//ʔi/ is realized as [ʔji].
	x=x.replaceAll("ʔi","ʔji")
	//[ʒ] is realized as [ʑ] before [j].
	x=x.replaceAll("ʒj","ʑj")
	//[ʃ] is realized as [ɕ] before [j].
	x=x.replaceAll("ʃj","ɕj")
	//k/, /g/ and /ɠ/ is pronounced as palatal before [j].
	x=x.replaceAll("kj","cj")
	x=x.replaceAll("gj","ɟj")
	x=x.replaceAll("ɠj","ʄj")
	//[kʼj] is realized as [cç].
	x=x.replaceAll("kʼj","cç")
	//assimilated and dissimilated
	x=x.replaceAll("n.b","m.b")
	x=x.replaceAll("n.g","ŋ.g")
	x=x.replaceAll("n.p","m.p")
	x=x.replaceAll("n.k","ŋ.k")
	x=x.replaceAll("n.v","m.v")
	x=x.replaceAll("n.f","m.f")
	x=x.replaceAll("n.x","ŋ.x")
	x=x.replaceAll("n.n","m.n")
	x=x.replaceAll("n.w","ŋ.w")
	x=x.replaceAll("n.ç","ɲ.ç")
	x=x.replaceAll("n.j","ɲ.j")
	x=x.replaceAll("n.c","ɲ.c")
	x=x.replaceAll("n.ɟ","ɲ.ɟ")
	x=x.replaceAll("n.ʄ","ɲ.ʄ")
	x=x.replaceAll("n.ɓ","m.ɓ")
	x=x.replaceAll("n.ɠ","ŋ.ɠ")
	
	while(x.includes("__")){
		x=x.replaceAll("__","_")
	}
	x=x.replaceAll("._"," _")
	x=x.replaceAll("_.","_ ")
	
	x="?"+x+"?"
	x=x.replaceAll(".?","")
	x=x.replaceAll("?.","")
	x=x.replaceAll("_?","_")
	x=x.replaceAll("_","__")
	
	while(x.indexOf("..") !== -1){
		x = x.replaceAll('..', '.');
	}
	return x
}

module.exports.ipa_converter = ipa_converter;
