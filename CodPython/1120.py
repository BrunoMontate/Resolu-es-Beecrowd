
#subprogramação
'''
def valorCorrigido(nErrado,contrato):
  nErrado = str(nErrado)
  contrato = str(contrato)
  posicaoErro = str("")
  vezesErrado = str(contrato.count(nErrado))
  for i in vezesErrado:
    posicaoErro = contrato.find(nErrado)
    if posicaoErro == -1:
        print(contrato)
    else:
        contrato = contrato.replace(posicaoErro,' ')
'''

def valorCorrigido(nRuim,contrato):
  nRuim = str(nRuim)
  contrato = str(contrato)
  val = ''
  val = int(contrato.replace(nRuim,''))
  if val == '':
    print('0')
  else:
    print(val)

#programaprincipal
nProblematico,totalContrato = map(int,input().split())
while(nProblematico > 0 and totalContrato > 0) :
   valorCorrigido(nProblematico,totalContrato)
   nProblematico, totalContrato = map(int, input().split())


'''while(True):
    d, n = input().split()
    if(d == '0' and n == '0'):
        break
    n = '0' + n
    val = int(n.replace(d,''))
    print(val)
'''