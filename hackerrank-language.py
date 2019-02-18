st="C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART: GROOVY:OBJECTIVEC"
st=st.split(":")
st=" ".join(st)
for _ in range(input()):
    t=raw_input().split()
    fnd=str(t[1])
    if st.find(fnd)>=0:
        print "VALID"
    else:
        print "INVALID"