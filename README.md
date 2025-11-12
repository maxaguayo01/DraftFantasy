# 🏈 Análisis de Fantasy NFL: Optimizador de Lineup (Fase EDA)

## 💡 Introducción al Proyecto

Este repositorio alberga un proyecto de análisis de datos con el objetivo final de desarrollar un **algoritmo de optimización** para la formación de **starting lineups** de Fantasy Football de la NFL.

Actualmente, el proyecto se encuentra en la **Fase 1: Análisis Exploratorio de Datos (EDA)**, donde se extraen, limpian y visualizan las métricas de los jugadores obtenidas de **FantasyPros** y otras fuentes (asumido) para entender la distribución y el valor de los Fantasy Points (FPTS) por posición.

### 🎯 Objetivo Final

El objetivo final del algoritmo es tomar un roster de Fantasy y, basándose en las proyecciones semanales, sugerir la alineación que maximice la puntuación proyectada, ayudando al usuario a tomar las mejores decisiones de **Start/Sit**.

---

## 🛠️ Tecnología Utilizada

| Componente | Tecnología/Herramienta | Uso Específico en la Fase EDA |
| :--- | :--- | :--- |
| **Lenguaje Principal** | **Python 3.x** | Core del análisis de datos. |
| **Ambiente** | **Jupyter Notebook** | Documentación y ejecución interactiva del análisis (`01_eda_inicial.ipynb`). |
| **Manejo de Datos** | `Pandas` | Extracción, limpieza y estructuración del dataset de jugadores (conteo por posición, cálculos de promedios). |
| **Visualización** | `Matplotlib` / `Seaborn` (Asumido) | Generación de gráficos detallados por posición (QB, RB, WR, etc.). |

---

## 📂 Contenido del Repositorio

### `01_eda_inicial.ipynb`

Este es el notebook central de la fase actual. El script realiza las siguientes acciones clave:

1.  **Carga y Limpieza de Datos:** Carga el conjunto de datos de jugadores y realiza una primera limpieza.
2.  **Distribución de Datos:** Muestra el número total de jugadores y la distribución por posición (`WR`, `RB`, `QB`, `TE`, `K`, `DST`).
3.  **Análisis de FPTS:** Calcula y muestra el **Promedio de Fantasy Points (FPTS)** y la **Desviación Estándar ($\sigma$)** de los jugadores por posición.
4.  **Generación de Visualizaciones:** Crea y guarda una serie de gráficos para un análisis más profundo:

| Archivo Generado | Descripción |
| :--- | :--- |
| `EDA_QB.png` | Análisis de Quarterbacks |
| `EDA_RB.png` | Análisis de Running Backs |
| `EDA_WR.png` | Análisis de Wide Receivers |
| `EDA_TE.png` | Análisis de Tight Ends |
| `EDA_Kickers.png` | Análisis de Kickers |
| `EDA_DST.png` | Análisis de Defensas y Equipos Especiales |
| `EDA_Comparativo.png` | Comparación de métricas clave entre todas las posiciones. |

---

## 📜 Licencia

Diego Canales Morales
David Gutierrez Castro
Maximiliano Aguayo Villanueva
Jose Luis Almendarez Gonzalez