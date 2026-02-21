# STAR WARS MISSIONS PLANNER 🚀

![cover art](/cover%20art.png)

## Descripción del Proyecto 📖

Star Wars Missions Planner es un aplicación/videojuego de **consola (CLI)** desarrollada por "AF STUDIO" en Python. Permite la planificación de eventos (**misiones**) en un intervalo de tiempo con un **Calendario Semanal** y gestiona **recursos limitados** de la Alianza Rebelde y el Imperio Galáctico. El sistema evita conflictos en la asignación de recursos y respeta restricciones personalizadas del universo de Star Wars.

Este proyecto fue desarrollado como parte del curso de Programación de MATCOM, implementando un motor de planificación inteligente con validación de reglas complejas.

## Características Principales 🎯

- Planificación de 15 misiones icónicas de la trilogía original (Episodios IV, V, VI)
- 33 recursos únicos con propiedades específicas (personajes, naves, droides, equipo)
- Sistema de restricciones avanzado (co-requisitos y exclusiones) + (recursos necesarios y prohibidos)
- Gestión de inventario con cantidades (pools de recursos)
- Búsqueda automática de horarios ("Buscar Hueco")
- Persistencia de datos en formato JSON
- Interfaz de consola inmersiva con música y efectos de sonido
- Música y sonidos temáticos de Star Wars

## DOMINIO ESCOGIDO: STAR WARS 🌌

1. Rica en restricciones naturales: Los recursos tienen relaciones complejas (Han Solo y Lando son rivales, R2-D2 y C-3PO siempre van juntos, etc.)
2. Recursos limitados y únicos: El Halcón Milenario, los sabables de luz, pilotos especializados
3. Misiones icónicas bien definidas: Rescate de la Princesa Leia, Batalla de Hoth, Destrucción de la Estrella de la Muerte
4. Alto potencial de inmersión: Permite usar música, sonidos y elementos visuales del universo

Basado en la trilogía original de las Películas de la SAGA (Episodio IV, V y VI).

## Sobre las MISIONES , RECURSOS y RESTRICCIONES 👀

1. **Misiones** ❇️: Cada misión tiene diferentes requisitos (Los puedes ver en "misiones.py"):
- Recursos necesarios (Los requisitos mínimos para agendar cada misión)
- Recursos prohibidos (Los recursos que no están permitidos en la misión, por el CONTEXTO DE STAR WARS)
Deberás encargarte de asignar los recursos que requiere la misión (puedes añadir algunos adicionales) y asegurarte de que no hayan recursos que no están permitidos. 
Cada misión cuenta con una <descripción> que te da una PISTA 💡 de cúales son los recursos requeridos y sobre que trata 🤔

2. **Recursos** 📦: 
Entidades u objetos que pueden ser asignados a cada misión, los recursos se asignan con un "input" en forma de lista de índices. Ej: [1,2,3,4]
Cada índice indica un recurso que se muestran en un inventario. Los recursos poseen cantidades, para añadir una cantidad de un recurso solo debes solicitarlo (repetirlo) una cantidad de veces que no sea superior a la disponible. Ej: [0,11,3,9,9,13,13].
- Cada recurso posee una serie de propiedades: ID, Nombre, Tipo, Bando, Cantidad, Sonido o Frase. (Visibles al agendar una misión en "añadir_mision.py")
- Puedes ver detalles sobre los recursos en la función **Ver Detalles** del menú principal (Su descripción y agenda de disponibilidad)

3. **Restricciones** ❌:
Entre los recursos existen una serie de restricciones que reflejan la lógica y referencias de Star Wars en este proyecto:
- Co-requisito: Un recurso necesita a otro.
Ej: El droide C-3PO necesita ir a una misión junto a su compañero R2-D2 (Porque siempre están juntos)
Ej: Luke Skywalker (Protagonista) necesita su Sable de Luz para combatir (Un Jedi siempre lleva su arma)
- Exclusión: Un recurso no puede estar junto a otro en una misión.
EJ: Han Solo y Lando Calrissian (Son rivales)
Ej: Detonadores Térmicos y Escudo Deflector (Riesgo de explosión propia)

## Instalación y Uso 🛠️

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. Clonar el repositorio:
git clone https://github.com/AngelForever23/STAR-WARS-MISSIONS-PLANNER.git
cd STAR-WARS-MISSIONS-PLANNER
2. Instalar dependencias:
Opción 1 (Manual):
    pip install -r requirements.txt
Opción 2 (Automática):
    intall_libraries.py
### Ejecutar el Programa
python main_controller.py

