all:	/Users/sarnobat/.pyenv/versions/3.10.13/lib/python3.10/site-packages/lark
	
	tput setaf 211
	cat research.mwk | /Users/sarnobat/.pyenv/shims//python3 mwk_parser.py | tee /tmp/out.json
	cat /tmp/out.json | jq
	tput setaf 149
	cat ~/sarnobat.git/2023/genealogy/rohidekar.ged  | /Users/sarnobat/.pyenv/shims//python3 gedcom.py
	
/Users/sarnobat/.pyenv/versions/3.10.13/lib/python3.10/site-packages/lark:
	python3 -m pip install lark