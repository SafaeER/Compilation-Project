from ply import yacc

# Import the tokens from the lexer
from lex1 import tokens  # Replace 'your_new_lex' with the actual name of your lexer file

# Grammar rules
def p_proverb(p):
    '''
    proverb :
            | MOBTADAE1 MOBTADAE2 khabar12
            | DARFZAMAN FI3L1 FA3IL1 FI3L2 FA3IL2
            | MOBTADAE3 HARFJAR ISMMAJROR KAAF MODAFILAYH HAAE
    '''
    p[0] = " ".join(p[1:])

# Error handling for syntax errors
def p_error(p):
    print(f"Syntax error at position {p.lexpos}: Unexpected character '{p.value}'")

# Create the parser
parser = yacc.yacc()

# Test the parser with the proverbs

proverb_input2 = "الصبر مفتاح الفرج"
result2 = parser.parse(proverb_input2, lexer=None)

proverb_input3 = "اذا تم العقل نقص الكلام"
result3 = parser.parse(proverb_input3, lexer=None)

proverb_input4 = "الدال على الخير كفاعله"
result4 = parser.parse(proverb_input4, lexer=None)

print("Parsed proverb 2:", result2)
print("Parsed proverb 3:", result3)
print("Parsed proverb 4:", result4)
