const dictionary = require('../../dictionary/en.yaml');

// Valid consonants list.
const c = ['b','b́','c','d','d́','f','g','ǵ','h','ȷ','k','ḱ','l','m','n','p','ṕ','r','s','ś','t','t́','v','w','x','z',''];

// Consonants weights.
const cw = '110110110000111001000011011';

// Valid vowels list.
const v = 'aeıouy';

// Vowels weights.
const vw = '111000';

// Building a map of the weight for all possible syllable forms.
let s = {"_____":2};
for (var i = 0; i < c.length; i++) {
	for (var j = 0; j < v.length; j++) {
		var extra=0;
		console.log(c[i] + v[j])
		if(["ȷı","ȷe","wu","wo"].includes(c[i] + v[j])){
			extra++;
		}
		console.log(extra)
		s[c[i] + v[j]] = parseInt(cw[i]) + parseInt(vw[j]) + extra;
		s[c[i] + v[j] + 'n'] = parseInt(cw[i]) + parseInt(vw[j]) + 1 + extra;

		s[c[i] + v[j]+"́"] = parseInt(cw[i]) + parseInt(vw[j]) + extra;
		s[c[i] + v[j] + '́n'] = parseInt(cw[i]) + parseInt(vw[j]) + 1 + extra;

		s[c[i] + v[j] + v[j]+"́"] = parseInt(cw[i]) + parseInt(vw[j]) + 1 + extra;
		s[c[i] + v[j] + v[j] + '́n'] = parseInt(cw[i]) + parseInt(vw[j]) + 2 + extra;

		s[c[i] + v[j]+"́" + v[j]] = parseInt(cw[i]) + parseInt(vw[j]) + 1;
		s[c[i] + v[j]+"́" + v[j] + 'n'] = parseInt(cw[i]) + parseInt(vw[j]) + 2 + extra;
	}
}

// Takes a string as input and returns a list of words.
function segmenter(str) {
	str = str.replaceAll(' _',"._")
	str = str.replaceAll(/\s/g, '..');
	for (var i = 0; i < c.length; i++) {
		if(c[i]!=""){
			str = str.replaceAll('n' + c[i], 'n.' + c[i]);
		}
	}
	for (var i = 0; i < v.length; i++) {
		str = str.replaceAll(v[i], v[i] + '.');
	}
	str = str.replaceAll('.́', '́.');
	for (var i = 0; i < v.length; i++) {
		str = str.replaceAll('.' + v[i], v[i]);
	}
	str+="."
	str = str.replaceAll('.n.', 'n.');
	str = str.replaceAll('._'," _")
	str = str.replaceAll('_', '._.');
	while(str.indexOf("..") !== -1){
		str = str.replaceAll('..', '.');
	}
	while(str.indexOf("_._") !== -1){
		str = str.replaceAll('_._', '__');
	}
	str = str.replaceAll(' ._',"._")
	while(str.indexOf("..") !== -1){
		str = str.replaceAll('..', '.');
	}
	str = str.slice(0, -1);
	str = str.replaceAll('.́', '́.');
	for (var i = 0; i < v.length; i++) {
		for (var j = 0; j < v.length; j++) {
			if(v[i]!=v[j]){
				str = str.replaceAll(v[i]+v[j],v[i]+"."+v[j]);
				str = str.replaceAll(v[i]+'́'+v[j],v[i]+'́.'+v[j]);
			}
		}
	}
	
	//console.log(str)
	str = str.split('.');
	let words = [ '' ];
	weight = 0;
	for (var i = 0; i < str.length; i++) {
		words[words.length - 1] = words[words.length - 1] + str[i];
		if (s[str[i]] == undefined) {
			return { err: `'${str[i]}' is an invalid syllable`};
		}
		weight = weight + s[str[i]];
		if (weight >= 2) {
			words.push('');
			weight = 0;
		}
	}

	if (weight > 0) {
		return { err: `'${words[words.length - 1]}' is an incomplete word`};
	}

	// remove leftover empty word.
	words.pop();

	return words;
}

// Transform an array of valid hýyban words into a tree.
function parseSentences(text) {
	// Turn all words into objects.
	for(i in text) {
		text[i] = { word: text[i].trim() };
	}

	// First pass.	
	let indexQueue = [];

	for(i in text) {
		// Makes sure all words have an empty children array for second pass.
		text[i].children = [];

		// If length is 0 then this word doesn't have a parent.
		// It is thus the start of a new sentence.
		if(indexQueue.length > 0) {
			text[i].parent = indexQueue.shift();
		}

		if(dictionary[text[i].word] != undefined && dictionary[text[i].word].type == 'prefix') {
			indexQueue.push(i);
		}

		if(dictionary[text[i].word] != undefined && dictionary[text[i].word].type == 'particle') {
			indexQueue.push(i);
			indexQueue.push(i);
		}
	}

	if(indexQueue.length > 0) {
		return { err: `incomplete sentence`};
	}

	// Second reverse pass.
	let sentences = [];
	while(text.length > 0) {
		let word = text.pop();

		if (word.parent == undefined) {
			// No parent = start of sentence. We add it at the start of the
			// sentence array since we're iterating in reverse order.
			sentences.unshift(word);
		} else {
			// Parent = argument of a particle. Reverse order = inserting at
			// start of children array.
			text[word.parent].children.unshift(word);
		}
	}

	return sentences;
}

// Turn apostrophes into accents
function toneMarking(str) {
	str = str.replaceAll("́","'");
    str = str.replaceAll("i","ı");
    str = str.replaceAll("j","ȷ");
    
    str = str.replaceAll("’","'");
    str = str.replaceAll("p'","ṕ");
    str = str.replaceAll("t'","t́");
    str = str.replaceAll("k'","ḱ");
    str = str.replaceAll("b'","b́");
    str = str.replaceAll("d'","d́");
    str = str.replaceAll("g'","ǵ");
    str = str.replaceAll("s'","ś");
	
	str=str.replaceAll("á","á")
	str=str.replaceAll("é","é")
	str=str.replaceAll("í","ı́")
	str=str.replaceAll("ó","ó")
	str=str.replaceAll("ú","ú")
	str=str.replaceAll("ý","ý")
	str=str.replaceAll("ṕ","ṕ")
	str=str.replaceAll("ḱ","ḱ")
	str=str.replaceAll("ǵ","ǵ")
	str=str.replaceAll("ś","ś")

    for (var i = 0; i < v.length; i++) {
      str = str.replaceAll(v[i] + "'", v[i]+"́")
    }

	return str;
}

module.exports.segmenter = segmenter;
module.exports.parseSentences = parseSentences;
module.exports.toneMarking = toneMarking;
