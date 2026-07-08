# Análisis Comparativo de Rendimiento: Locust vs. JMeter

Este documento contiene la plantilla y estructura para comparar las herramientas de pruebas de carga **Locust** y **Apache JMeter** utilizadas sobre la aplicación de Registro de Asistencia.

## Tabla Comparativa de Resultados

Complete la siguiente tabla tras la ejecución de las pruebas con una configuración de carga idéntica en ambas herramientas (por ejemplo: 50 usuarios concurrentes, tasa de subida de 5 usuarios/segundo, durante 3 minutos).

| Criterio de Evaluación | Locust | Apache JMeter |
| :--- | :--- | :--- |
| **Tiempos de respuesta** <br>*(Promedio, Mínimo, Máximo)* | | |
| **Número de solicitudes procesadas** <br>*(Total y por segundo - RPS)* | | |
| **Errores detectados** <br>*(Cantidad total y porcentaje de error)* | | |
| **Percentiles de tiempo** <br>*(p50, p90, p95, p99)* | | |
| **Capacidad de la aplicación para manejar la carga simulada** <br>*(Análisis cualitativo y de cuello de botella)* | | |

---

## Preguntas de Discusión y Conclusiones

### 1. Observaciones sobre los Tiempos de Respuesta y Percentiles
*¿Qué diferencias se observan en la distribución de los tiempos de respuesta? ¿Alguna herramienta reporta mayor variabilidad?*

### 2. Eficiencia y Facilidad de Simulación
*¿Cómo se compara la experiencia de programar las pruebas en Python (Locust) frente a la interfaz gráfica de usuario y archivos XML (JMeter)?*

### 3. Consumo de Recursos del Cliente de Pruebas
*¿Cuál de las dos herramientas consume más memoria/CPU en la máquina local al escalar el número de usuarios?*
