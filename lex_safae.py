from ply import lex

# Define the token names
tokens = ('MOBTADAE1', 'MOBTADAE2', 'khabar12', 'DARFZAMAN', 'FI3L1', 'FA3IL1', 'FI3L2', 'FA3IL2', 'MOBTADAE3', 'HARFJAR', 'ISMMAJROR', 'KAAF','MODAFILAYH','HAAE')

# Define the regular expressions for each token
t_MOBTADAE1 = r'الصبر'
t_MOBTADAE2 = r'مفتاح'
t_khabar12 = r'الفرج'
t_DARFZAMAN = r'اذا'
t_FI3L1 = r'تم'
t_FA3IL1 = r'العقل'
t_FI3L2 = r'نقص'
t_FA3IL2= r'الكلام'
t_MOBTADAE3= r'الدال'
t_HARFJAR = r'على'
t_ISMMAJROR = r'الخير'
t_KAAF = r'ك'
t_MODAFILAYH = r'فاعل'
t_HAAE = r'ه'

# الصبر /مبتدا مرفوع بالضمة
# مفتاح/مبتدا تانى مرفوع بالضمة
# الفرج /خبر مبتدا ثانى مرفوع بالضمة
# والجملة الاسميةمن المبتداو الخبر فى محل رفع خبر المبتدا الاول

# إذا : ظرف لما يستقبل من الزمان مبني على السكون في محل نصب
# تم : فعل ماض مبني على الفتح
# العقل : فاعل مرفوع و علامة رفعه الضمة الظاهرة
# نقص : فعل ماض مبني على  الفتح
# الكلام : فاعل مرفوع و علامة رفعه الضمة الظاهر


# على الخير : جار ومجرور كما تفضلتم وهو متعلق بــ ( الدال ) الوصف المشتق / والله أعلم
# كفاعله : صحيح الكاف للتشبيه ولكنها إما أن نعتبرها : حرفا أو اسما والكثير منهم من يعتبرونها اسما بمعنى : مثل .
# كفاعله : الكاف : اسم بمعنى مثل مبني على الفتح في محل رفع خبر ، وهو مضاف .
# فاعله : مضاف إليه مجرور وعلامة جره الكسرة الظاهرة على آخره ، وهو مضاف ، والهاء : ضمير متصل مبني على الكسر في محل جر بالإضافة .
# وإما أن نقول : كفاعله : الكاف : حرف جر مبني على الفتح لا محل له من الإعراب .
# فاعله : اسم مجرور وعلامة جره الكسرة الظاهرة على آخره ، وهو مضاف ، والهاء : ضمير متصل مبني على الكسر في محل جر بالإضافة .
# والجار والمجرور متعلق بمحذوف خبر للمبتدإ ( الدال ) .

# Ignore whitespace
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer with the proverbs
proverb1 = "الصبر مفتاح الفرج"
proverb2 = "اذا تم العقل نقص الكلام"
proverb3 = "الدال على الخير كفاعله"

# Tokenize and print the recognized tokens for the first proverb
lexer.input(proverb1)
print("Tokens for proverb1:")
for token in lexer:
    print(f"Token Type: {token.type}, Value: {token.value}")

# Tokenize and print the recognized tokens for the second proverb
lexer.input(proverb2)
print("\nTokens for proverb2:")
for token in lexer:
    print(f"Token Type: {token.type}, Value: {token.value}")

# Tokenize and print the recognized tokens for the third proverb
lexer.input(proverb3)
print("\nTokens for proverb3:")
for token in lexer:
    print(f"Token Type: {token.type}, Value: {token.value}")
