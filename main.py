#resolver questoes de mov balistico com codigo 

from math import*

g = 9.8
#gravidade -> sinal negativo (contrária ao referencial y positivo (o mesmo do plano cartesiano))

def unidade_medida():
  print()
  conversao =input("Você deseja fazer a conversão de medidas? (s ou n): ")
  if conversao == "s":
    valor = float(input("Valor da velocidade: "))
    medida = input("Digite a unidade de medida da velocidade: ")
    if medida == "km/h":
      valor = valor/3.6
      print("velocidade em m/s: ",valor)
    if medida == "m/s":
      valor = valor*3.6
      print("velocidade em km/h: ", valor)
    if medida == "cm/s":
      valor = valor*0.01
      print("velocidade em m/s: ", valor)
  else:
    return
    
print()

print("1.v0x: velocidade inicial na direção i \n2.v0y: velocidade inicial na direção j \n3.hmáx(altura) \n4.tar : tempo em que o objeto permanece no ar (alcance) \n5.xmáx \n6.vx na posição ℎ𝑚á𝑥 \n7.vy na posição ℎ𝑚á𝑥 \n8.|v| na posição ℎ𝑚á𝑥 \n9.vx quando o objeto atinge o solo \n10.vy quando o objeto atinge o solo \n11.|v| quando o objeto atinge o solo \n12.X(t) \n13.Y(t) \n14.Vx(t) \n15.Vy(t) \n16.|v(t)|\n17.Descobrir alcance máximo, sabendo  (hmáx ou tempo de queda) e v0x: \n18.(lancamento horizontal)Calcular a altura que o objeto chega sabendo altura inicial e tempo de queda. \n19.Descobri xmáx tenho 2 objetos: 1 que cai, outro que salta horizontalmente, temos tempo de queda do primeiro e v0x do segundo. \nPara sair digite 0") 

unidade_medida()

