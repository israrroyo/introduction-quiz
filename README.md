## introduction-quiz

*1 clonar repositorio *     
*2 Abrir una pestaña en la terminal y ejecutar  el comando de netcat para recibir el contenido del json  " nc -l -p [puerto a utilizar]"  ejemplo : nc -l -p 9090   Este comando se debe dejar corriendo en todo momento para recibir el contenido *     
*3 Dirigirse a la carpeta "Quiz" e instalar los requirements en nuestro entorno*
*4 Ejecutar el programa "send_answers.py" con el comando  python [nombre del programa] [json a procesar] [ip donde se enviara el json] [puerto] , ejemplo:  python send_answers.py introduction_quiz.json localhost 9090*  
  


