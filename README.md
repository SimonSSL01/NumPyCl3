# Laboratorio NumPy – 10 Ejercicios de Análisis de Datos

Este repositorio contiene la solución completa de la **Actividad de Aprendizaje No. 3** del curso de Análisis de Datos con NumPy.  
El objetivo es demostrar el uso de la biblioteca NumPy para resolver problemas reales de análisis de datos académicos, financieros, de inventario, producción, imágenes, sensores, encuestas y finanzas.

- **Solo NumPy**: No se utilizan listas de Python como estructura principal para los cálculos.
- **Código comentado**: Cada función y bloque está explicado brevemente.

## Requisitos

- Python 3.6 o superior
- NumPy (instalado automáticamente con el comando de instalación)

## Instalación y ejecución

1. Clona este repositorio:
   ```bash
   git clone https://github.com/SimonSSL01/NumPyCl3.git
   cd NumPyCl3

2. Instala NumPy (si no lo tienes):

    ```bash
    pip install numpy
    ```
---

## Resumen de los ejercicios
|Ejercicio|Tema|Descripción breve|
|---|---|---|
|1|Temperaturas|Estadísticas de 10 días: media, max, min, desviación, varianza, día más caluroso/frío.|
|2|Ventas|Matriz 3×4 (vendedores×meses). Total por vendedor, por mes, mejor/peor vendedor, promedio mensual.|
|3|Notas|Matriz 5×3 (estudiantes×materias). Promedios por estudiante/asignatura, mejor/peor, aprobados/reprobados.|
|4|Inventario|Matriz 4×3 (productos×sucursales). Producto con más existencia, sucursal con menos, total, promedio, productos agotados.|
|5|Producción|14 días × 2 líneas. Producción diaria, semanal, mensual y línea más productiva.|
|6|Imagen|Matriz 5×5 (escala de grises). Ajuste de brillo (+50/-50), inversión de colores y transpuesta.|
|7|Sensores IoT|10 mediciones. Detección de sensores fuera del rango [0.2, 0.8], promedio y desviación.|
|8|Encuesta|10 edades. Promedio, mediana, moda, edad máxima/mínima y conteo de mayores de edad.|
|9|Acción financiera|10 precios diarios. Promedio, máximo, mínimo, variación porcentual y días con precio superior al promedio.|
|10|Dashboard|Función genérica que recibe cualquier matriz NumPy y genera un reporte con todas las estadísticas básicas.|