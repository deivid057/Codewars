def open_or_senior(data):
    position = 0
    l = []
    while position <= len(data) - 1:
        # Pega um conjunto da lista de cada vez!      
        n = data[position]
        position += 1

        # Coleta apenas a idade e a deficiência!
        idade = n[0]
        defi = n[1]
        
        # Verifica se o candidato é Senior ou Open! 
        try :
            if idade < 55 or defi <= 7:
              nivel = ('Open')
            
            elif idade >= 55 or defi > 7:
              nivel = ('Senior')
              

        finally:
          for i in range(1):
            l.append(nivel)
          
    print(l)

