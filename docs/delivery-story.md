# DELIVERY STORY — Flujo real de entrega

> **Type:** Interactive living story (memory aid, not spec)
> **Version:** v2.8 (2026-10-21)
> **Scope:** Only validated concepts up to Phase 8 + audit 2026-09-29. Phases 9–14 as upcoming map only.
> **Rule:** This story is **source material** for the mandatory concept-by-concept review.
> It is told **incrementally**, never as a full monologue and never as a general summary.
> Every time a new concept is validated, this file grows (v1.1, v1.2...). Never shrink it,
> never introduce unvalidated tech. Rest of the session workflow stays unchanged.

---

## How to use

1. Mentor uses this story as **source material** for the mandatory v3 review.
2. Tell it **incrementally**: one concept at a time, with the v3 cycle (simple explanation +
   example/analogy → connection to previous concepts → comprehension check + questions →
   wait for "asimilado y sin preguntas" → next concept).
3. Never dump the full story as a monologue or as a general summary.
4. When Phase 9 (VPS) is validated, append it keeping the same format.

---

## Guía del pipeline CI/CD (10 etapas)

**1. Código Fuente.**
Qué es: `Principal.py` (`suma`, `division`, `es_par`, loop cada 5s) y `test_principal.py` (4 pruebas que importan esas funciones y fijan resultados).
Para qué sirve: es el único valor real; sin programa no hay nada que cuidar. Si faltara, el resto es vacío.
Qué archivo hace qué: `Principal.py` propone el comportamiento; `test_principal.py` lo comprueba.
Conectividad: se escriben en local y viajan juntos en el `push` del paso 4. No se prueban oficialmente aquí.

**2. Gestión de Dependencias.**
Qué es: `requirements.txt` con una línea clavada (`pytest==9.0.3`; `==` = exactamente esa, fijada tras el recall PYSEC-2026-1845).
Para qué sirve: que tu PC, los dos robots y la fábrica instalen lo mismo con la orden de instalar la lista. Aporta reproducibilidad. Si fuera flexible o faltara, cada máquina armaría algo distinto.
Qué archivo hace qué: esta lista viaja en el mismo `push` y será leída después por los robots y la fábrica.
Conectividad: se escribe en local, viaja con el código y se usa oficialmente tras el `push`.

**Explicación canónica (v1.2 — 2026-10-21):**
- `requirements.txt` **no instala Python**: lista paquetes de Python. Python 3.11 se define
  en `setup-python`, la imagen de GitLab y `FROM python:3.11-slim`.
- Aquí solo hay `pytest==9.0.3`; `==` fija la versión exacta. Es una dependencia de
  **pruebas**: `Principal.py` usa solo la librería estándar.
- Analogía: el código es la receta; `requirements.txt` es la lista de compra con marca y
  versión exactas; el pipeline es la cocina que compra esa lista antes de cocinar. Sin
  versión fija, cada cocina usa una sal distinta; sin lista, no sabe qué comprar.
- Proyecto ambicioso: runtime vs dev/test; versiones (`==`, `~=`, rangos); transitivas y
  lock files; marcadores de entorno; extras; índices privados/hashes; composición (`-r`, `-c`).
- Afecta: instalación local, tests de CI, `pip-audit`, build/caché/imagen de Docker,
  runtime/deploy, reproducibilidad/rollback y supply chain.
- En este proyecto: la app solo usa stdlib; pytest es de pruebas; las herramientas de
  calidad se instalan en CI sin pin (deuda); el Dockerfile instala pytest en la imagen final
  (optimización futura).

