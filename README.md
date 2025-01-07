# Mia-RPS


## Contornos da tarefa

| Contornos da tarefas | Observable | Axentes | Determinista | Episodico | Estatico | Discreto | Coñecido |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| RPS | Partially | Single | Non Deterministic | Sequential | static | Discrete | Know |

Observable, o modelo e partial pues non e consciente das decisions do xogador e por tanto non pode observar o estado completo do entorno

Axentes , o modelo e Single xa que no existe otro axente que interactuen con o entorno

Determinista, este e Non Deterministic devido a que a decision do xogador e aleatoria y non se pode predecir a suas decisiones exactamente , aparte de esto no e Stochastic puoi no se lidia con probabilidades.

Episodico, este modelo es Sequential ya que en nuestra estrategia se tiene en cuenta los resultados de anteriores partidas y es necesario tener encuenta estos resultados para seber quien ganara el juego

Estatico, e static porque o modelo no cambia mentras o agente toma a su decision e se espera a que este acabe o seu turno para poder continuar.

Discreto, este e discrete xa que existen finitas posibilidades  nun rps

Coñecido , Simplemente es Know devido a que o axente coñece todas as regras do entorno


## Estructura do Axente

Decidin utilizar un axente baseado en modelos porque o entorno e parcialmente observable e  creo que e o mais facil de utilizar 


![Axente baseado en modelo](/doc/model-based-reflex-agent.png)

As acions de mi modelo son bastantes sinxelas, primero este e invocado por o entorno,este sendo o codigo xeral do xogo, entonces primero utilizaria a lista Past actions, unha lista de diccionarios estatica,  para obter informacion sobre a partida anterior con esta informacion podra pasar por as condition action rules e obter o siguinte movemento.

As condition-action rules se basan nun estudio universitario chino que se fixo sobre o xogo do rps, basicamente para resumilo, este estudio mostra que xogando contra persoas os movementos mais comun son que os xogadores que gañan continuan con a mesma accion e os perdedores cambian de movemento polo tal,  os movementos optimos son si o axente perde, deveria xogar a mesma accion que o xogador rival e se o axente gaña a ronda deveria xogar o movemento que non a salido na ronda anterior.

Despois disto simplemente devolve o movemento mediante un return ao enviroment para que se poda executar a comparacion, observar quen gañou esta ronda e esta se garde na lista de past actions.

## Implementacion python

Esta es a implementacion a python que e codeado para el rps.

![Implementacion del rps](/doc/implementacion_rps.png)

O primeiro que facemos e obtener o tamaño ou lenght da lista past actions esto e necesario  xa que ao principio do xogo non existen memorias de xogos pasados e entonces non importa a decision da maquina, pode ser completamente aleatoria pero al buscar informacion sobre o xogo se falaba moito sobre que papel es a xogada mais popular al principio da partida por lo que decidin que o principio da partida se xoge tixeira.

despois de esto obtemos si na  anterior ronda a maquina a ganado o non, si a maquina a ganado esto significa que deveria escoller unha accion que no se a xogado, e decir si o axente a gañado con pedra contra unas tixoiras aa jugada optima e papel, esto o consigo utilizando  un enumerado onde se gardan todas as accions posibles , estas representadas por un numero  e ciclo as opcions simplemente obtendo a accion da computadora , a accion ganadora e sumandolle 1 ao valor e tendo un if para poder prevenir errores.

![Enum del rps](/doc/enum_rps.png)

NO caso de que o axente perdiera a ronda anterio solo ten que executar o movemento do rival , e decir o movemento que gañou, esto o consigo da lista past action.

## Expansion RPSLS

No caso de expandir o rps a o rpsls no meu caso e bastante facil xa que o meu codigo no recibe muchos, simplemente añado as dos novas accions ao enumerado , esta sendo lagarto e spock e despois modifico o metodo na parte onde o axente gana, cando o axente gana este ten que escoller unha opcion que no sido escogida en la anterior partida pero como agora as regras cambia ao añadir duas xogadas extra embez de sumar 1 ao valor da xogada anterior da maquina agora añadimos 2 e no momento que supere a accion con valor mais alto neste caso catro se reinicia de volta a 0.

![Implementacion RPSLS](/doc/implementacion_rpsls.png)

esto e necesario xa que añadiendo 2 emvez de 1 sempre se xogara unha xogada que non foy selecionada anterior mente pero que tampoco perderia contra a xogada gañadora anterior.
## Bibliografia

Winning at Rock Paper Scissors - Numberphile , video explicatibo basado no estudio universitario chino.
https://www.youtube.com/watch?v=rudzYPHuewc&t=236s

Social cycling and conditional responses in the Rock-Paper-Scissors game∗, papel hablando sobre o xogo do rps.
https://arxiv.org/pdf/1404.5199v1