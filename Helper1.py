
#Helper1.py

#              Invoke ONLY these THREE routines
#molesAndCompound (myCell) returns a list with two items: # moles and the compound
#	Example: molesAndCompound (‘Fe(OH)3’) returns [1, Fe(OH)3]
#atomCount (compound) returns a dictionary – key is atom, and value is # atoms. 
#	Example: atomCount (‘Fe(OH)3’) returns {'H': 3, 'Fe': 1, 'O': 3} 
#symbolAndMass (peirodicTableFileName) returns a dictionary – key is atom, and value is mass, for all elements in the file. 
#	Example: symbolAndMass (‘PeriodicTableData.xlsx’) returns {'H': '1.008', 'He': '4.003' …}


import xlrd

def symbolAndMass (fileName):
    
    workbook = xlrd.open_workbook(fileName)
    sheet = workbook.sheet_by_index(0)
    symbolName = sheet.col_values(1, 1)
    mass = sheet.col_values(6, 1)

    symbolMassDict = {s : m for s, m in zip(symbolName, mass)}
    return (symbolMassDict)

def unParen(compound):
    import re 
    myRegEx = re.compile(r"(\()(\w*)(\))(\d*)",re.I)
    while (1): 
      myMatches = myRegEx.findall(compound)
      if (len(myMatches) == 0):
         return(compound)
      for match in myMatches:   
        text =""
        count = 1 if  match[3] == "" else int(match[3])
        text = match[1] * count
        compound = compound.replace('(' + match[1] + ')' + match[3], text)
        print ("now", compound) 
     
def atomCount(compound):

  #return: dictionary - key is atom, value is # atoms

  #Modified from Lpez web resource ... stackoverflow.com/questions/16699180 ...
  import re

  atomDict = {}

  #unParentisize the given compound
  compoundNoParen = unParen(compound)

  myRegEx = re.compile("(C[laroudsemf]?|Os?|N[eaibdpos]?|S[icernbmg]?|P[drmtboau]?|H[eofgas]?|A[lrsgutcm]|B[eraik]?|Dy|E[urs]|F[erm]?|G[aed]|I[nr]?|Kr?|L[iaur]|M[gnodt]|R[buhenaf]|T[icebmalh]|U|V|W|Xe|Yb?|Z[nr])(\d*)")

  #create dictionary with key as atom, and value as # how many of this atom
  myMatches = myRegEx.findall(compoundNoParen)
  for match in myMatches:
    #Search atom
    atom = match[0]
    value = 1 if match[1]=="" else int(match[1])
    print(atom,value)
    atomDict.setdefault(atom,0)
    atomDict [atom] += value

  #print (atomDict)
  return (atomDict)

def molesAndCompound (thisTerm):
    c = thisTerm[0]
    print (c)
    if c.isdigit():
        noMoles = int (c)
        myCompound = thisTerm[1:]
    else:
        noMoles = 1
        myCompound = thisTerm
    return [noMoles,  myCompound ]