**3. Calidad y Seguridad.**
Qué es: 7 revisores que se ensayan en local con Python 3.11.9 y cuyo veredicto oficial corre en los repos tras tu `push`.
- **Ruff:** lee todo en segundos y marca descuidos (a nosotros nos frenó por imports desordenados en `test_principal.py`). Sirve para cazar errores baratos al instante, antes de que ensucien lo demás.
- **Flake8:** revisa que el código se lea igual siempre (espacios, líneas, nombres). No mira si suma bien, mira si otro lo entiende. Sirve para mantenerlo legible.
- **Black `--check`:** revisa que el formato sea idéntico. En tu PC arregla, en CI solo informa: si está chueco reprueba y tú lo planchas en local. Sirve para cero discusiones de estilo.
- **MyPy:** revisa que los tipos coincidan sin correr el programa (si una función espera número y llega texto, avisa). Sirve para frenar choques que explotarían corriendo.
- **Pytest:** corre tus 4 pruebas reales de `test_principal.py` (`suma`, `division`, par verdadero/falso). Sirve para probar que lo prometido se cumple.
- **Bandit:** revisa `Principal.py` buscando secretos olvidados o llamadas peligrosas. Ignora tests a propósito (un `assert` ahí no es riesgo). Sirve para no embarcar claves.
- **pip-audit:** lee tu `requirements.txt` y la compara con fallas publicadas. Nos subió `pytest` por el recall PYSEC. Sirve para no montar piezas con falla conocida.
Para qué en conjunto: si las 7 están en verde, se puede fabricar; si una falla, su trabajo se pone rojo y por `needs` frena a `docker`. Si faltaran, lo roto se empaca y viaja hasta el servidor.
Qué archivo hace qué: ningún archivo nuevo; son programas que leen tu código y tu lista, igual en local y en CI.
Conectividad: se ensayan en local, se ejecutan oficialmente en el paso 5 tras el `push`, y frenan a fábrica.

**La puerta de calidad/seguridad (v1.4 — 2026-10-21):** no es una herramienta, es un equipo
de revisores. Ruff (lint rápido), Flake8 (estilo), Black `--check` (formato), MyPy (tipos),
Pytest (comportamiento), Bandit (seguridad del código), pip-audit (vulnerabilidades de
dependencias). Los tests prueban comportamiento; la puerta añade legibilidad, tipos,
seguridad y salud de dependencias. GitHub corre `lint`/`test`/`security` en paralelo y
`docker` necesita los tres; GitLab va `lint→test→security`. Si uno falla, no se fabrica ni
publica. Analogía: inspectores en el pase de cocina; el plato sale solo si pasan todos. Hay
solapamiento (Ruff/Flake8/Black) y ninguna herramienta es infalible.

**Ruff — explicación canónica (v1.5 — 2026-10-21):** linter estático en Rust; lee el código
sin ejecutarlo y es muy rápido. Detecta imports/variables sin usar, nombres no definidos,
comparaciones sospechosas, `except` amplios, código muerto y f-strings sin variables. No
ejecuta tests, no comprueba tipos, no busca secretos ni audita dependencias; puede formatear
con `ruff format`, pero aquí no se usa para eso. En CI corre `ruff check .` dentro del job
`lint`; si falla, `docker` no se ejecuta por `needs`. En este repo no hay `pyproject.toml` ni
`ruff.toml`, así que usa reglas por defecto. Analogía: inspector rápido con checklist;
detecta lo barato, no la calidad profunda. Se solapa con Flake8; en un proyecto real podrías
consolidarlos.

**Flake8 — explicación canónica (v1.6 — 2026-10-21):** linter estático de Python; combina
PyFlakes (errores simples), pycodestyle (estilo PEP 8) y mccabe (complejidad). Reporta, no
reescribe. Detecta líneas largas, espacios/sangría, líneas en blanco, imports sin usar,
nombres no definidos, comparaciones raras con `None`, `except` vacíos/amplios y complejidad
innecesaria. No ejecuta tests, no comprueba tipos, no busca secretos, no audita dependencias
ni arregla formato. En CI corre `flake8 .` en el job `lint`; si falla, `docker` no se ejecuta
por `needs`. Se solapa con Ruff; en un proyecto real podrías consolidarlos. Contraste clave
con Black: Flake8 informa, Black reescribe. Analogía: corrector de estilo del código; revisa
que la receta sea legible, no si el plato sabe bien o los ingredientes son seguros.

