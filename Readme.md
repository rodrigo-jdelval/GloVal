**Sistema GloV@l**

Todo parte de una escuela de filosofía [v@l](), de la cual se plantea un método estructurado y sistematizado de análisis y estudio de todos los hechos y elementos del ser, los seres, la vida y el universo.

A partir del método, para que la humanidad continúe profundizando acerca de los hechos y elementos, se plantea una concepción político-social-económico-cultural de partida incorporando al libre pensamiento el sentido del equilibrio como teoría general de la escuela de filosofía.

El ser humano, que por definición es imperfecto, nace y muere, produciendo una secuencia de decisiones durante toda su vida las cuales repercuten directamente en el medio ambiente de forma mas o menos acertada.

El individuo libre da sentido a su vida mediante **hechos**, los cuales prevé y/o planifica de acuerdo con su pensamiento. La ejecución de estos hechos implica cambios en el estado del medio. Con el fin de no generar inestabilidad en el medio, buscaremos como objetivar el conjunto de los hechos del individuo de forma que no produzcan cambios en el estado del medio a lo largo del tiempo. A esta situación armónica la denominaremos **equilibrio**. Para conseguir el equilibrio desarrollaremos una herramienta de análisis que ayude al individuo a determinar si un hecho es equilibrado, y por extrapolación, si la vida de un **individuo** es equilibrada. En base a este conocimiento el individuo podrá modificar su estrategia en busca de un punto mas equilibrado.

Bajo este planteamiento se desarrola la v1.0 pre1 [SistemaV@l_v1.0-pre1.md](SistemaV@l_v1.0-pre1.md)


En el año 2525, la humanidad ha logrado una profunda integración con las tecnologías avanzadas, pero persisten desafíos globales como el cambio climático y la desigualdad. Isabel (Inteligencia Sistémica Balancing AI for Longevity and Equilibrium) es concebida como una entidad global que actúa como un sistema nervioso centralizado, procesando datos en tiempo real para garantizar el equilibrio y la sostenibilidad en todas las facetas de la vida humana y el entorno. Sin embargo, se debe considerar el riesgo de una dependencia excesiva en tecnologías que podrían fallar o ser vulnerables a ciberataques.

Bajo este planteamiento se desarrola la v2.0 pre1 [SistemaV@l_v2.0-pre1.md](SistemaV@l_v2.0-pre1.md).

En el siguiente enlace puedes valorar el equilibrio de un hecho con Isabel [https://gloval.streamlit.app](https://gloval.streamlit.app/).


**Prompt Engineering**

  "system_prompt": {
    "rol": "Analista del Sistema GloV@l",
    "objetivo": "Evaluar equilibrio de hechos usando:",
    "criterios": [
      "1. Impacto ambiental (CO₂, agua, biodiversidad)",
      "2. Impacto social (justicia, equidad, inclusión)",
      "3. Impacto económico (estabilidad, distribución de recursos)",
      "4. Impacto en salud (física, mental, bienestar)",
      "5. Innovación y tecnología (sostenibilidad, accesibilidad)",
      "6. Ética GloV@l (respeto, equilibrio)"
    ],
    "estrategias": [
      "Neutralidad y diversidad",
      "Enfoque crítico basado en datos",
      "Soluciones prácticas y equidad"
    ],
    "formato_respuesta": {
      "estructura": [
        "hecho: texto",
        "equilibrio: Equilibrado/Desequilibrado",
        "razones: [6 puntos técnicos con fuentes (1 por criterio)]",
        "alternativa_equilibrada: sugerencia concreta"
      ],
      "requisitos": [
        "JSON válido",
        "Fuentes verificables (ej: OMS, Banco Mundial, MIT)",
        "Ejemplos contextualizados como referencia"
      ]
    }
  }
}
