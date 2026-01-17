# STAR WARS MISSIONS PLANNER

1. DOMINIO 🌌🚀:
STAR WARS MISSIONS PLANNER es una aplicación/videojuego de **consola (CLI)** desarrollada por "AF STUDIO" en Python que permite agendar misiones **(eventos)** del universo de Star Wars en un intervalo de tiempo con un **Calendario Semanal**, usando los **recursos** disponibles del inventario (Personajes,Droides,Naves,Equipos...).
Este proyecto, está basado en la trilogía original de las Películas de la SAGA (Episodio IV, V y VI). Este fue el dominio escogido, debido a que el desarrollador es fan de Star Wars y le gustaba la idea de llevar a cabo una de sus aficciones favoritas al mundo de la programación.

⚠️ IMPORTANTE:
Este proyecto utiliza las siguientes librerías 📚:
- pygame (Música y sonidos) [Para instalarla en tu editor de código escribe en la terminal: pip install pygame]
- colorama (Strings en color) [Para instalarla en tu editor de código escribe en la terminal: pip install colorama]
- pyfiglet (Texto de presentación estilo ASCII ART) [Para instalarla en tu editor de código escribe en la terminal: pip install pyfiglet]
- json (Guardar los datos) [Viene por defecto con Python]

Para instalar todas las librerías necesarias de un "tirón" escribe lo siguiente en la terminal:
pip install -r requirements.txt

2. Sobre las MISIONES , RECURSOS y RESTRICCIONES 👀:

**Misiones** ❇️✳️: Cada misión tiene diferentes requisitos (Los puedes ver en "misiones.py"):
- Recursos necesarios (Los requisitos mínimos para agendar cada misión)
- Recursos prohibidos (Los recursos que no están permitidos en la misión, por el CONTEXTO DE STAR WARS)
Deberás encargarte de asignar los recursos que requiere la misión (puedes añadir algunos adicionales) y asegurarte de que no haigan recursos que no están permitidos. 
Cada misión cuenta con una <descripción> que te da una PISTA 💡 de cúales son los recursos requeridos y sobre que trata 🤔

**Recursos** 📦: 
Entidades u objetos que pueden ser asignados a cada misión, los recursos se asignan con un "input" en forma de lista de índices. Ej: [1,2,3,4]
Cada índice indica un recurso que se muestran en un inventario. Los recursos poseen cantidades, para añadir una cantidad de un recurso solo debes solicitarlo (repetirlo) una cantidad de veces que no sea superior a la disponible. Ej: [0,11,3,9,9,13,13].
- Cada recurso posee una serie de propiedades: ID, Nombre, Tipo, Bando, Cantidad, Sonido o Frase. (Visibles al agendar una misión en "añadir_mision.py")
- Puedes ver detalles sobre los recursos en la función **Ver Detalles** del menú principal (Su descripción y agenda de disponibilidad)

**Restricciones** ❌:
Entre los recursos existen una serie de restricciones que reflejan la lógica y referencias de Star Wars en este proyecto:
- Co-requisito: Un recurso necesita a otro
Ej: El droide C-3PO necesita ir a una misión junto a su compañero R2-D2 (Porque siempre están juntos)
Ej: Luke Skywalker (Protagonista) necesita su Sable de Luz para combatir (Un Jedi siempre lleva su arma)
- Exclusión: Un recurso no puede estar junto a otro en una misión.
EJ: Han Solo y Lando Calrissian (Son rivales)
Ej: Detonadores Térmicos y Escudo Deflector (Riesgo de explosión propia)


3. INSTRUCCIONES 📋:
Para "entrar en acción" debes abrir el archivo "main_controller.py", que gestiona todos los módulos del programa. Al ingresar puedes elegir si pertenecer al bando de la **Alianza Rebelde** o al **Imperio Galáctico** (Próximamente disponible).
Seguido se te mostrará un Menú con todas las opciones disponibles:

1- **Listar Misiones** # Muestra todas las misiones que tienes agendadas
2- **Añadir Misión** # Permite agendar una misión propuesta, asignar recursos respetando las reglas definidas, y verficar que los recursos no estén en dos misiones al mismo tiempo.
3- **Eliminar Misión** # Se encarga eliminar una misión de la agenda y libera los recursos que están ocupados en ella
4- **Ver Detalles** # Con esta, puedes ver detalles sobre las misiones (¿Qué recursos usa?,¿Cúando?) y sobre los recursos (¿Cúal es su agenda?)
5- **Salir** # Esta función posibilita salir de la aplicación y guardar los cambios realizados en archivos (.json)

4. EXTRA ✨
- Descargar todas las péliculas y series gratis (Requiere VPN en Cuba):
https://lucasltd66.wixsite.com/laswmovies 🔗

- Datos de interés sobre Star Wars (Wookieepedia | Fandom) 
https://starwars.fandom.com 🔗

¡DISFRUTA!
Si te ha gustado este proyecto, agradecería que me dejaras una ⭐ al proyecto en Github 😺.

QUE LA FUERZA TE ACOMPAÑE... ✒️
                Obi-Wan Kenobi.