**Black — explicación canónica (v1.7 — 2026-10-21):** formateador, no linter. Reescribe a un
formato único; es opinionated y determinista. Normaliza comillas, espacios, paréntesis, saltos
de línea y 88 columnas por defecto; no cambia lógica, no renombra variables, no ordena imports
ni corrige errores. En local `black .` reescribe; en CI `black --check .` solo verifica. Si
falla, ejecuta Black en local, revisa el diff y vuelve a commitear. No ejecuta tests, no
comprueba tipos, no busca secretos, no audita dependencias ni detecta lógica. Corre en `lint`
después de Flake8 y antes de Ruff/MyPy; si falla, `docker` no se ejecuta. Contraste: Flake8
informa, Black reescribe. Usa 88 columnas y Flake8 79; en proyectos reales se alinean.
Analogía: el planchador/maquetador del código; deja la presentación impecable, no decide si
la receta es buena o segura.

**MyPy — explicación canónica (v1.8 — 2026-10-21):** chequeador de tipos estático; lee las
anotaciones y verifica coherencia sin ejecutar. Detecta argumentos/retornos incompatibles,
`Optional` sin comprobar `None`, contenedores/atributos incompatibles; no detecta lógica,
división por cero, tests, estilo, secretos ni dependencias. Python no aplica los tipos en
runtime; son una promesa que MyPy verifica antes. En este proyecto `Principal.py` y
`test_principal.py` no tienen anotaciones, así que `mypy .` corre pero su cobertura real es
limitada; anotar funciones es una deuda/mejora. Corre al final del job `lint`; si falla,
`docker` no se ejecuta. Analogía: inspector de medidas/unidades; verifica gramos vs litros
antes de cocinar, no prueba el plato ni revisa la higiene.

**Bandit — explicación canónica (v1.9 — 2026-10-21):** escáner de seguridad estático (SAST)
para Python; lee el código sin ejecutarlo y busca patrones peligrosos: secretos hardcodeados,
`eval`/`exec`, `pickle`, `yaml.load`, `subprocess` con `shell=True`, `os.system`, `assert` en
producción, cripto débil. Reporta severidad y confianza; requiere triage. En el proyecto corre
`bandit -r . -x "./__pycache__,./test_principal.py"` en el job `security`; excluye tests
porque usan `assert` a propósito y `assert` se elimina con `python -O`. No detecta CVEs de
dependencias (eso es pip-audit), no ejecuta el programa ni sustituye revisión humana. Si falla,
`security` se pone rojo y `docker` no corre. Analogía: inspector de higiene de la cocina;
revisa carne cruda junto a la ensalada, no prueba el plato ni las etiquetas del proveedor.

**pip-audit — explicación canónica (v2.0 — 2026-10-21):** auditor de seguridad de
dependencias; resuelve `requirements.txt` (incluidas transitivas) y compara versiones con
PyPI Advisory Database/OSV. En el proyecto corre `pip-audit -r requirements.txt` en el job
`security`; audita también las dependencias transitivas de pytest. Si encuentra un CVE
conocido, `security` falla y `docker` no se ejecuta. No escanea tu código (eso es Bandit),
no detecta zero-days/malware desconocido, no audita el SO, la imagen base ni GitHub Actions,
y no garantiza que un paquete sea seguro. `requirements.txt` no es un lock file: el resultado
puede cambiar si cambian las transitivas; un lock mejora la reproducibilidad, no la
seguridad. Analogía: inspector de recalls del proveedor; Bandit revisa cómo cocinas,
pip-audit revisa qué ingredientes usas.

**Git/`.gitignore` — explicación canónica (v2.1 — 2026-10-21):** Git guarda snapshots en
tres zonas: working tree, staging (`git add`) y repositorio (commits). `.gitignore` excluye
archivos **no trackeados**; no los borra. Si ya están trackeados, hay que `git rm --cached` y
commitear. En el proyecto ignora `_archive/`, cachés de Python/pytest/MyPy/Ruff, `.venv/`,
basura de sistema/editor, claves/`.env` (con `!.env.example`) y logs. Sí se commitean código,
tests, requirements, Dockerfile, CI, `.gitignore`, `.gitattributes` y docs. No es barrera de
seguridad: un secreto ya commiteado sigue en el historial; hay que rotarlo y eliminarlo.
`.gitattributes` controla finales de línea, no qué se ignora. Analogía: Git es el álbum de
fotos del proyecto; `.gitignore` es la lista de lo que no quieres fotografiar.

