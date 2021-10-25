https://pluc-cotacao.herokuapp.com/

|  ROTA | TIPO| 
|---|---|
|/cotacao/de=<moeda>&para=<moeda>   | GET  |
  
EX:
  https://pluc-cotacao.herokuapp.com/cotacao/de=USD&para=BRL
  
  Resposta
  ```json
  {
    "Valor":5.48
  }
  
  ```
