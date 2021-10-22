const { segmenter, parseSentences, toneMarking } = require('../src/parser.js');
const dictionary = require('../../dictionary/en.yaml');
const { ipa_converter } = require('../src/dictionary');

// Triggered at page loading or when input is updated.
export function parse() {
    let text = $('#input_textarea').val();
    
    text = toneMarking(text);
    $('#input_textarea').val(text);

    text = text.trim().toLowerCase().replaceAll('i', 'ı').replaceAll('j', 'ȷ');

    if (text == '') {
        $('#parse-result-tree').html(`Type some text to parse.`);
        return;
    }

    let segmented = segmenter(text);
    if(segmented.err != undefined) {
        $('#parse-result-tree').html(`Morphology error: ${segmented.err}`);
        return;
    }

    let sentences = parseSentences(segmented);
    if(sentences.err != undefined) {
        $('#parse-result-tree').html(`Parse tree error: ${sentences.err}`);
        return;
    }

	let output = `<small>`+ipa_converter(text)+`</small>`
    output += "<ul>";
    sentences.forEach(sentence => {
        output += nodeToHtml(sentence);
    })
    output += `</ul>`;
    
    $('#parse-result-tree').html(output);
}

function nodeToHtml(node) {
    let output = `<li>`;

    output += `<b>${node.word} `;

    if(dictionary[node.word] != undefined) {
        let entry = dictionary[node.word];
        output += `<small>(${entry.type})</small> : </b> ${entry.short}`;
    } else {
        output += `:</b> <i>unknown word</i>`
    }

    if(node.children.length > 0) {
        output += `<ul>`;
        node.children.forEach(child => {
            output += nodeToHtml(child);
        })
        output += `</ul>`;
    }

    output += `</li>`;

    return output;
}