**YAML/pipelines — explicación canónica (v2.2 — 2026-10-21):** YAML describe datos y
configuración; no ejecuta. La indentación (dos espacios, nunca tabs), `clave: valor` y las
listas con `-` definen la estructura; conviene entrecomillar `"3.11"` y cadenas con `:`.
GitHub Actions: `on` (push a develop, PR a master), `jobs` lint/test/security/docker,
`runs-on`, `steps` con `uses:`/`run:` y `needs` para que docker espere a los tres. Cada job
usa un runner limpio; lint/test/security corren en paralelo y docker después. GitLab usa
stages lint→test→security, con un job por stage (secuencial) y solo validación; la publicación
ocurre en GitHub (ADR-0007). El YAML es la orden de trabajo; el runner es el taller. Analogía:
orden de trabajo de un taller con estaciones y orden de ejecución.

**Flujo del push — explicación canónica (v2.3 — 2026-10-21):** `commit` guarda un snapshot
local; `push` envía esos commits a un remoto, no el working tree ni los archivos ignorados.
Remotos del proyecto: `github` (`proyecto1`, principal, pipeline completo y publicación) y
`gitlab` (`repo2`, espejo, solo validación); no hay `origin`. `develop` es la rama de trabajo
y `master` la vitrina. Flujo: status → add → commit → fetch github → push github develop; el
push dispara el workflow de GitHub (lint/test/security, y docker solo si pasan). Lo local es
ensayo; el veredicto oficial es el CI remoto. El espejo se empuja aparte (`git push gitlab
develop`). El PR develop→master también dispara CI; un push a feature no, y un push directo a
master no está en el `on`. Si el push es rechazado, fetch/integra; no fuerces ramas
compartidas. Analogía: el commit cierra y etiqueta el paquete; el push lo entrega en el
edificio central; los inspectores deciden si pasa a fábrica.

**Docker/Dockerfile — explicación canónica (v2.4 — 2026-10-21):** Dockerfile es la receta;
la imagen es el paquete inmutable con Python, dependencias y código; el contenedor es una
instancia en ejecución. El Dockerfile usa `FROM python:3.11-slim`, variables para no generar
`.pyc` y no bufferizar logs, `WORKDIR /app`, copia `requirements.txt`, instala con
`--no-cache-dir`, copia `Principal.py` y arranca con `CMD ["python", "Principal.py"]`. Se
construye con `docker build -t mi-app:latest .` y se ejecuta con `docker run --rm mi-app`.
El orden aprovecha la caché por capas: cambios de código no reinstalan dependencias; cambios
de requirements sí. Deudas: instala pytest aunque no copia tests, corre como root, no expone
puerto y la etiqueta base puede moverse. Analogía: receta → kit de comida sellado → kit
abierto y funcionando.

**`.dockerignore` — explicación canónica (v2.5 — 2026-10-21):** filtra el contexto de build
que `docker build ... .` envía al daemon; no borra archivos locales, no cambia Git y no altera
la imagen por sí solo: lo que entra lo decide `COPY`. Se diferencia de `.gitignore` en que
puede excluir archivos trackeados, como `docs/`. El proyecto excluye `.git`, cachés/venvs,
logs, basura de sistema/editor, claves/`.env`, `_archive/`, `docs/`, `screenshots/`, `scripts/`
y `CICD.txt`; conserva `requirements.txt` y `Principal.py`. Beneficios: contexto más pequeño,
builds más rápidos, menos invalidaciones de caché y menos riesgo de secretos. Un secreto ya
cocinado en una capa vieja no se arregla agregándolo después: hay que reconstruir y rotarlo.
Analogía: `.gitignore` decide qué no va al álbum; `.dockerignore` decide qué no va en la caja
de envío al taller.

