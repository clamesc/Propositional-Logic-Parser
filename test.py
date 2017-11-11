#!/usr/bin/python
#!python

from main import *

print ""
print ""
print "    ==================================================================="
print "    ||     Practical 3 Program by Claus Meschede [IMAT: 03667973]    ||"
print "    ==================================================================="
print ""
print ""
print "Problem 4.1"
print ""
print "Use the function 'entails' to check whether the following entailment is true or not."
print "1. False |= True"
print "2. True |= False"
print "3. (A /\ B) |= (A <=> B)"
print "4. (A <=> B) |= A \/ B"
print "5. (A <=> B) |= ~A \/ B"
print ""
print "Solution:"
print "1. " + str(entails(parse(lex("False")),parse(lex("True"))))
print "2. " + str(entails(parse(lex("True")),parse(lex("False"))))
print "3. " + str(entails(parse(lex("(A /\ B)")),parse(lex("(A <=> B)"))))
print "4. " + str(entails(parse(lex("(A <=> B)")),parse(lex("A \/ B"))))
print "5. " + str(entails(parse(lex("(A <=> B)")),parse(lex("~A \/ B"))))
print ""
print ""
print "Problem 4.2.2"
print ""
print "Use the function tautology, satisfiable, unsatisfiable to check whether the following formulae is tautology, satisfiable, or unsatisfiable. Compare the output with the result from your pencil-and-paperderivation."
print "1. Smoke ==> Smoke"
print "2. (Smoke ==> Fire) ==> (~ Smoke ==> ~ Fire)"
print "3. Smoke \/ Fire \/ ~Fire"
print "4. (Fire ==> Smoke) /\ Fire /\ ~ Smoke"
print ""
print "Solution:"
print "1. " + str(check(parse(lex("Smoke ==> Smoke"))))
print "2. " + str(check(parse(lex("(Smoke ==> Fire) ==> (~ Smoke ==> ~ Fire)"))))
print "3. " + str(check(parse(lex("Smoke \/ Fire \/ ~Fire"))))
print "4. " + str(check(parse(lex("(Fire ==> Smoke) /\ Fire /\ ~ Smoke"))))
print ""
print ""
print "Problem 4.2.3"
print ""
print "Represent what B says with your parser."
print "bsays = parse 'b <=> (a <=> ~a)'"
print "where parse is your parser implementation. Do the same with what C says."
print "csays = parse 'c <=> ~b'"
print "Construct a knowledge base - kb of type Formula - by performing conjunction of what B and C says. By using the function entails, check whether the knowledge base entails whether A is a knight. Check also whether it entails whether A is a knave. Perform these checks for B and C as well."
print ""
print "Solution:"

bsays = parse(lex("b <=> (a <=> ~a)"))
csays = parse(lex("c <=> ~b"))
kb = [bsays, "and", csays]
print "KB entails 'A is a knight': " + str(entails(kb, parse(lex("a"))))
print "KB entails 'A is a knave': " + str(entails(kb, parse(lex("~a"))))
print "KB entails 'B is a knight': " + str(entails(kb, parse(lex("b"))))
print "KB entails 'B is a knave': " + str(entails(kb, parse(lex("~b"))))
print "KB entails 'C is a knight': " + str(entails(kb, parse(lex("c"))))
print "KB entails 'C is a knave': " + str(entails(kb, parse(lex("~c"))))
print ""
print ""
print ""
print ""