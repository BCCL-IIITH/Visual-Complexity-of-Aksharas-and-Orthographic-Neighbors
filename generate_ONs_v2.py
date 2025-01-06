TELUGU_CONSONANTS = [
    'క', 'ఖ', 'గ', 'ఘ', 'ఙ', 'చ', 'ఛ', 'జ', 'ఝ', 'ఞ', 'ట', 'ఠ', 'డ', 'ఢ', 'ణ',
    'త', 'థ', 'ద', 'ధ', 'న', 'ప', 'ఫ', 'బ', 'భ', 'మ', 'య', 'ర', 'ల', 'వ', 'శ',
    'ష', 'స', 'హ', 'ళ', 'ఱ'
]
TELUGU_VOWELS = [
    'అ', 'ఆ', 'ఇ', 'ఈ', 'ఉ', 'ఊ', 'ఋ', 'ౠ', 'ఎ', 'ఏ', 'ఐ', 'ఒ', 'ఓ', 'ఔ'
]
TELUGU_VOWEL_SIGNS = [
    '', 'ా', 'ి', 'ీ', 'ు', 'ూ', 'ృ', 'ౄ', 'ె', 'ే', 'ై', 'ొ', 'ో', 'ౌ'
]
TELUGU_VOWEL_SIGNS_X_POS = ['ా', 'ి', 'ీ', 'ె', 'ే', 'ొ', 'ో', 'ౌ']
TELUGU_VOWEL_SIGNS_Y_POS = ['ృ', 'ౄ', 'ై']
TELUGU_VOWEL_SIGNS_Z_POS = ['ు', 'ూ']
TELUGU_VIRAMA = '్'
TELUGU_ANUSVARA = 'ం'

SYLLABLE_SETS_VASANTA = {
    # TODO
}

SYLLABLE_SETS_bak = {
    '.V':
    TELUGU_VOWELS,
    'V':
    TELUGU_VOWEL_SIGNS,
    '.Vm': [v + TELUGU_ANUSVARA for v in TELUGU_VOWELS],
    'Vm': [v + TELUGU_ANUSVARA for v in TELUGU_VOWEL_SIGNS],
    'C1C1': [c1 + TELUGU_VIRAMA + c1 for c1 in TELUGU_CONSONANTS],
    'C1C2': [
        c1 + TELUGU_VIRAMA + c2 for c1 in TELUGU_CONSONANTS
        for c2 in TELUGU_CONSONANTS
    ],
    'C1':
    TELUGU_CONSONANTS,
}

SYLLABLE_SETS = {
    '.V':
    TELUGU_VOWELS + [v + TELUGU_ANUSVARA for v in TELUGU_VOWELS],
    'V':
    TELUGU_VOWEL_SIGNS + [v + TELUGU_ANUSVARA for v in TELUGU_VOWEL_SIGNS],
    '.Vm':
    TELUGU_VOWELS + [v + TELUGU_ANUSVARA for v in TELUGU_VOWELS],
    'Vm':
    TELUGU_VOWEL_SIGNS + [v + TELUGU_ANUSVARA for v in TELUGU_VOWEL_SIGNS],
    'C1C1': [c1 + TELUGU_VIRAMA + c1 for c1 in TELUGU_CONSONANTS] + [
        c1 + TELUGU_VIRAMA + c2 for c1 in TELUGU_CONSONANTS
        for c2 in TELUGU_CONSONANTS
    ],
    'C1C2': [c1 + TELUGU_VIRAMA + c1 for c1 in TELUGU_CONSONANTS] + [
        c1 + TELUGU_VIRAMA + c2 for c1 in TELUGU_CONSONANTS
        for c2 in TELUGU_CONSONANTS
    ],
    'C1': [c1 + TELUGU_VIRAMA + c1 for c1 in TELUGU_CONSONANTS] + [
        c1 + TELUGU_VIRAMA + c2 for c1 in TELUGU_CONSONANTS
        for c2 in TELUGU_CONSONANTS
    ],
}

SYLLABLE_SETS = SYLLABLE_SETS_bak

