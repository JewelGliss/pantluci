module.exports.dictionary_en = require('../../dictionary/en.yaml');

const alphabet = 'aábcdeéfghiíjklmnoópqrstuúvwxyýz';

let symbol_indices = {};

for (i = 0; i < alphabet.length; i++) {
    symbol_indices[alphabet[i]] = i;
}

console.log({symbol_indices});

function compare_words(x, y) {
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
	
    x=x.replaceAll("aá","a\u{1bC76}")
	x=x.replaceAll("eé","e\u{1bC76}")
	x=x.replaceAll("ií","i\u{1bC76}")
	x=x.replaceAll("oó","o\u{1bC76}")
	x=x.replaceAll("uú","u\u{1bC76}")
	x=x.replaceAll("yý","y\u{1bC76}")

	x=x.replaceAll("áa","a\u{1bC77}")
	x=x.replaceAll("ée","e\u{1bC77}")
	x=x.replaceAll("íi","i\u{1bC77}")
	x=x.replaceAll("óo","o\u{1bC77}")
	x=x.replaceAll("úu","u\u{1bC77}")
	x=x.replaceAll("ýy","y\u{1bC77}")

	x=x.replaceAll("á","a\u{1bC74}")
	x=x.replaceAll("é","e\u{1bC74}")
	x=x.replaceAll("í","i\u{1bC74}")
	x=x.replaceAll("ó","o\u{1bC74}")
	x=x.replaceAll("ú","u\u{1bC74}")
	x=x.replaceAll("ý","y\u{1bC74}")

	x=x.replaceAll("a","\u{1BC41}\u{1BC71}")
	x=x.replaceAll("y","\u{1BC57}\u{1BC71}")
	x=x.replaceAll("e","\u{1BC41}\u{1BC46}\u{1BC71}")
	x=x.replaceAll("o","\u{1BC42}\u{1BC46}\u{1BC71}")
	x=x.replaceAll("i","\u{1BC41}\u{1BC51}\u{1BC71}")
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
	x=x.replaceAll("j","\u{1BC3A}")
	x=x.replaceAll("k","\u{1BC05}")
	x=x.replaceAll("l","\u{1BC06}")
	x=x.replaceAll("m","\u{1BC19}")
	x=x.replaceAll("n","\u{1BC1A}")
	x=x.replaceAll("p","\u{1BC02}")
	x=x.replaceAll("q","\u{1BC28}")
	x=x.replaceAll("r","\u{1BC0B}")
	x=x.replaceAll("s","\u{1BC1C}")
	x=x.replaceAll("t","\u{1BC03}")
	x=x.replaceAll("v","\u{1BC09}")
	x=x.replaceAll("w","\u{1BC3C}")
	x=x.replaceAll("x","\u{1BC30}")
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
	
	return x
}

module.exports.dupl_converter = dupl_converter;