const words = require('../../dictionary/en.yaml');

// Valid consonants list.
const c = 'bcdfghjklmnpqrstvwxz ';

// Consonants weights.
const cw = '101010001110110011011';

// Valid vowels list.
const v = 'aeiouyáéíóúý';

// Vowels weights.
const vw = '111000111000';

// Building a map of the weight for all possible syllable forms.
let s = {};
for (var i = 0; i < c.length; i++) {
	for (var j = 0; j < v.length / 2; j++) {
		s[c[i] + v[j]] = parseInt(cw[i]) + parseInt(vw[j]);
		s[c[i] + v[j] + 'n'] = parseInt(cw[i]) + parseInt(vw[j]) + 1;

		s[c[i] + v[j + v.length / 2]] = parseInt(cw[i]) + parseInt(vw[j]);
		s[c[i] + v[j + v.length / 2] + 'n'] = parseInt(cw[i]) + parseInt(vw[j]) + 1;

		s[c[i] + v[j] + v[j + v.length / 2]] = parseInt(cw[i]) + parseInt(vw[j]) + 1;
		s[c[i] + v[j] + v[j + v.length / 2] + 'n'] = parseInt(cw[i]) + parseInt(vw[j]) + 2;

		s[c[i] + v[j + v.length / 2] + v[j]] = parseInt(cw[i]) + parseInt(vw[j]) + 1;
		s[c[i] + v[j + v.length / 2] + v[j] + 'n'] = parseInt(cw[i]) + parseInt(vw[j]) + 2;
	}
}

// Takes a string as input and returns a list of words.
function segmenter(str) {
	str = ' ' + str + ' ';
	str = str.replaceAll(/\s/g, ' ');
	for (var i = 0; i < c.length; i++) {
		str = str.replaceAll('n' + c[i], 'n.' + c[i]);
	}
	for (var i = 0; i < c.length; i++) {
		str = str.replaceAll('n' + c[i], 'n.' + c[i]);
	}
	for (var i = 0; i < v.length; i++) {
		str = str.replaceAll(' ' + v[i], '?' + v[i]);
	}
	str = str.replaceAll(/\s/g, '');
	for (var i = 0; i < v.length; i++) {
		str = str.replaceAll(v[i], v[i] + '.');
	}
	for (var i = 0; i < v.length; i++) {
		str = str.replaceAll('.' + v[i], v[i]);
	}
	str = str.replaceAll('.n.', 'n.');
	str = str.slice(0, -1);
	str = str.replaceAll('?', ' ');
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
	console.log(weight);
	if (weight > 0) {
		return { err: `'${words[words.length - 1]}' is an incomplete word`};
	}
	return words;
}

module.exports.segmenter = segmenter;