syllable_lists = "అ, ఆ, అం, ఇ, ఇం, ఎ, ఎం, ఉం, ఒ, ఐ, కం, కాం, కిం, కోం, గం, గుం, చెం, టం, డం, తం, పం, బం, నుమ్, ముం, మం, రెం, వం, హిం, హం, రం, శాం, లం, సం, యం, నం, క, కా, ఖ, కె, కే, కొ, కు, కూ, గ, గా, గొ, గో, గు, గూ, చ, చా, చి, చు, చూ, చె, చే, జి, జీ, జు, ట, టి, టీ, టూ, టో, డ, డు, డొ, డే, డి, డు, త, తి, తూ, ద, దా, ధ, ధి, దు, దూ, దే, దో, న, నా, ని, నీ, ను, నే, ప, పా, పూ, పె, పే , బ, బా, భ, భా, బే, బో, మ, మా, మి, మీ, మే, మొ, ము, మై, యా, యో, ర, రా, రి, రు, ల, లి, లా, లె, లే, లు, ళ, యా, స, సి, వి, వ, వా, వు, సా, హి, న్న, న్ని, న్నీ, మ్మ, ల్లు, చ్చి, ట్టి, క్క, త్తు, ద్ద, న్ను, ళ్ళు, ధ్ధి, త్త, చ్చే, ల్లి, ప్పు, బ్బు, వ్వు, ళ్లు, ప్ప, ట్టు, ళ్ళి, ల్లా, ద్ది, ట్లు, ట్లో, ధ్య, త్రం, ఖ్య, ర్పు, ర్తి, ర్య, ర్చి, ర్చు, స్తే, త్ర, ర్లు, స్త, బ్దం, ర్త, ర్వం, ద్య, క్తం, ట్ల, ర్దు, ర్చి, ర్పు, ప్ర, క, రి, శ్ర, దృ, ప్రే, వ్యా, క్ర, క్రో, స్థి, వృ, ద్వా, జ్ఞా, వ్యా, స్వ, స్ప, ప్రి, త్యా, ప్రా, గ్రా, వ్రా, శ్నా, త్రం, క్తి".split(
    ', ')

# # print(len(set(syllable_lists)))

# # print frequencies of aksharas
# from collections import Counter
# akshara_counts = Counter(syllable_lists)
# print(akshara_counts)

# exit()


class Dictionary:

    def __init__(self, filename):
        self.filename = filename
        self.words = open(filename).read().splitlines()
        self.words = [word.strip() for word in self.words]
        self.words = set(self.words)

    def is_word(self, word: str):
        return word in self.words


def infer_syllable_structure(word: str, return_breakup=False):
    '''infer the syllable structure of a word'''
    syllable_structure = ''
    syllable_breakup = ''
    consonant_index = {}
    i = 0
    while i < len(word):
        if word[i] in TELUGU_CONSONANTS:
            if i > 0 and (word[i - 1] in TELUGU_VOWEL_SIGNS or word[i - 1]
                          in TELUGU_VOWELS or word[i - 1] in TELUGU_CONSONANTS
                          or word[i - 1] == TELUGU_ANUSVARA):
                syllable_structure += '.'  # syllable boundary
                syllable_breakup += '.'
                consonant_index = {}  # reset consonant index
            if word[i] not in consonant_index:
                consonant_index[word[i]] = len(consonant_index) + 1
            index = consonant_index[word[i]]
            syllable_structure += f'C{index}V'
        elif word[i] in TELUGU_VOWELS or word[i] in TELUGU_VOWEL_SIGNS:
            if i > 0 and word[i - 1] in TELUGU_CONSONANTS:
                pass  # inherent vowel 'a'
            else:
                syllable_structure += 'V'
        elif word[i] == TELUGU_ANUSVARA:
            syllable_structure += 'm'
        elif word[i] == TELUGU_VIRAMA:
            syllable_structure = syllable_structure[:-1]
        elif word[i] == ' ':
            syllable_structure += '. '
        else:
            raise ValueError(f'Unknown character: {word[i]}')
        syllable_breakup += word[i]
        # print(word[i], syllable_structure, syllable_breakup)
        i += 1

    if return_breakup:
        return syllable_structure, syllable_breakup
    return syllable_structure