**Registries — explicación canónica (v2.6 — 2026-10-21):** un registry es un almacén de
imágenes Docker (capas), no de código. El proyecto publica la misma imagen en Docker Hub
(`erickdev8/mi-app`, consumo), GHCR (`ghcr.io/ericksuper8000-source/mi-app`) y GitLab
(`registry.gitlab.com/ericksuper80-group/repo2`) para no depender de uno solo; solo GitHub
Actions publica (ADR-0007) y GitLab solo valida. El job hace login con tokens y
`--password-stdin`, construye una vez, etiqueta con los 8 primeros caracteres del commit y
`latest`, crea alias con `docker tag` y hace `docker push` a cada registry. La etiqueta del
commit rastrea la imagen hasta el código; `latest` es móvil; el digest es inmutable. Un
registry no es un remoto Git: Git mueve texto, el registry mueve imágenes. Analogía: almacén
de kits sellados con dirección y etiqueta; `latest` es el más reciente del estante y el SHA
es el número de lote.

**Compose/Watchtower — explicación canónica (v2.7 — 2026-10-21):** Compose declara el estado
deseado de varios contenedores y el Engine lo ejecuta; aquí no construye, descarga la imagen.
`docker-compose.yml` define `app` (`mi-app:latest`, nombre fijo, `restart: always`; imprime
cada 5s en bucle) y `watchtower` (versión fija `1.7.1`, `restart: always`, monta
`/var/run/docker.sock`, `DOCKER_API_VERSION=1.41`, `--interval 30`). `docker compose up -d` lo
levanta; `ps`, `logs -f app` y `down` ayudan a operarlo. Watchtower revisa cada 30s, y si hay
imagen nueva hace pull y recrea el contenedor; no reconstruye. `latest` es deliberado solo en
local para simular CD (ADR-0004); el VPS fijará la etiqueta del commit. Montar el socket da
control poderoso sobre Docker: es aceptable en ensayo local, no ideal en producción.
Analogía: Compose es el director de orquesta; Watchtower es el vigilante nocturno que cambia
el kit viejo por el nuevo.

**SSH/VPS — explicación canónica (v2.8 — 2026-10-21):** el VPS es una máquina Linux remota,
persistente y sin monitor, con IP propia; no es un contenedor, es la máquina donde Docker
corre contenedores. SSH es la puerta cifrada: el cliente `ssh` habla con `sshd` en el puerto
22 y obtiene una shell remota. Al conectar, el servidor muestra su host key; la primera vez
aparece el aviso de autenticidad y se guarda en `known_hosts`. La llave pública es el candado
que se deja en el servidor; la privada nunca sale del equipo y responde al desafío. Una llave
por puerta: GitHub, GitLab y VPS (`id_ed25519_vps`), con alias `mi-vps` en `~/.ssh/config`.
El VPS baja la imagen del registry y nunca construye; se usará la etiqueta del commit, no
`latest`. Cerrar SSH no apaga el servidor ni los contenedores. Analogía: casa remota sin
recepción, puerta blindada, candado público y llave privada en el bolsillo.

**Tests — concepto separado (v1.3 — 2026-10-21):**
- La pieza angular es la **práctica** de verificar comportamiento de forma automática y
  repetible; `test_*.py` es solo la convención de descubrimiento de pytest.
- La mayoría de proyectos de producción tienen tests automatizados, pero "todos los
  proyectos serios" es demasiado absoluto: prototipos/scripts pueden no tenerlos; los
  sistemas críticos normalmente sí. Hay tests unitarios, de integración, end-to-end, de API,
  de carga y de seguridad; no todos son `test_*.py`.
- Solo los tests prueban que el programa hace lo que promete; lint/formato/tipos/seguridad
  no prueban corrección. Sin tests, un pipeline verde puede publicar comportamiento erróneo.
- **20 archivos `.py` ≠ 20 tests:** se testea por comportamiento/riesgo, no por archivo. Un
  test puede cruzar varios archivos; un archivo puede necesitar muchos casos.
- **Pirámide:** muchos unitarios (rápidos, aislados), menos de integración, pocos end-to-end
  (lentos). No todo archivo necesita test unitario (código generado, configuración,
  envoltorios triviales, scripts de un solo uso).
