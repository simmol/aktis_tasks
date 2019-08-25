class MouseType:
    animal = 'animal'
    computer_mouse = 'computer-mouse'


# Simple word dicts that contain words that are likely to describe one or the other
# For filling this data in more real life scenario learning data can be provided and words extracted from real documents.
concrete_matches = {
    MouseType.animal: ['rodent', 'tail', 'genome', 'species', 'breeding', 'ears', 'rat', 'sanitation', 'sleep',
                       'evolution', 'house mouse', 'on mouse'],
    MouseType.computer_mouse: ['device', 'USB', 'computer', 'object', 'keyboard']
}


def check_by_common_words(mouse_type, sentence):
    for word in concrete_matches[mouse_type]:
        if word.lower() in sentence.lower():
            return mouse_type


def mouse_vs_mouse(sentence):
    for word in concrete_matches[MouseType.animal]:
        if word.lower() in sentence.lower():
            return MouseType.animal

    for word in concrete_matches[MouseType.computer_mouse]:
        if word.lower() in sentence.lower():
            return MouseType.computer_mouse

    # If not sure most likely will be animal
    return MouseType.computer_mouse


def mouse_vs_mouse_from_file(file_name):
    with open(file_name) as f:
        number_of_lines = int(f.readline())

        for x in range(0, number_of_lines):
            result = mouse_vs_mouse(f.readline())
            print(result)
