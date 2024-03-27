class Rule:
    def __init__(self, pattern, replacement):
        self.pattern = pattern
        self.replacement = replacement

def apply_rules(input_str, rules, max_iterations=1000, sep = " -> "):
    output = input_str
    print_str = input_str
    count = 0
    rule_applied = True
    while rule_applied and count < max_iterations:
        rule_applied = False
        for rule in rules:
            if not rule_applied:
                match_len = len(rule.pattern)
                pos = output.find(rule.pattern)
                while pos != -1:
                    output = output[:pos] + rule.replacement + output[pos + match_len:]
                    pos = output.find(rule.pattern, pos + len(rule.replacement))
                    count += 1
                    rule_applied = True
                    print_str += sep + output
    if count == max_iterations:
        return "Recursive"
    print(print_str + "\n")
    return output

def remove_duplicated_a(input_string):
    found_first_a = False
    result = ""
    
    for char in input_string:
        if char == 'a' and found_first_a:
            continue
        elif char == 'a':
            found_first_a = True
        result += char
    
    print(result)

print("\nTask 1:\n")
rules = [Rule("yx", "xy"), Rule("xy", "")]
apply_rules("yxyxyxxxy",rules)
apply_rules("yxyxxyxyx",rules)
apply_rules("yx",rules, sep="\n |\n")

print("\nTask 2:\n")
rules = [Rule("yyx", "y"), Rule("xx", "y"), Rule("yyy", "x")]
apply_rules("yyyyxyxyxy",rules)
apply_rules("yyyyxyyyxxxxyxy",rules)

print("\nTask 3:\n")
rules = [Rule("1-1", "-0"), Rule("01", "1"), Rule("-0", "")]
A = "1111111"
B = "1111"
apply_rules(A + "-" + B, rules)
apply_rules("111" + "-" + "11111", rules)
apply_rules("111111" + "-" + "11", rules)

print("\nTask 4:\n")
rules = [Rule("1+1", "11+0"), Rule("01", "1"), Rule("+0", "")]
A = "1111111"
B = "1111"
apply_rules(A + "+" + B, rules)
apply_rules("111" + "+" + "1", rules)
apply_rules("1" + "+" + "1111", rules)

print("\nTask 5:\n")
rules = [Rule("*11", "T*1"), 
         Rule("*1", "T"), 
         Rule("1T", "T1F"), 
         Rule("FT", "TF"), 
         Rule("F1", "1F"), 
         Rule("T1", "T"), 
         Rule("TF", "F"), 
         Rule("F", "1")]
apply_rules("11*11", rules)
apply_rules("111*1111", rules)
apply_rules("11*1111", rules)

print("\nTask 6:\n")
remove_duplicated_a("acaabaa")
remove_duplicated_a("bacabac")
remove_duplicated_a("abacabacabac")
rules = [Rule("aa", "a"), Rule("ba", "ab"), Rule("ca", "ac")]
#rules = [Rule("0a", "0"), Rule("0b", "b)"), Rule("0c", "c0"), Rule("a", "01"), Rule("0", "")]
apply_rules("acaabaa", rules)
apply_rules("bacabac", rules)
apply_rules("abacabacabac", rules)

print("\nTask 7:\n")
rules = [Rule("  ", " ")]
apply_rules("  a  b  c  ", rules, sep="|")
apply_rules("  a  b  c    ", rules, sep="|")
apply_rules("  a b c ", rules, sep="|")