### Funciones del Menú Principal
1- **Listar Misiones** # Muestra todas las misiones que tienes agendadas.
2- **Añadir Misión** # Agendar una misión propuesta, asignar recursos respetando las reglas, y verficar que los recursos no estén en dos misiones al mismo tiempo.
3- **Eliminar Misión** # Eliminar una misión de la agenda y libera los recursos que están ocupados en ella.
4- **Ver Detalles** # Ver detalles sobre las misiones (¿Qué recursos usa?, ¿Cúando?) y sobre los recursos (¿Cúal es su agenda?)
5- **Salir** # Salir de la aplicación y guardar los cambios realizados en archivos (.json)

## Estructura del Proyecto 📚

STAR-WARS-MISSIONS-PLANNER/
│
├── Audio/                      # Música y efectos de sonido
│   ├── Background Music/
│   ├── Resource Sounds/
│   └── Sounds/
│
├── Saved Data/                 # Archivos JSON de guardado (generados automáticamente)
│   ├── agendas_recursos_alianza.json
│   ├── misiones_agendadas_alianza.json
│   ├── misiones_restantes_alianza.json
│   ├── papelera_alianza.json
│   ├── agendas_recursos_imperio.json
│   ├── misiones_agendadas_imperio.json
│   ├── misiones_restantes_imperio.json
│   └── papelera_imperio.json
│
├── cover art.png               # Imagen de portada del protecto
├── main_controller.py          # Punto de entrada principal
├── recursos.py                 # Definición de recursos (Clase Recurso)
├── misiones.py                 # Definición de misiones (Clase Evento)
├── restricciones.py            # Lógica de validación de restricciones
├── añadir_mision.py            # Módulo para agendar misiones
├── eliminar_mision.py          # Módulo para eliminar misiones
├── listar_misiones.py          # Módulo para mostrar misiones agendadas
├── detalles.py                 # Módulo para ver detalles de recursos/misiones
├── bando.py                    # Módulo encargado del bando que está activo
├── persistencia.py             # Sistema de guardado/carga en JSON
├── musica_sonidos.py           # Gestión de audio
├── utilidades.py               # Funciones auxiliares
├── requirements.txt            # Dependencias del proyecto
├── install_libraries.py        # Módulo para instalar las librerías necesarias automáticamente
└── README.md                   # Este archivo

## 🎵 Características Multimedia

- Música de fondo temática según el bando
- Efectos de sonido para cada interacción
- Frases y sonidos de personajes/objetos cuando se asignan a misiones
- Arte ASCII en pantallas de bienvenida
- Animaciones sencillas en pantallas de carga

## 💾 Persistencia de Datos

El sistema guarda automáticamente:
- Agendas de todos los recursos
- Misiones planificadas con detalles
- Misiones restantes por asignar
- Papelera de reciclaje (misiones que ya fueron planificadas)

## Funcionalidades Avanzadas ⚙️

### Búsqueda Automática de Horarios
Presiona [7] al seleccionar el día para que el sistema encuentre automáticamente el primer hueco disponible en el calendario semanal.

### Validación Inteligente
El sistema verifica:
1. Que no haya conflictos de recursos en el mismo día
2. Que se cumplan todos los co-requisitos
3. Que no se violen exclusiones mutuas
4. Que estén todos los recursos requeridos para la misión
5. Que no haya recursos prohibidos

## Solución de Problemas 🐛

### Error: "No module named 'pygame'"
pip install pygame
### Error: "No module named 'colorama'"
pip install colorama
### Error: "No module named 'pyfiglet'"
pip install pyfiglet
### El audio no se reproduce
Asegúrate de que la carpeta Audio/ esté en la misma ubicación que main_controller.py.

## Autor 👨‍💻

Ángel Arian Arias López.
- GitHub: [@AngelForever23] (https://github.com/AngelForever23)
- Proyecto: [STAR WARS MISSIONS PLANNER] (https://github.com/AngelForever23/STAR-WARS-MISSIONS-PLANNER)

## Próximas Actualizaciones 🔮

- [☸️] Implementación del Imperio Galáctico como segundo bando jugable ✅ (Completado)
- [👥] Añadir cantidades de recursos (pools) y manejo de excepciones
- [🏆] Sistema de logros
- [🎨] Interfaz gráfica (GUI)
- [▶️] Reproducción de clips de las películas al completar misiones

## EXTRA ✨

### Descarga o ve todas las péliculas y series de la saga gr4t1s (Requiere VPN en Cuba):

https://lucasltd66.wixsite.com/laswmovies 🔗

### Datos de interés sobre Star Wars (Wookieepedia | Fandom)

https://starwars.fandom.com 🔗

## ¡DISFRUTA!

Si te ha gustado este proyecto, deja tu ⭐ al repositorio en Github 😺.

Que la fuerza te acompañe a donde quiera que vayas... ✒️
│                                                       Obi-Wan Kenobi.