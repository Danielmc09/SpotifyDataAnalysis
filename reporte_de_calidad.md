# Reporte de Análisis de Calidad de Datos de Spotify

## Descripción del Proyecto

Análisis de calidad de datos de las pistas musicales de Taylor Swift obtenidas de la API de Spotify. El propósito es identificar y reportar anomalías para asegurar la integridad y la calidad de los datos.

## Proceso de Análisis de Calidad de Datos

### 1. Extracción de Datos

- **Archivo de Entrada**: `taylor_swift_spotify.json`
- Datos extraídos de la API de Spotify que contienen información detallada sobre álbumes y pistas.

### 2. Transformación y Limpieza

- **Script de Procesamiento**: `analisis_file.py`
- Convertimos los datos JSON a un formato CSV estructurado.
- Realizamos limpieza inicial, normalizando y estandarizando los datos.

### 3. Análisis de Calidad de Datos

- **Script de Análisis**: `analyze_data_quality.py`
- **Aspectos Analizados**:
  - **Duplicados**: Identifica y cuenta las filas duplicadas en el dataset.
  - **Valores Nulos**: Enumera y cuenta los valores nulos en cada columna del dataset.
  - **Unicidad**: Verifica la unicidad de los identificadores de las pistas para asegurar que no hayan repetidos. 

### 4. Reporte de Anomalías

- **Archivo de Salida**: `anomalies_report.csv`
- Documentamos todas las anomalías detectadas durante el análisis.
- El reporte incluye el tipo de anomalía, una descripción y detalles específicos.

## Tecnologías Utilizadas

- Python
- Pandas
- JSON

## Conclusión

Este análisis proporciona una visión general de la calidad de los datos de Spotify, destacando áreas críticas que necesitan atención para garantizar análisis futuros precisos y confiables. Los resultados ayudan a guiar las decisiones de limpieza y mejora de datos.

Autor: <a href="https://www.linkedin.com/in/angeldanielmendieta/">Angel Daniel Menideta Castillo</a> © 2024