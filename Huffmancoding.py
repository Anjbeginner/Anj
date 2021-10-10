huff_tree = {}

# Huffman Coding in python

string = ("NameJames C. MaxwellBirth DateJune 13, 1831Death DateNovember 5, 1879Did You Know?Optics innovator "
          "James C. Maxwell took the first color photograph in 1861, specifically of a tartan ribbon. "
          "EducationUniversity of Cambridge, King's College London, Marischal College, University of Edinburgh, "
          "Edinburgh AcademyPlace of BirthEdinburgh, Scotland, United KingdomPlace of DeathCambridge, England, "
          "United KingdomAKAJames C. MaxwellJames MaxwellNicknameFather of Modern PhysicsFull NameJames Clerk "
          "MaxwellQUOTES1 of 2\“We have strong reason to conclude that light itself—including radiant heat and "
          "other radiation, if any—is an electromagnetic disturbance in the form of waves propagated through the "
          "electromagnetic field according to electromagnetic laws.\”—James C. MaxwellJames C. Maxwell Biography"
          "(1831–1879)James C. Maxwell was a 19th-century pioneer in chemistry and physics who articulated the "
          "idea of electromagnetism.Who Was James C. Maxwell?James C. Maxwell studied at the University of "
          "Cambridge before holding a variety ofprofessorship posts. Already known for his innovations in optics"
          "and gas velocity research, his groundbreaking theories around electromagnetism, articulated in the famed"
          "Maxwell's Equations, greatly influenced modern physics as we know it.Academic BackgroundJames Clerk "
          "Maxwell was born on June 13, 1831, in Edinburgh, Scotland. Having a keen intellect from childhood, "
          "he had one of his geometry papers presented at the Royal Society of Edinburgh during his adolescence. "
          "By 16 he'd enrolled at the University of Edinburgh, pursuing a fervent interest in optics and color "
          "research. He studied there for three years and eventually attended Cambridge University's Trinity College,"
          "graduating in 1854.After teaching at Trinity for a time, Maxwell moved on to Marischal College as part of "
          "the physics faculty. He wed Katherine Mary Dewar in 1858.Saturn's RingsWhile at Marischal, Maxwell "
          "pondered a major astronomical question, looking at the case of Saturn and coming up with the idea that "
          "the planet's rings are comprised of particles, a theory later confirmed via 20th-century space probes. "
          "For this, Maxwell received the Adam Prize.Upon Marischal becoming part of the University of Aberdeen, "
          "Maxwell took on a professor position at King's College in London. He taught there until 1865 when he "
          "resigned from his post to do research from his home in Glenlair. Having continued to do work with "
          "Cambridge University as well, Maxwell was instrumental in helping to establish the institution's "
          "Cavendish Laboratory, and he took on roles there as lab director and professor of experimental "
          "physics at the start of the 1870s.Pioneer in ElectromagnetismMaxwell had continued his research on "
          "color and made ground breaking discoveries around gas velocity. It was during Maxwell's time at King's "
          "College that he began to share revolutionary ideas around electromagnetism and light.Fellow physicist "
          "Michael Faraday had already championed the notion that electricity and magnetics were connected; Maxwell, "
          "via experimentation with vortexes, expanded on Faraday'sork and came up with the theory of electromagnetic"
          "movement being conceptualized in the form of waves, with said energy traveling at light speed.Maxwell's "
          "EquationsSupporting his theorems, Maxwell's Equations—speaking to the scholar's aptitude in using math "
          "to articulate scientific occurrences—were found in the paper \"Dynamical theory of the electromagnetic "
          "field,\" presented to the Royal Society of London in 1864 and published the following year. In 1873 he "
          "published the book A Treatise on Electricity and Magnetism, which further expounded on his research. "
          "Maxwell's other scientific contributions included producing the first color photograph, taken in 1861, "
          "and creating structural engineering calculations for bridge maintenance. He earned an array of awards "
          "over the course of his career, including the Rumford Medal, Keith Prize and Hopkins Prize, in addition "
          "to receiving membership in groups like the Royal Academy of Sciences of Amsterdam. Other publications "
          "included Theory of Heat (1871) and Matter and Motion(1877).Death and LegacyMaxwell died in Cambridge, "
          "England, on November 5, 1879, from abdominal cancer. His discoveries paved the way for much of the modern "
          "world's technological innovations and continued to influence physics well into the next century, with "
          "thinkers like Albert Einstein praising him for his indispensable contributions. Maxwell's original house, "
          "now a museum, is the site of the James Clerk Maxwell Foundation.")


# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '1'))
    d.update(huffman_code_tree(r, False, binString + '0'))
    return d


# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])
sym_prob = {}
total = 0
print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    huff_tree[char] = huffmanCode[char]
    total += frequency
    sym_prob[char] = frequency
    print(' %-4r |%12s' % (char, huffmanCode[char]))
for i in sym_prob.keys():
    sym_prob[i] = sym_prob[i] / total

print("{:<10} {:<10}".format('SYMBOL', 'PROBABILITY'))

for key, value in sym_prob.items():
    probabilty = value
    symbol = key
    print("{:<10} {:<10}".format(symbol, probabilty))

# print(huff_tree)
avg_code_length = 0
my_name = "Anjana Lakshmi"
my_r_no = "cb.en.u4ece18008"
my_name_encode = ""
my_r_no_encode = ""
for i in my_name:
    my_name_encode += huff_tree[i]
for i in my_r_no:
    my_r_no_encode += huff_tree[i]

print("encoding of my name - Anjana lakshmi")
print(my_name_encode)

print("encoding of my roll number - cb.en.u4ece18008")
print(my_r_no_encode)