def test_infer_syllable_structure():
    tests = {
        'V.C1V':
        'ఒక, అని, ఇది, అది, అనే, అవి, ఇవి, అను, ఒకే, ఆమె, ఇలా, అదే, అలా, ఎలా, ఏదో, అతి, ఆయా, ఇక, ఇదే, ఏమి, ఆరు, ఏది, అటు, ఆట, ఐదు',
        'V.C1C1V': 'ఎన్ని, అన్నీ, అమ్మ, ఇల్లు, ఇచ్చి, ఒక్క, ఇట్టి, ఎత్తు',
        'V.C1C2V': 'ఇట్లు',
        'C1Vm.C1V':
        'రెండు, నుంచి, ముందు, కొంత, వంట, మంది, కింది, కాంతి, కంటే, రెండో, రంగు, చెంది, బంతి, శాంతి, ముందే, హిందీ, గుండె, పంట, మందు',
        'C1V.C1Vm': 'కాలం, భాగం, శతం, పటం, దూరం, పాపం',
        'C1V.C1C1V':
        'పెద్ద, యొక్క, చిన్న, వచ్చి, బట్టి, కొత్త, దాన్ని, వచ్చే, వద్ద, తల్లి, తప్పు, డబ్బు, నువ్వు, గొప్ప, పెట్టి, చుట్టూ, పన్ను, మొక్క, చెప్పు, జిల్లా, నన్ను, నిన్ను',
        'C1V.C1C2V':
        'దృష్టి, వృద్ధి, మధ్య, శక్తి, ముఖ్య, మార్పు, పూర్తి, చర్య, గూర్చి, ఖర్చు, చూస్తే, భార్య, పాత్ర, సార్లు, కాస్త, పేర్లు, భర్త, విద్య, పట్ల, బోర్డు, మార్చి, తూర్పు, వస్తే',
        'C1V.C1C2Vm': 'పూర్వం, మాత్రం, శబ్దం, రక్తం',
        'C1V.C1V':
        'తన, మన, తమ, పని, తల, తను, మైనా, పది, గత, కవి, ములు, మత, విని, వలె, కొని, మని, నది, పడి, ధర, గదా, సరి, పద, కళ, కల, సమ',
        'C1C2V.C1V': 'ప్రతి, శ్రమ, ప్రేమ, వ్యాధి, స్థితి, ద్వారా, ప్రభ, వ్రాత',
        'C1C2Vm.C1V': 'క్రింది',
        'C1C2Vm.C1Vm': 'ప్రాంతం',
        'C1C2V.C1Vm': 'స్వయం, క్రమం, జ్ఞానం, త్యాగం, ప్రాయం, గ్రహం, న్యాయం',
        'C1C2V.C1C2V': 'ప్రశ్న, వ్యాప్తి, వ్యక్తి, ప్రాప్తి',
        'C1C2V.C1C1V': 'క్రొత్త',
        'C1C2V.C1C2Vm': 'స్పష్టం',
    }

    for syllable_structure, words in tests.items():
        for word in words.split(', '):
            assert infer_syllable_structure(word) == syllable_structure, word


def generate_syllable_set(syllable_type: str):
    '''generate all possible syllables of a given type'''

    from itertools import product
    import re

    # break down syllable type into components
    syllable_parts = re.subn(r'(C1C1|C1C2|C1|Vm|\wం)', r'.\1.',
                             syllable_type)[0]
    syllable_parts = syllable_parts.split('.')
    syllable_parts = [part for part in syllable_parts if part != '']

    print('  syllable parts', syllable_parts)

    syllable_set = []
    for syllable_part in syllable_parts:
        if syllable_type[0] == 'V':
            syllable_part = '.' + syllable_part

        if syllable_part in SYLLABLE_SETS:
            # syllable_set.append(syllable_lists)
            syllable_set.append(SYLLABLE_SETS[syllable_part])
        else:
            syllable_set.append([syllable_part])

        print('    ', syllable_part, '=', len(syllable_set[-1]))

    # syllable_set.append(syllable_lists)

    return [''.join(syllable) for syllable in product(*syllable_set)]


def print_list_head(list, n=10):
    print(', '.join(list[:n]), '...' if len(list) > n else '')


def generate_all_words_from_syllable_structure(syllable_structure: str):
    '''generate all possible words from a syllable structure'''
    from itertools import product

    syllable_types = syllable_structure.split('.')

    syllable_sets = [
        generate_syllable_set(syllable_type)
        for syllable_type in syllable_types
    ]
    print('syllable types', syllable_types)
    print('syllable set sizes', [len(x) for x in syllable_sets])

    words = [''.join(syllable) for syllable in product(*syllable_sets)]
    print('total potential words', len(words))

    print_list_head(words)

    return words