- **Cobertura:** 100% no significa buenos tests; es un mapa para encontrar huecos, no una meta.
- Aquí: `test_principal.py` tiene 4 casos para 3 funciones; no prueba el bucle `while True`
  ni la división por cero. En un proyecto de 20 archivos se organiza por módulo/feature y se
  añaden tests de integración para flujos que cruzan archivos.
- Analogía: código = receta; `requirements.txt` = lista de compra; tests = el catador/control
  de calidad en el pase. No hace falta un catador por cocinero; se controlan los puntos críticos.

**4. Control de Versiones.**
Qué es: Git (`.git/` historia local), ramas `develop` (taller) y `master` (vitrina), espejado en GitHub (`proyecto1`) y GitLab (`repo2`), con `.gitignore` que filtra lo que no va al archivo (entornos, temporales, `.env`, claves).
Para qué sirve: historial público, respaldo en dos casas y encendido de robots. Si faltara, no hay disparo ni prueba de avance.
Qué archivo hace qué: `.git` guarda, los remotos copian, `.gitignore` filtra.
Conectividad: recibe tu código validado en local y con `push` a `develop` lo sube y enciende al paso 5. Las pruebas oficiales empiezan aquí, no antes. Antes de comparar, `fetch`.

**5. Orquestadores de CI.**
Qué es: dos recetas escritas (YAML donde un espacio roto tumba todo) más sus cuadrillas que sí trabajan (`ubuntu-latest`, `python:3.11`). El papel no ejecuta; el runner sí, y solo trabaja con lo que acaba de subir.
Para qué sirve: repetir controles y fabricar sin manos, igual siempre.
Qué archivo hace qué: `.github/workflows/ci.yml` despierta con `push` a `develop`/pedido a `master`, corre `lint/test/security` en paralelo y `docker` solo si los 3 pasan (esa línea de `needs` es el freno). En cada trabajo los pasos van en fila: clona el texto, coloca Python 3.11, instala, corre (sin clonar no hay qué revisar). `.gitlab-ci.yml` declara turnos `lint→test→security`, cada trabajo con turno, máquina y guion, sin fabricar (por decisión GitHub fabrica, GitLab revisa). Secretos viven en cada plataforma, nunca en el repo.
Conectividad: recibe texto clonado + secretos de su plataforma; entrega veredicto y, solo GitHub, la imagen a los almacenes. El plano de despliegue aquí solo viaja como texto, nadie lo ejecuta en CI.

**6. Contenedorización.**
Qué es: `Dockerfile` (plano: base, avisos, piso `WORKDIR`, copiar lista e instalar **antes** que el código porque esa pareja fragua y se reusa —si inviertes el orden cada coma reinstala—, copiar programa, botón `CMD`; cada renglón necesita al anterior) más `.dockerignore` (lo que no sube al camión: entornos, temporales, docs, secretos = liviano y sin claves; `.gitignore` es otra lista: lo que no va al archivo).
Para qué sirve: que corra igual en todas partes. Si metes secretos viajan dentro.
Qué archivo hace qué: `Dockerfile` ordena, `.dockerignore` filtra, el contexto es lo que sí viaja.
Conectividad: recibe código + lista del clon del robot (ya probados oficialmente) y entrega imagen sellada con 2 etiquetas (commit exacto + última). Fabricar sella, servir usa.

**7. Almacenes de Imágenes.**
Qué es: 3 servidores que guardan la misma imagen con 3 direcciones: Docker Hub (consumo), GHCR y GitLab (respaldo), cada una con etiqueta exacta de commit y `latest` móvil.
Para qué sirve: el disco del robot se borra; sin almacén se pierde. Con 3 no dependes de uno.
Qué archivo hace qué: ningún archivo nuevo; el trabajo `docker` pone otros nombres a la misma (`tag` sin reconstruir) y la sube (`push`); para bajar se pide por nombre:etiqueta (`pull`). La clave viaja por tubo cerrado.
Conectividad: recibe del paso 5, entrega al paso 8. Git mueve texto, el almacén mueve imágenes.

