import re

class AnalisadorLexico:
    regex = re.compile('".*"|[0-9]+|[a-zA-Z_]+[a-zA-Z0-9_]*|[+|*|/|\-|{|}|(|)|\[|\]|\.|,|;|<|>|=|~|&]')
    keyword = [
        'var','null','this','let','do','return', 'constructor'
    ]
    keywordClass = ['class'] 
    keywordConstructor = ['constructor'] 
    keywordFunction = ['function'] 
    keywordMethod = ['method'] 
    keywordVarStaticType = ['field','static']
    keywordVarType = ['int','char','boolean']
    keywordFunctionType = ['void']
    keywordBooleanType = ['true','false']
    keywordConditional = ['if','else']
    keywordLoop = ['while']


    symbol = '[+|*|/|{|}|(|)|.|,|;|<|>|=|~]'
    identifier = '[a-zA-Z_]+[a-zA-Z0-9_]*'
    integer = '[0-9]+'
    string = '".*"'

    def __init__(self):
        self.arquivo = open('main.jack', 'r').read()
        self.arquivo = re.sub('//.*'," ", self.arquivo) #remover os comentário com //
        self.arquivo = re.sub('(/\*(.|\n)*?\*/)'," ", self.arquivo) #remover os comentário com /* */
        self.tokens = self.regex.findall(self.arquivo)
        self.lentokens = len(self.tokens)
        self.indice = 0
        self.saida = open('saida.xml', 'w+')
        self.identador = 0

    def trocarXML(self, simbolo): #trocar para o XML
        if (simbolo == '>'):
            return '&gt;'
        if (simbolo == '<'):
            return '&lt;'
        if (simbolo == '&'):
            return '&amp;'
        if (simbolo == '"'):
            return '&quot;'
        else:
            return simbolo

    def avancar(self):
        if(self.hatoken()):
            self.indice += 1

    def hatoken(self):
        return self.indice < self.lentokens

    def buscartoken(self):
        if (self.indice < self.lentokens):
            return self.tokens[self.indice]
        return

    def tipo(self): #tipo do indix no xml
        token = self.buscartoken()
        if(token != None):
            if(re.match(self.identifier, token)):
                if(token in self.keyword):
                    return 'keyword'              
                elif(token in self.keywordClass):
                    return 'keywordClass'
                elif(token in self.keywordConstructor):
                    return 'keywordConstructor'
                elif(token in self.keywordFunction):
                    return 'keywordFunction'
                elif(token in self.keywordMethod):
                    return 'keywordMethod'
                elif(token in self.keywordVarStaticType):
                    return 'keywordVarStaticType'
                elif(token in self.keywordVarType):
                    return 'keywordVarType'
                elif(token in self.keywordFunctionType):
                    return 'keywordFunctionType'
                elif(token in self.keywordBooleanType):
                    return 'keywordBooleanType'
                elif(token in self.keywordConditional):
                    return 'keywordConditional'
                elif(token in self.keywordLoop):
                    return 'keywordLoop'
                else:
                    return 'identifier'

            elif(re.match(self.symbol, token)):
                return 'symbol'

            elif(re.match(self.integer, token)):
                return 'integer'
            
            elif(re.match(self.string, token)):
                return 'string'

    def escrever(self, flag=0, estado=''):
        if(flag == 1):
            self.saida.writelines((self.identador * "  ") + "<{0}>\n".format(estado))
            self.identador += 1
        elif(flag == 2):
            self.identador -= 1
            self.saida.writelines((self.identador * "  ") + "</{0}>\n".format(estado))
        else:
            if(flag == 0):
                token = self.buscartoken() 
                tipo = self.tipo()
                self.saida.writelines((self.identador * "  ") + "<{0}>{1}</{2}>\n".format(tipo, token,tipo))

        # saida = open('saida.xml', 'w+')
        # saida.writelines('<tokens>\n') 
        # for token in self.tokens:
        #     tipo = self.tipo(token)

        #     saida.writelines(('<{0}> {1} </{2}>\n'.format(tipo, token, tipo)))
        # saida.writelines('</tokens>') 
        # print('finalizado')

# analisador = AnalisadorLexico()
# analisador.escrever()