def generate_orthographic_neighbors(word: str):
    '''addition, deletion, substitution'''

    import re

    syllable_structure, syllable_breakup = infer_syllable_structure(
        word, return_breakup=True)
    syllable_types = syllable_structure.split('.')
    syllables = syllable_breakup.split('.')

    print('syllable structure', syllable_structure)
    print('syllable breakup', syllable_breakup)

    neighbors = []

    def generate_for_new_structure(syllable_types: list, replacement: str,
                                   index: int):
        new_structure = syllable_types.copy()
        new_structure[index] = replacement
        new_structure = '.'.join(new_structure)

        print(f'{syllable_breakup} ({syllable_structure}) -> {new_structure}')
        new_neighbors = generate_all_words_from_syllable_structure(
            new_structure)
        print_pruned_words(new_neighbors)
        neighbors.extend(new_neighbors)
        print('-' * 20)

    def generate_by_substitution(syllable_types: list, replacement: str,
                                 index: int):
        new_structure = syllable_types.copy()
        new_structure[index] = replacement
        new_structure = '.'.join(new_structure)

        print(f'{syllable_breakup} ({syllable_structure}) -> {new_structure}')
        new_neighbors = generate_all_words_from_syllable_structure(
            new_structure)
        print_pruned_words(new_neighbors)
        neighbors.extend(new_neighbors)
        print('-' * 20)

    for i, (syllable_type,
            syllable) in enumerate(zip(syllable_types, syllables)):
        # ---- SUBSTITUTION ----
        new_syllable = syllable
        # keep ith syllable same
        print(f'by keeping syllable "{new_syllable}" same')
        generate_for_new_structure(syllable_types, new_syllable, i)

        # ---- ADDITION ----
        new_syllable = syllable
        # add anusvara after vowel
        if 'V' in syllable_type and 'Vm' not in syllable_type:
            for consonant in TELUGU_CONSONANTS:
                new_syllable = re.subn(
                    rf'{consonant}(?!{TELUGU_ANUSVARA}|{TELUGU_VIRAMA}{TELUGU_ANUSVARA})',
                    rf'{consonant}{TELUGU_ANUSVARA}', new_syllable)[0]

            # ensure Vm + virama -> Vm
            new_syllable = re.subn(rf'{TELUGU_ANUSVARA}{TELUGU_VIRAMA}',
                                   rf'{TELUGU_VIRAMA}', new_syllable)[0]

            # ensure Vm + V -> V, Vm + Vm -> Vm
            for vowel in TELUGU_VOWELS + TELUGU_VOWEL_SIGNS:
                if vowel != '':  # check if not vowel sign for 'a'
                    new_syllable = re.subn(rf'{TELUGU_ANUSVARA}{vowel}',
                                           rf'{vowel}', new_syllable)[0]

            # ensure V -> Vm and also Vm -> Vm
            for vowel in TELUGU_VOWELS + TELUGU_VOWEL_SIGNS:
                if vowel != '':  # check if not vowel sign for 'a'
                    new_syllable = re.subn(rf'{vowel}(?!{TELUGU_ANUSVARA})',
                                           rf'{vowel}{TELUGU_ANUSVARA}',
                                           new_syllable)[0]
            # print(new_syllable)
            print('by adding anusvara after vowel')
            generate_for_new_structure(syllable_types, new_syllable, i)

        # ---- DELETION ----
        new_syllable = syllable
        # remove anusvara after vowel
        if 'Vm' in syllable_type:
            new_syllable = new_syllable.replace(TELUGU_ANUSVARA, '')
            print('by deleting anusvara after vowel')
            generate_for_new_structure(syllable_types, new_syllable, i)

        new_syllable = syllable
        # remove C2 from C1C2
        if 'C1C2' in syllable_type:
            new_syllable = re.subn(rf'(\w){TELUGU_VIRAMA}(\w)', rf'\1',
                                   new_syllable)[0]
            print('by deleting C2 from C1C2')
            generate_for_new_structure(syllables, new_syllable, i)

    return neighbors


def print_neighbors(word: str, file=None):
    '''print all possible neighbors for a word, ensuring they are valid words'''

    if file is None:
        import sys
        file = sys.stdout

    file.write('Word: ' + word + '\n')
    ONs_all = generate_orthographic_neighbors(word)
    for dict_name, pruned_words in prune_words(ONs_all):
        ONs = [w for w in pruned_words if w != word]
        file.write(
            f'Orthographic Neighbors ({len(ONs)}) (dict: {dict_name}):\n')
        file.write('\n'.join(ONs) + '\n')

    file.write('\n' + '-' * 30 + '\n\n')


def prune_words(words: list):
    '''prune words that are not in the dictionary'''
    dict_words = []
    for dictionary in dictionaries:
        words = [word for word in words if dictionary.is_word(word)]
        dict_words.append((dictionary.filename, words))
    return dict_words


def print_pruned_words(words: list):
    for dict_name, pruned_words in prune_words(words):
        print(dict_name, len(pruned_words))
        print_list_head(pruned_words)