**8. Despliegue y Orquestación Local.**
Qué es cada pieza y dónde vive en tu Windows hoy: **Docker Desktop** = programa de tu PC que por dentro levanta una máquina Linux con todo (ejecutor + lector + línea de armado). **`docker compose` (lector)** = comando de tu terminal que lee el plano **del disco donde escribes** (hoy `C:\Repo2`, nunca del almacén). **Engine (ejecutor)** = servicio dentro de esa máquina interna que guarda imágenes, crea contenedores y los prende; le hablas por el teléfono interno (en Windows por Desktop, por dentro el socket que el plano le presta incluso a Watchtower).
Qué archivo hace qué: `docker-compose.yml` describe (`app` con imagen de Docker Hub + nombre + reabrir solo; `watchtower` con versión fija + teléfono + ritmo 30s). Al escribir `up` en ese disco el lector llama por teléfono y el ejecutor mira su disco, si falta baja del almacén, crea, prende y conecta. Descargar surte sin apagar; abrir usa lo guardado; los expertos surten primero. En servidor jamás se fabrica. En Windows llegan juntos con Desktop; en Linux futuro vendrán como paquetes separados con la misma relación.
Conectividad: el plano llega por `clone` (texto), la imagen por `pull` (capas). Sin lector nadie ordena; sin ejecutor nadie hace.

**9. Ensayo y Acceso Remoto.**
Qué es: Watchtower, contenedor prendido **por Engine** con pase al teléfono; su programa interno cada 30s pregunta si hay etiqueta nueva de lo servido y si la hay le ordena a Engine parar, borrar, bajar y recrear con los mismos datos (no reconstruye). Solo ensayo local: ciego, sin salud, con llave maestra. Y SSH validado: escucha en extensión 22, aviso anti-impostor la primera vez, privada que nunca viaja + pública que sí, llavero con una por puerta (GitHub, GitLab, servidor reservada), servidores sin monitor.
Para qué sirve: practicar el cambio hoy y tener la puerta lista para mañana.
Qué archivo hace qué: la línea de Watchtower vive dentro del plano; las llaves viven en `~/.ssh/` con etiquetas.
Conectividad: vigila lo servido y deja el túnel pronto para el terreno.

**10. Resumen y Reglas de Oro.**
Escribes → subes (`push`) → en los repos corren los 7 → 1 fabricada y guardada ×3 → el plano viaja por clon → el lector (tu terminal) pide por teléfono → el ejecutor (máquina interna/servidor) surte y abre → el ensayo practica → mañana igual en terreno.
Reglas: orden exacta con máquina exacta; el lector ordena y el ejecutor ejecuta; Git mueve texto y el almacén mueve imágenes; una llave por puerta.

**Principio permanente (2026-10-21):** el pipeline nace de la aplicación. El código define el stack; el stack define dependencias, pruebas, build y, por tanto, las herramientas del pipeline. No se diseña un pipeline sin saber qué aplicación va a correr. Las etapas genéricas son universales; los comandos y herramientas son específicos del stack. Analogía: no construyes la carretera antes de saber si pasarán coches o trenes.

---

## Changelog

- **v1.0 (2026-09-30):** Approved version. Covers Phases 1–8 + audit 2026-09-29. Official verdict after `push` (local as rehearsal).
- **v1.1 (2026-10-21):** Added the permanent principle "the pipeline is born from the application" (student insight) and updated the rule: the story is source material, told incrementally in the v3 interactive review, never as a monologue.
- **v1.2 (2026-10-21):** Concept 2 — Dependencies validated. Added the canonical explanation:
  `requirements.txt` lists packages (not Python); pytest is the only test dependency; salt
  analogy; runtime vs dev, pins/lock files, and effects on CI, Docker, security and
  reproducibility. Student asked to keep this explanation consistent in future reviews.
- **v1.3 (2026-10-21):** Concept 3 — Tests validated. Added the canonical explanation: the
  practice of automated testing (not the filename), most production projects have tests but
  not all, tests by behavior/risk not 1:1 with files, test pyramid, coverage caveat, and the
  project's 4 basic cases + gaps.