while True: 
  
  opcao = int(input("Digite o número do calculo que deseja fazer: "))
  
  if opcao == 1: 
    V0 = float(input("Digite a velocidade inicial de lançamento(V0): "))
    angulo = float(input("Digite o ângulo de lançamento: "))
    rad = radians(angulo)
    v0x = V0*cos(rad)
    print("V0X é: ", v0x)

  elif opcao == 2:
    V0 = float(input("Digite a velocidade inicial de lançamento(V0): "))
    angulo = float(input("Digite o ângulo de lançamento: "))
    rad = radians(angulo)
    v0y = V0*sin(rad)
    print("V0Y é: ", v0y)

  elif opcao == 3:
    Yinic = float(input("Digite a altura (em metros) em que o objeto saiu: "))
    V0 = float(input("Digite a velocidade inicial de lançamento(V0): "))
    angulo = float(input("Digite o ângulo de lançamento: "))#ângulo com o eixo x positivo
    rad = radians(angulo)
    V0y = V0*sin(rad)
    hmax = (V0y**2 + 2*g*Yinic)/(2*g) 
    #v*2=v02+2*a(sfinal -sinicial)->
    #vy*2=v0y2-2*g(hmax - Yinicial) 
    print("Hmáx é: ", hmax)

  elif opcao == 4:
    hmax = float(input("Digite a altura máxima (em metros): "))
    V0 = float(input("Digite a velocidade inicial de lançamento: "))
    angulo = float(input("Digite o ângulo de lançamento: "))
    rad = radians(angulo)
    V0y = V0*sin(rad)
    tsub = V0y/g  #v=v0+at -> v=v0y-gt
    tqued = sqrt((2*hmax)/g) #calculo hmax ja inclui diferenca de altura final e inicial
    #S=S0+V0*t+a*t*2/2 -> Y=Yinic+v0y*t-g*t*2/2 
    #(-V0y +- sqrt(V0y*2 -4(-g)(hmax))/(2-g))
    tar = tsub + tqued
    print("Tempo (em segundos) que o objeto permanece no ar é: ", tar)
  
  elif opcao == 5:
    tar = float(input("Digite o tempo (em segundos) em que o objeto permanece no ar: "))
    V0 = float(input("Digite a velocidade inicial de lançamento: "))
    angulo = float(input("Digite o ângulo de lançamento: "))#ângulo com o eixo x positivo
    rad = radians(angulo)
    V0x = V0*cos(rad)
    xmax = V0x*tar #MRU. #s=so+vx*t 
    print("Alcance horizontal máximo é: ",xmax)

  elif opcao == 6:
  #vx é sempre igual (MRU)
    V0 = float(input("Digite a velocidade inicial de lançamento: "))
    angulo = float(input("Digite o ângulo de lançamento: "))
    rad = radians(angulo)
    V0x = V0*cos(rad)
    Vx = V0x
    print("Vx na posição Hmáx é: ", Vx)

  elif opcao == 7:
    print("Vy na posiçao Hmáx é 0")

  elif opcao == 8:
    Vx = float(input("Digite o valor de Vx quando o objeto atinge a altura máxima: "))
    V = sqrt(Vx**2+ 0 )  #Vy=0
    print("Módulo de V na posicao Hmáx é: ", V)

  elif opcao == 9:
    V0 = float(input("Digite a velocidade inicial de lançamento: "))
    angulo = float(input("Digite o ângulo de lançamento: "))
    rad = radians(angulo)
    Vx = V0*cos(rad) #Vx é sempre igual
    print("Vx quando o objeto atinge o solo é: ", Vx) 

  elif opcao == 10: 
    hmax = float(input("Digite a altura maxima (em metros): "))
    tqued = sqrt((2*hmax)/g)
    Vy = -(g*tqued) 
    #vy é negativa->contraria ao referencial
    #v=v0+a*t -> Vy=-(V0y-g*t)(v0y=0 (hmax))
    print ("Vy quando o objeto atinge o solo é: ", Vy)

  elif opcao == 11:
    Vx = float(input("Digite a velocidade em x quando o objeto atinge o solo: "))
    Vy = float(input("Digite a velocidade em y quando o objeto atinge o solo: "))
    V = sqrt(Vx**2 + Vy**2)
    print("O modulo da velocidade quando o objeto atinge o solo é:", V)

  elif opcao == 12:
    X0 = float(input("Digite o valor inicial em x (X0): "))
    tempo = float(input("Digite um tempo (em segundos) após o lançamento: "))
    V0 = float(input("Digite a velocidade inicial de lançamento: "))
    angulo = float(input("Digite o ângulo de lançamento: "))
    rad = radians(angulo)
    V0x = V0*cos(rad)
    Xt = X0 + V0x*tempo   #S=S0+v0*t
    print("A posicao em x após um tempo (X(t)) é: ", Xt)

  elif opcao == 13:
    tempo = float(input("Digite um tempo (em segundos) após o lançamento: "))
    V0 = float(input("Digite a velocidade inicial de lançamento(V0): "))
    angulo = float(input("Digite o ângulo de lançamento: "))
    Y0 = float(input("Digite a altura (em metros) em que o objeto saiu: "))
    rad = radians(angulo)
    v0y = V0*sin(rad)
    ts = v0y/g
    Yt = Y0 + v0y*tempo -g*(tempo**2)/2
    #S=S0+V0*t-g*t**2/2
    print("A posicao em y apos um tempo (Y(t)) é: ",Yt)

  elif opcao == 14:
    tempo = float(input("Digite um tempo (em segundos) após o lançamento: "))
    V0 = float(input("Digite a velocidade inicial de lançamento(V0): "))
    angulo = float(input("Digite o ângulo de lançamento: "))
    rad = radians(angulo)
    V0x = V0*cos(rad)
    Vxt = V0x
    print("Vx(t),Vx em um tempo qualquer é: ", Vxt)

  elif opcao == 15: 
    tempo = float(input("Digite um tempo (em segundos) após o lançamento: "))
    V0 = float(input("Digite a velocidade inicial de lançamento(V0): "))
    angulo = float(input("Digite o ângulo de lançamento: "))
    rad = radians(angulo)
    v0y = V0*sin(rad)
    Vy = v0y -g*tempo #só g é contraria ao referencial
    print("A velocidade em y em um tempo qualquer é: ", Vy) #v=v0+a*t -> vy=v0y-g*t

  elif opcao == 16:
    Vxt = float(input("Digite a velocidade em x após um certo tempo: "))
    Vyt = float(input("Digite a velocidade em y após um certo tempo: "))
    V = sqrt(Vxt**2 + Vyt**2)
    print("O módulo da velocidade após um certo tempo é: ", V)

  elif opcao == 17:
    pergunta = int(input("Sabe 1. tempo de queda ou 2.hmáx? (digite o número):"))
    if pergunta == 1:
      v0x = float(input("Digite a velocidade inicial em x(v0x): "))
      tqued = float(input("Digite o tempo de queda: "))        
      xmax = v0x*tqued
      print("O alcance máximo será de ",xmax)
    if pergunta == 2:
      hmax = float(input("Digite a altura máxima que o objeto é lançado: "))
      v0x = float(input("Digite a velocidade inicial em x(v0x): "))
      tqued = sqrt((2*hmax)/g)
      xmax = v0x*tqued
      print("O alcance máximo será de ",xmax)
  elif opcao == 18:
    tt=float(input("Tempo total: "))
    h = float(input("Digite a altura inicial: "))
    v0y = -g*tt
    y= h + v0y*tt+(g*tt**2)/2 
    print("y em cm será: ",y)
    
  elif opcao == 19:
    v0x= float(input("Digite a velocidade inicial em x(v0x): "))
    tt=float(input("Tempo total: "))
    vy=g*tt
    y=(vy**2)/2*g
    t2 = sqrt(2*y/g)
    xmax= v0x*tt
    print("O alcance maximo será: ",xmax)
    
  elif opcao == 0:
    break