if __name__ == '__main__':
    dictionaries = [
        # Dictionary('dicts/telugu.lemma.txt.dict'),
        # Dictionary('dicts/telugu.lex.txt.dict'),
        # Dictionary('dicts/sortdict.txt.dict'),
        # Dictionary('dicts/test.txt.dict'),
        # Dictionary('dicts/dictionary.sqlite.dict'),
        Dictionary('dicts/cpbrown.txt.dict'),
    ]

    # print(infer_syllable_structure('ఎన్ని'))
    # print_pruned_words(generate_all_words_from_syllable_structure('C1V.C1V'))
    # print_pruned_words(
    #     generate_all_words_from_syllable_structure('C1C2V.C1C2Vm'))
    # print_neighbors('ఇంత')
    # print_neighbors('ఒక')
    # print_neighbors('మార్పు')
    # print_neighbors('పూర్వం')
    # print_neighbors('వ్యక్తి')

    # print_pruned_words(
    #     ['ఎన్ని', 'అన్నీ', 'అమ్మ', 'ఇల్లు', 'ఇచ్చి', 'ఒక్క', 'ఇట్టి', 'ఎత్తు'])
    # import json
    # output_path = 'output_all_dicts_28aug.txt'
    # with open('word_syllable_structures.json') as input_file:
    #     with open(output_path, 'w') as output_file:
    #         data = json.load(input_file)
    #         for category in data:
    #             output_file.write(f'Category: {category}\n')
    #             for word in data[category]:
    #                 print_neighbors(word, output_file)

    # print('Output written to', output_path)

    # ---

    # two_hundred_words = 'ఒక, అని, ఇది, అది, అనే, అవి, ఇవి, అను, ఒకే, ఆమె, ఇలా, అదే, అలా, ఎలా, ఏదో, అతి, ఆయా, ఇక, ఇదే, ఏమి, ఆరు, ఏది, అటు, ఆట, ఐదు, ఎన్ని, అన్నీ, అమ్మ, ఇల్లు, ఇచ్చి, ఒక్క, ఇట్టి, ఎత్తు, ఇట్లు, రెండు, నుంచి, ముందు, కొంత, వంట, మంది, కింది, కాంతి, కంటే, రెండో, రంగు, చెంది, బంతి, శాంతి, ముందే, హిందీ, గుండె, పంట, మందు, కాలం, భాగం, శతం, పటం, దూరం, పాపం, పెద్ద, యొక్క, చిన్న, వచ్చి, బట్టి, కొత్త, దాన్ని, వచ్చే, వద్ద, తల్లి, తప్పు, డబ్బు, నువ్వు, గొప్ప, పెట్టి, చుట్టూ, పన్ను, మొక్క, చెప్పు, జిల్లా, నన్ను, నిన్ను, దృష్టి, వృద్ధి, మధ్య, శక్తి, ముఖ్య, మార్పు, పూర్తి, చర్య, గూర్చి, ఖర్చు, చూస్తే, భార్య, పాత్ర, సార్లు, కాస్త, పేర్లు, భర్త, విద్య, పట్ల, బోర్డు, మార్చి, తూర్పు, వస్తే, పూర్వం, మాత్రం, శబ్దం, రక్తం, తన, మన, తమ, పని, తల, తను, మైనా, పది, గత, కవి, ములు, మత, విని, వలె, కొని, మని, నది, పడి, ధర, గదా, సరి, పద, కళ, కల, సమ, ప్రతి, శ్రమ, ప్రేమ, వ్యాధి, స్థితి, ద్వారా, ప్రభ, వ్రాత, క్రింది, ప్రాంతం, స్వయం, క్రమం, జ్ఞానం, త్యాగం, ప్రాయం, గ్రహం, న్యాయం, ప్రశ్న, వ్యాప్తి, వ్యక్తి, ప్రాప్తి, క్రొత్త, స్పష్టం'.split(
    #     ', ')

    # d = Dictionary('dicts/cpbrown_meanings.txt.dict')
    # wordlist = d.words

    # two_syllable_words = []
    # for word in wordlist:
    #     try:
    #         if len(infer_syllable_structure(word).split('.')) == 2:
    #             two_syllable_words.append(word)
    #     except:
    #         pass

    # # print(*sorted(two_syllable_words), sep='\n')
    # # print(len(two_syllable_words))

    # count=0
    # for word in two_hundred_words:
    #     if word not in wordlist:
    #         print(word)
    #         count+=1

    # print(count)