TELUGU_CONSONANTS = [
    'క', 'ఖ', 'గ', 'ఘ', 'ఙ', 'చ', 'ఛ', 'జ', 'ఝ', 'ఞ', 'ట', 'ఠ', 'డ', 'ఢ', 'ణ',
    'త', 'థ', 'ద', 'ధ', 'న', 'ప', 'ఫ', 'బ', 'భ', 'మ', 'య', 'ర', 'ల', 'వ', 'శ',
    'ష', 'స', 'హ', 'ళ', 'ఱ'
]
TELUGU_VOWELS = [
    'అ', 'ఆ', 'ఇ', 'ఈ', 'ఉ', 'ఊ', 'ఋ', 'ౠ', 'ఎ', 'ఏ', 'ఐ', 'ఒ', 'ఓ', 'ఔ'
]
TELUGU_VOWEL_SIGNS = [
    'ా', 'ి', 'ీ', 'ు', 'ూ', 'ృ', 'ౄ', 'ె', 'ే', 'ై', 'ొ', 'ో', 'ౌ'
]
TELUGU_VOWEL_SIGNS_X_POS = ['ా', 'ి', 'ీ', 'ె', 'ే', 'ొ', 'ో', 'ౌ']
TELUGU_VIRAMA = '్'

# Orthographic Syllable Types making up the 200 bi-syllabic words from
# The CIIL corpus
#     I. V/Vm as orthographic syllables # 11
#     II. CVm type of orthographic syllables (with homorganic nasals) # 25
#     III. CV(V) type orthographic syllables (inherent V / vowel modifiers) # 93
#     IV. C1C1V type orthographic syllables (with geminates) #25
#     V. C1C2V type orthographic syllables (with clusters) # 46
# Total = 200

syllable_lists = [
    "అ, ఆ, అం, ఇ, ఇం, ఎ, ఎం, ఉం, ఒ, ఐ",
    "కం, కాం, కిం, కోం, గం, గుం, చెం, టం, డం, తం, పం, బం, నుమ్, ముం, మం, రెం, వం, హిం, హం, రం, శాం, లం, సం, యం, నం",
    "క, కా, ఖ, కె, కే, కొ, కు, కూ; గ, గా, గొ, గో, గు, గూ; చ, చా, చి, చు, చూ, చె, చే; జి, జీ, జు; ట, టి, టీ, టూ, టో; డ, డు, డొ, డే, డి, డు; త, తి, తూ; ద, దా, ధ, ధి, దు, దూ, దే, దో; న, నా, ని, నీ, ను, నే; ప, పా, పూ, పె, పే ; బ, బా, భ, భా, బే, బో; మ, మా, మి, మీ, మే, మొ, ము, మై, యా, యో, ర, రా, రి, రు; ల, లి, లా, లె, లే, లు; ళ, యా, స, సి, వి, వ, వా, వు, సా, హి",
    "న్న, న్ని, న్నీ, మ్మ, ల్లు, చ్చి, ట్టి, క్క, త్తు, ద్ద, న్ను, ళ్ళు, ధ్ధి, త్త, చ్చే, ల్లి, ప్పు, బ్బు, వ్వు, ళ్లు, ప్ప, ట్టు, ళ్ళి, ల్లా, ద్ది",
    "ట్లు, ట్లో, ధ్య, త్రం, ఖ్య, ర్పు, ర్తి, ర్య, ర్చి, ర్చు, స్తే, త్ర, ర్లు, స్త, బ్దం, ర్త, ర్వం, ద్య, క్తం, ట్ల, ర్దు, ర్చి, ర్పు, ప్ర, క, రి, శ్ర, దృ, ప్రే, వ్యా, క్ర, క్రో, స్థి, వృ, ద్వా, జ్ఞా, వ్యా, స్వ, స్ప, ప్రి, త్యా, ప్రా, గ్రా, వ్రా, శ్నా, త్రం, క్తి",
]

class Dictionary:

    def __init__(self, filename):
        self.words = open(filename).read().splitlines()
        self.words = [word.strip() for word in self.words]
        self.words = set(self.words)

    def is_word(self, word: str):
        return word in self.words


def generate_orthographic_neighbors(word: str):
    '''change a single vowel sign'''
    neighbors = []
    for i in range(len(word)):
        if word[i] in TELUGU_VOWEL_SIGNS_X_POS:
            for vowel_sign in TELUGU_VOWEL_SIGNS_X_POS:
                if word[i] != vowel_sign:
                    neighbors.append(word[:i] + vowel_sign + word[i + 1:])
    return neighbors


def generate_phonological_neighbors(word: str):
    '''change a single consonant, but not after a virama'''
    neighbors = []
    for i in range(len(word)):
        if word[i] in TELUGU_CONSONANTS:
            if i == 0 or word[i - 1] != TELUGU_VIRAMA:
                for consonant in TELUGU_CONSONANTS:
                    if word[i] != consonant:
                        neighbors.append(word[:i] + consonant + word[i + 1:])
    return neighbors


def print_neighbors(word: str, file):
    '''print all possible neighbors for a word, ensuring they are valid words'''
    file.write('Word: ' + word + '\n')
    ONs = generate_orthographic_neighbors(word)
    ONs = [neighbor for neighbor in ONs if dictionary.is_word(neighbor)]
    ONs = [w for w in ONs if w != word]
    file.write(f'Orthographic Neighbors ({len(ONs)}):\n')
    file.write('\n'.join(ONs) + '\n')

    PNs = generate_phonological_neighbors(word)
    PNs = [neighbor for neighbor in PNs if dictionary.is_word(neighbor)]
    ONs = [w for w in PNs if w != word]
    file.write(f'\nPhonological Neighbors ({len(PNs)}):\n')
    file.write('\n'.join(PNs) + '\n')

    file.write('\n' + '_' * 30 + '\n\n')

# with open('test_output.txt','w') as f:
#     dictionary = Dictionary('dicts/telugu.lemma.txt.dict')
#     word = 'పాలు'
#     print_neighbors(word, f)
#     word = 'పెద్ద'
#     print_neighbors(word, f)
#     word = 'కొంచెం'
#     print_neighbors(word, f)
#     word = 'ముద్దు'
#     print_neighbors(word, f)

if __name__ == '__main__':
    dictionary = Dictionary('dicts/telugu.lemma.txt.dict')

    import json
    output_path = 'output4.txt'
    with open('word_syllable_structures.json') as input_file:
        with open(output_path, 'w') as output_file:
            data = json.load(input_file)
            for category in data:
                output_file.write(f'Category: {category}\n')
                for word in data[category]:
                    print_neighbors(word, output_file)

    print('Output written to', output_path)
