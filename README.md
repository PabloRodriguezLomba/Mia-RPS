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

Decidin utilizar un axende baseado en modelos porque o entorno e parcialmente observable e  creo que e o mais facil de utilizar 


![Axente baseado en modelo](/doc/model-based-reflex-agent.png)

Las aciones de mi modelo son bastantes sinxelas, primero este es invocado por o enviroment,este sendo o codigo xeral do xogo, entonces primero utilizaria a lista Past actions, unha lista de diccionarios estatica,  para obtener informacion sobre a partida anterior con esta informacion podra pasar por las condition action rules y obtener el siguiente movimiento.

Las condition-action rules son bastante sencillas se basan en un estudio universitario chino que se hizo sobre o xogo do rps, basicaemente para resumilo neste estudio mostran que xogando contra persoas os movementos mais comun son que os xogadores que gañan continuan con a mesma accion e os perdedores cambian de movemento polo tal,  os movementos optimos son si o axente perde, deveria xogar a mesma accion que o xogador rival e se o axente gaña a ronda deveria xogar o movemento que non a salido na ronda anterior.

despois disto simplemente devolve o movemento mediante un return ao enviroment para que se poda executar a comparacion, observar quen gañou esta ronda e esta se garde na lista de past actions.