- **v1.4 (2026-10-21):** Concept 4 — Quality/Security gate validated as one concept (7
  reviewers, each answers a different question; GitHub parallel jobs + `needs`; GitLab
  sequential stages; inspectors analogy; overlap and fallibility).
- **v1.5 (2026-10-21):** Concept 5 — Ruff validated. Added canonical explanation: static
  Rust linter, what it catches and does not catch, `ruff check .` in the lint job, default
  rules (no config here), and the fast-inspector analogy.
- **v1.6 (2026-10-21):** Concept 6 — Flake8 validated. Added canonical explanation: static
  linter (PyFlakes + pycodestyle + mccabe), reports but does not rewrite, default config,
  overlap with Ruff, contrast with Black, and the style-proofreader analogy.
- **v1.7 (2026-10-21):** Concept 7 — Black validated. Added canonical explanation: formatter
  (not linter), deterministic/opinionated, local rewrite vs CI `--check`, 88 columns, no
  logic/import changes, contrast with Flake8 and Ruff, and the ironer/typesetter analogy.
- **v1.8 (2026-10-21):** Concept 8 — MyPy validated. Added canonical explanation: static
  type checker, what it catches/does not catch, Python types not enforced at runtime, no
  annotations in this project (limited real coverage/debt), pipeline placement, and the
  measurement/unit-inspector analogy.
- **v1.9 (2026-10-21):** Concept 9 — Bandit validated. Added canonical explanation: static
  security scanner, dangerous patterns, severity/confidence triage, test exclusion for
  `assert`, pipeline placement, limits vs pip-audit, and the hygiene-inspector analogy.
- **v2.0 (2026-10-21):** Concept 10 — pip-audit validated. Added canonical explanation:
  dependency auditor, transitive resolution, known CVEs, pipeline placement, lock-file
  caveat, limits vs Bandit, and the supplier-recalls analogy.
- **v2.1 (2026-10-21):** Concept 11 — Git/`.gitignore` validated. Added canonical
  explanation: working tree/staging/repository, untracked-only behavior, project rules,
  tracked-file caveat, secret-history caveat, `.gitattributes` distinction, and the photo
  album analogy.
- **v2.2 (2026-10-21):** Concept 12 — YAML/pipelines validated. Added canonical explanation:
  YAML syntax, triggers, jobs/steps/needs, fresh runners, parallel vs sequential execution,
  GitHub vs GitLab schemas, validation-only GitLab, and the workshop work-order analogy.
- **v2.3 (2026-10-21):** Concept 13 — push flow validated. Added canonical explanation:
  commit vs push, remotes, develop/master, trigger behavior, mirror push, PR flow, fetch vs
  pull, non-fast-forward handling, and the package-delivery analogy.
- **v2.4 (2026-10-21):** Concept 14 — Docker/Dockerfile validated. Added canonical
  explanation: Dockerfile vs image vs container, project instructions, build vs run, layer
  cache, debt (pytest, root, no EXPOSE, mutable tag), and the meal-kit analogy.
- **v2.5 (2026-10-21):** Concept 15 — `.dockerignore` validated. Added canonical
  explanation: build-context filtering, diff vs `.gitignore`, project exclusions, what must
  stay, cache/security benefits, and the shipping-box analogy.
- **v2.6 (2026-10-21):** Concept 16 — registries validated. Added canonical explanation:
  three registries, image naming, login/tag/push flow, token security, commit vs `latest`
  tags, push/pull layers, and the warehouse analogy.
- **v2.7 (2026-10-21):** Concept 17 — Compose/Watchtower validated. Added canonical
  explanation: declarative services, app/watchtower config, Compose vs Engine, CD simulation,
  local `latest` vs VPS commit tag, socket security, and the conductor/watchman analogy.
- **v2.8 (2026-10-21):** Concept 18 — SSH/VPS validated. Added canonical explanation: VPS vs
  container, SSH client/server/port 22, host-key warning, key pairs, per-door keys, VPS pulls
  images, and the remote-house/padlock analogy. The v3 review list is complete.
- **Next:** Append Phase 9 when validated (VPS Oracle, first SSH connection).
