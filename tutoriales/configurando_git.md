# TUTORIAL INSTALACION GIT EN WINDOWS Y LINUX

## Descripción

Archivo creado a base de una entrada en Deepseek para ayudarme a configurar github en 2 entornos 
de trabajo diferentes, como son Windows 10 y MXLinux.
En windows10 de momento estoy utilizando VSCode para editar codigo y en MXLinux de momento Nano.

A continuacion dejo a modo de respaldo el prompt y la respuesta generada por DeepSeek para
dicha configuracion Inicial.

## Prompt y respuesta

Estoy trabajando con un notebook con mxlinux y otro con windows 10, en windows uso visual studio code para escribir código, en linux por el momento uso nano, pero si corro en la terminal los codigos que creo. Entonces, necesito me ayudes a configurar mi cuenta de github en windows y visual studio code para poder crear mis proyectos de estudio, cargarlos en github y luego en linux poder configurar también para ir sincronizando el código en las carpetas locales y así poder correr y probar el código directo en la terminal de linux, y así de una vez, voy cargando mi github de código, así aprendo git, lo lleno y de pasada aumento mi portafolio, por ahora solo son códigos de prueba, para estudiar, de momento no tengo ningún proyecto principal, pero a futuro espero crear y respaldar proyectos de backend y frontend.
Dame los pasos para configurar github en windows y linux y enséñame a mantener sincronizado mi código.
Leer 10 páginas web
¡Perfecto! Me parece una excelente iniciativa. Pasar de usar nano a un flujo profesional con Git y GitHub es un gran paso, y hacerlo entre Windows y Linux te dará una base sólida para el futuro.

Aquí tienes una guía paso a paso para configurar todo tu entorno y mantener tu código sincronizado entre ambos sistemas.

Parte 1: Configuración en Windows (La Base Central)
Aquí crearás tus proyectos y los subirás a GitHub. Usaremos HTTPS con GitHub CLI, que es el método más moderno y seguro.

Paso 1: Instalar herramientas necesarias

Git para Windows: Descárgalo de git-scm.com. Incluye Git Bash (una terminal Linux para Windows) y Git Credential Manager.

GitHub CLI (gh): Es un programa para usar GitHub desde la terminal. Descárgalo de cli.github.com.

Visual Studio Code: Si no lo tienes, descárgalo de code.visualstudio.com. La integración con Git es automática.

Paso 2: Configurar tu identidad global

Abre Git Bash (búscalo en el menú inicio) y ejecuta estos dos comandos, sustituyendo por tu nombre y el correo de GitHub:

bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
Paso 3: Autenticarte con GitHub (Lo más importante)

Esto conecta tu PC con GitHub de forma segura. En la misma terminal (Git Bash), ejecuta:

bash
gh auth login
Te hará unas preguntas; responde así:

What is your preferred protocol for Git operations? Selecciona HTTPS (es el más universal y fácil).

Authenticate Git with your GitHub credentials? Selecciona Yes.

How would you like to authenticate GitHub CLI? Selecciona Login with a web browser.

First copy your one-time code: (Te mostrará un código). Selecciona y copia ese código (con el ratón o Ctrl+C).

Press Enter to open github.com...: Presiona Enter. Se abrirá una ventana en tu navegador.

En la web, pega el código y haz clic en "Authorize GitHub".

¡Listo! Windows ya está conectado a GitHub. Tus credenciales se guardan de forma segura en el "Administrador de credenciales" de Windows .

Paso 4: Crear y subir tu primer proyecto (Prueba de fuego)

Usaremos Visual Studio Code para esto.

Abre VS Code.

Ve al menú Ver -> Terminal (se abrirá una terminal abajo, puedes usar la de Git Bash o PowerShell).

Crea una carpeta para tu proyecto y navega a ella:

bash
mkdir mi-primer-proyecto
cd mi-primer-proyecto
Conviértela en un repositorio de Git y súbela a GitHub en unos pocos comandos:

bash
# Inicializa el repositorio
git init

# Crea un archivo de ejemplo
echo "# Mi Proyecto de Estudio" > README.md

# Prepara y guarda (commit) los cambios
git add README.md
git commit -m "Primer commit: agrego README"

# Crea el repositorio en GitHub y sube el código
gh repo create mi-primer-proyecto --public --source=. --remote=origin --push
Explicación del último comando: Le dice a gh que cree un repo público llamado "mi-primer-proyecto", usando la carpeta actual (.) como fuente, que conecte el remoto (origin) y que lo suba (--push) .

