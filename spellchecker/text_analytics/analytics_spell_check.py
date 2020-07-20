
import pkg_resources
from symspellpy.symspellpy import SymSpell, Verbosity
import spacy 

nlp = spacy.load('en_core_web_lg')
def check_spelling(content):
    # maximum edit distance per dictionary precalculation
    max_edit_distance_dictionary = 2 
    prefix_length = 7
    # create object
    sym_spell = SymSpell(max_edit_distance_dictionary, prefix_length)
    # load dictionary
    dictionary_path = pkg_resources.resource_filename(
        "symspellpy", "frequency_dictionary_en_82_765.txt")
    bigram_path = pkg_resources.resource_filename(
        "symspellpy", "frequency_bigramdictionary_en_243_342.txt")
    # term_index is the column of the term and count_index is the
    # column of the term frequency
    if not sym_spell.load_dictionary(dictionary_path, term_index=0,
                                     count_index=1):
        print("Dictionary file not found")
        return
    # print("words",sym_spell._words)
    # if not sym_spell.load_bigram_dictionary(dictionary_path, term_index=0,
    #                                         count_index=2):
    #     print("Bigram dictionary file not found")
    #     return

    # result = sym_spell.word_segmentation(content,max_edit_distance=0,max_segmentation_word_length=None,ignore_token=None)
    # display suggestion term, term frequency, and edit distance
    # print("{}, {}, {}".format(result.corrected_string, result.distance_sum,
    #                           result.log_prob_sum))
    # print("corrrectedstring",result.corrected_string)
    doc = nlp(content)
    suggest = {}
    for word in doc:
        print("content",word.text)
        suggestions = sym_spell.lookup(word.text, Verbosity.TOP, max_edit_distance = 2, include_unknown=False)
        for suggestion in  suggestions:
            if suggestion._distance > 0:
                suggest[word.text] = suggestion._term
                # print("sugg",suggestion,suggestion._term,type(suggestion))

    print(suggest)
    return suggest
if __name__ == "__main__":
    content = """whereis th elove hehad dated forImuch of thepast who "
                  "couqdn'tread in sixtgrade and ins pired him arunkumar """
    content1 = "arunkumar"
    cont ="""word_segmentation divides a string into words by inserting missing spaces at the appropriate positions misspelled words are corrected and do not affect segmentation existing spaces are allowed and considered for optimum segmentation
"""
    check_spelling(content)