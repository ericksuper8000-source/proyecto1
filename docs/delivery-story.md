# DELIVERY STORY — Flujo real de entrega

> **Type:** Interactive living story (memory aid, not spec)
> **Version:** v1.0 (approved 2026-09-30)
> **Scope:** Only validated concepts up to Phase 8 + audit 2026-09-29. Phases 9–14 as upcoming map only.
> **Rule:** This story is told at the start of EVERY CICD work session, BEFORE the general summary.
> Every time a new concept is validated, this file grows (v1.1, v1.2...). Never shrink it,
> never introduce unvalidated tech. Rest of the session workflow stays unchanged.

---

## How to use

1. Mentor tells the full story below before the general journey summary.
2. Then per-topic recap cycle (1–2 blocks) + work session, unchanged.
3. When Phase 9 (VPS) is validated, append it keeping the same format.

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

---

## Changelog

- **v1.0 (2026-09-30):** Approved version. Covers Phases 1–8 + audit 2026-09-29. Official verdict after `push` (local as rehearsal).
- **Next:** Append Phase 9 when validated (VPS Oracle, first SSH connection).
