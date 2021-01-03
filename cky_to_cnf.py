import nltk




s = grammar_original.productions()
start_symbol = grammar_original.start()
cnf_form = []
def is_unit(production):
    
    if len(production)==1 and production.is_nonlexical():
        return True
    else:
        return False
    
def is_null(production):
    return True

def has_start_symbol(production):
    
    if  start_symbol in production.rhs():
        return True
    else:
        return False
    
def useless_production():
    """
    return all useless non terminals that never ends in a string and that could never be derived from start symbol
    """
    useless_non_terminals = []
    non_terminals = [xx for x in grammar2.productions() for xx in x.rhs() if type(xx) == nltk.Nonterminal]
    for non_terminal in non_terminals:
        filtered = grammar2.productions(lhs= non_terminal)
        useless = False
        filtered
            
    return useless_non_terminals

                    
def replacing_start_symbol(productions):
    
    for production in productions:
        if has_start_symbol(production):
            
            return True
        else:
            return False
           

def removing_unit_production(grammar):
    
    productions = grammar.productions()
    new_productions = []
    replacing_prod=[]
    for production in productions:
        if not is_unit(production):
            new_productions.append(production)
        else:
            replacing_prod.append(production)
            
    i = 0           
    while replacing_prod:
        a = replacing_prod.pop()
        for each in grammar.productions(lhs = a.rhs()[0]):
            temp_rule = nltk.grammar.Production(a.lhs(), each.rhs())
            if len(temp_rule) != 1 or temp_rule.is_lexical():
                new_productions.append(temp_rule)
                
            else:
                replacing_prod.append(temp_rule)
                
        
    return nltk.grammar.CFG(grammar.start(),new_productions)
                   

def replacing_terminals(new_grammar):
    """
    """
    productions = new_grammar.productions()
    new_productions = []
    for production in productions:
        rhs = []
        if len(production.rhs())>1:
            for each_rhs in production.rhs():
                if nltk.grammar.is_terminal(each_rhs):
                    new_non_terminal = nltk.grammar.Nonterminal(each_rhs)
                    new_productions.append(nltk.grammar.Production(new_non_terminal,each_rhs))
                    rhs.append(new_non_terminal)
                else:
                    rhs.append(each_rhs)
            new_productions.append(nltk.grammar.Production(production.lhs(), tuple(rhs)))
        else:
            new_productions.append(production)
            
                
    return nltk.grammar.CFG(new_grammar.start(),new_productions)

            


def making_binary(new_grammar):
    """
    """
    productions = new_grammar.productions()
    new_productions = []
    for production in productions:
        rhs = production.rhs()
        prod = production
        new_rhs = []
        if len(rhs)>2:
            while True:
                for i in range(0, len(rhs), 2):
                    new_prod = tuple(rhs[i:i+2])
                    if len(new_prod) == 2:
                        binarized_lhs = nltk.grammar.Nonterminal("_".join([str(x).lower() for x in new_prod]))
                        new_rhs.append(binarized_lhs)
                        new_productions.append(nltk.grammar.Production(binarized_lhs,new_prod))
                    else:
                        new_rhs.append(new_prod[0])
                prod =  nltk.grammar.Production(production.lhs(),new_rhs)
                if len(prod.rhs()) <= 2:
                    new_productions.append(prod)
                    break;
                else:
                    rhs = new_rhs.copy()
                    new_rhs = []
                                       
        else:
            new_productions.append(production)
    return nltk.grammar.CFG(new_grammar.start(),new_productions)
    
    
def to_cnf():
    """
    """

    has_start_symbol = replacing_start_symbol(s)

    if has_start_symbol:
        s.append(nltk.grammar.Nonterminal("S0_SIGMA"),[start_symbol])
        start_symbol = nltk.grammar.Nonterminal("S0_SIGMA")

    new_grammar = nltk.grammar.CFG(start=start_symbol, productions=s)
    new_grammar = making_binary(new_grammar)
    new_grammar = replacing_terminals(new_grammar)
    new_grammar = removing_unit_production(new_grammar)


if __name__()==__main__:

    to_cnf()
