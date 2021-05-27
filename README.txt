lexical_analyzer.py
input은 input.c이고, output은 output.txt입니다.
syntax_analyzer.py
input은 lexical analyzer의 output인 output.txt입니다

lexical_analyzer의 경우

terminal에서 

python lexical_analyzer.py input.c


syntax_analyzer의 경우

terminal에서 

python syntax_analyzer.py output.txt

로 실행해주시면 됩니다.






NFA_FOLLOW_DFA_SLRTABLE 폴더에 들어있는 것들은 모두 TERM_PROJECT_DOCUMENT 문서에 포함되어있습니다.


TERM_PROJECT_DOCUMENT는 코드 설명, 코드 시연이 들어있는 문서입니다.