Ahora, si entras a github.com/tu-usuario/mi-primer-proyecto, ¡verás tu código!

Parte 2: Configuración en Linux (El Clon)
En tu MX Linux, solo necesitas "clonar" (descargar) el proyecto que creaste en Windows para trabajar en él.

Paso 1: Instalar Git

Abre tu terminal en Linux y escribe:

bash
sudo apt update
sudo apt install git
Paso 2: Configurar tu identidad (importante)

Debe coincidir con la de Windows para que los commits tengan el mismo autor.

bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
Paso 3: Clonar tu repositorio desde GitHub

Ve a la página de tu repositorio en github.com/tu-usuario/mi-primer-proyecto.

Haz clic en el botón verde Código.

Asegúrate de que esté en la pestaña HTTPS y copia la URL. Será algo como: https://github.com/tu-usuario/mi-primer-proyecto.git.

En tu terminal de Linux, navega a donde quieras guardar tus proyectos (por ejemplo, cd ~/Documentos) y ejecuta:

bash
git clone https://github.com/tu-usuario/mi-primer-proyecto.git
Te pedirá tu usuario y contraseña de GitHub (para la contraseña, usa un Personal Access Token que puedes crear en GitHub > Settings > Developer settings > Personal access tokens > Tokens (classic), ya que la contraseña normal no funciona desde terminales ).

Una vez clonado, entra en la carpeta: cd mi-primer-proyecto. ¡Ya tienes todo el código!

Parte 3: Flujo de Trabajo Sincronizado (¡El más importante!)
Ahora viene la magia. El ciclo de trabajo diario sería así:

Día 1: Trabajas en Linux (MX)

Abres tu terminal en Linux, vas a tu proyecto (cd ~/Documentos/mi-primer-proyecto).

Usas nano o tu editor favorito para crear o modificar código.

Al terminar, guardas los cambios en el historial de Git local y los subes a GitHub:

bash
# 1. Ver qué ha cambiado (opcional)
git status

# 2. Añadir los archivos que modificaste
git add .  # El "." añade todos los archivos nuevos y modificados

# 3. Crear un "commit" (una foto del estado actual)
git commit -m "Descripción clara de lo que cambié"

# 4. Subir el commit a GitHub
git push origin main
# (Si tu rama se llama 'master', usa 'master' en lugar de 'main')
Día 2: Continuas en Windows

Abres VS Code.

Abres la terminal integrada (Ver -> Terminal).

Navegas a tu proyecto (cd mi-primer-proyecto).

Antes de empezar a trabajar, es crucial que te traigas los últimos cambios que hiciste en Linux:

bash
git pull origin main
Ahora sí, puedes abrir los archivos (desde el explorador de VS Code) y seguir trabajando. Cuando termines, repites el ciclo git add, git commit -m, git push.

En resumen, el flujo universal es:
Acción	Comando	¿Dónde?	¿Qué hace?
Descargar cambios	git pull origin main	Linux y Windows	Trae el código más actual de GitHub a tu PC.
Subir cambios	git push origin main	Linux y Windows	Envía tus commits locales a GitHub.
Parte 4: Construyendo un Buen Portafolio (Consejos Clave)
Ignora lo innecesario con .gitignore: No querrás subir archivos temporales, de configuración local o las pesadas carpetas node_modules. Crea un archivo llamado .gitignore en la raíz de tu proyecto y escribe dentro, por ejemplo, node_modules/ o .env. GitHub tiene plantillas para lenguajes comunes.

Escribe buenos mensajes de commit: Olvídate de "cambios" o "update". Usa el imperativo y sé claro: git commit -m "Corrige error en el cálculo del IVA" o git commit -m "Agrega función para validar email". A futuro, esto te salvará la vida .

Usa ramas (branches) para no romper nada (Nivel Avanzado Principiante):
Cuando quieras probar algo nuevo, crea una rama:

bash
git checkout -b nueva-funcionalidad
Trabajas ahí, haces commits, y cuando funciona perfecto, la mezclas con tu rama principal (main). Esto es el pan de cada día en cualquier trabajo .

bash
# Estando en la rama 'nueva-funcionalidad'
git checkout main       # Volver a la rama principal
git pull origin main    # Asegurarse de tener lo último
git merge nueva-funcionalidad  # Mezclar los cambios
git push origin main    # Subir la mezcla a GitHub
Siguiendo esta guía, no solo estarás aprendiendo a programar, sino que estarás practicando el flujo de trabajo estándar de la industria. ¡Mucha suerte con tus estudios y tu portafolio!
