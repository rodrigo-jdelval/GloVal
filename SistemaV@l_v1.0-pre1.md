**Sistema GloV@l**  
Subsistema Individuo  
**Método del Hecho-Equilibrado**  
Domingo del Val Perdiguero & Rodrigo Jiménez del Val  
V1.0 pre1 / 
Enero del 2010

Análisis e Implementación de una  
Herramienta Individual de Análisis del Hecho-Equilibrado  
**(HidAdHE)**

**RESUMEN**

Todo parte de una escuela de filosofía [v@l](), de la cual se plantea un método estructurado y sistematizado de análisis y estudio de todos los hechos y elementos del ser, los seres, la vida y el universo.

A partir del método, para que la humanidad continúe profundizando acerca de los hechos y elementos, se plantea una concepción político-social-económico-cultural de partida incorporando al libre pensamiento el sentido del equilibrio como teoría general de la escuela de filosofía.

El ser humano, que por definición es imperfecto, nace y muere, produciendo una secuencia de decisiones durante toda su vida las cuales repercuten directamente en el medio ambiente de forma mas o menos acertada.

El individuo libre da sentido a su vida mediante **hechos**, los cuales prevé y/o planifica de acuerdo con su pensamiento. La ejecución de estos hechos implica cambios en el estado del medio. Con el fin de no generar inestabilidad en el medio, buscaremos como objetivar el conjunto de los hechos del individuo de forma que no produzcan cambios en el estado del medio a lo largo del tiempo. A esta situación armónica la denominaremos **equilibrio**. Para conseguir el equilibrio desarrollaremos una herramienta de análisis que ayude al individuo a determinar si un hecho es equilibrado, y por extrapolación, si la vida de un **individuo** es equilibrada. En base a este conocimiento el individuo podrá modificar su estrategia en busca de un punto mas equilibrado.

1 Introducción 5  
1.1 Motivación 5  
1.2 Objetivos 5  
1.3 Planing 6  
1.4 Puntos críticos 6  
2 Contexto 7  
2.1 Declaración Universal 7  
2.2 Principios Universales 7  
2.3 Teoría General (Social) 7  
2.4 Normas Universales-Derecho-Ética 7  
3 Análisis del Individuo 11  
3.1 Visión general 11  
3.2 Metodología 12  
3.3 Requerimientos del Subsistema Individuo 13  
3.4 Modelado del Subsistema Individuo 14  
3.4.1 Modelo de datos 14  
3.4.2 Modelo de procesos 17  
3.4.3 Arquitectura 18  
3.5 Protocolos de comunicación 20  
3.6 Métodos del Individuo 21  
3.6.1 Metodos generales 21  
3.6.2 Métodos específicos 21  
4 Agrupaciones de Individuo 23  
4.1 Grupos del Sistema GloV@l 23  
4.1.1 Escuela de el libre pensamiento 23  
4.1.2 Grupo Social Global 23  
4.1.3 Grupo Economico 23  
4.1.4 Club de Ocio y Tiempo Libre 23  
4.1.5 Medio Ambiente 23  
5 Diccionario 24  
6 Fuentes 25

# 

# **1 Introducción**

## **1.1 Motivación**

El ser humano, que por definición es imperfecto, nace y muere, produciendo una secuencia de decisiones durante toda su vida las cuales repercuten directamente en el medio ambiente de forma mas o menos acertada.

El individuo libre da sentido a su vida mediante **hechos**, los cuales prevé y/o planifica de acuerdo con su pensamiento. La ejecución de estos hechos implica cambios en el estado del medio. Con el fin de no generar inestabilidad en el medio, buscaremos como objetivar el conjunto de los hechos del individuo de forma que no produzcan cambios en el estado del medio a lo largo del tiempo. A esta situación, estacionariamente deseable, la denominaremos **equilibrio**. Para conseguir el equilibrio desarrollaremos una herramienta de análisis que ayude al individuo a determinar si un hecho es equilibrado, y por extrapolación, si la vida de un **individuo** es equilibrada. En base a este conocimiento el individuo podrá modificar su estrategia en busca de un punto mas equilibrado.

Se deja para el lector la reflexión de si el equilibrio conduce a la felicidad o la armonía, así como la trascendencia de la misma en nuestra vida.

**1.2 Objetivos**

El objetivo es crear una Herramienta de Análisis del hecho-equilibrado del individuo. Para ello analizaremos en el tema 3 como caracterizar los individuos y sus interfaces con el medio. En base a esta caracterización propondremos un modelado de datos y procesos para concretar una arquitectura del sistema.

En el tema 3 definiremoes una aplicación basada en el sistema que nos ayude a conseguir un individuo libre en equilibrio-felicidad, armonía y respeto al medio natural y sus semejantes mediante el análisis del equilibrio del hecho: la “Herramienta Individual de Análisis del Hecho-Equilibrado” (HIdAdHE).

Se podrían crear mas aplicaciones del sistema como simulaciones de como evolucionarian agrupaciones de individuos en un medio concreto o juegos virtuales, pero nos centraremos en el HidAdHE.

## **1.3 Planing**

Entendemos que sin una aproximación multidisciplinar el sistema carece de sentido, de forma que se pretende analizar desde diferentes puntos de vista el mismo problema. Básicamente, cabe destacar que este primer documento teórico no tiene sentido si el sistema carece de experiencias prácticas en un futuro cercano.

Tareas:

* Escribir el Diccionario-vocabulario-concepto del documento (Cap. 5\)  
* Escribir la Estructura del Sistema (basada en los diccionarios wikipedia, UNESCO (antropológico-social), clasificación decimal universal de archivos y bibliotecas)  
* Descripción de Métodos, aplicaciones, programas, planes.  
* Descripción de Formatos (XML, Braille, esperanto, dimensión documentos, 16:9 TV/hojas,....)

**1.4 Puntos críticos**

Con el fin de que el sistema evolucione simplemente nos proponemos que en todo momento haya por lo menos un hito con respecto al diseño o implementación del sistema.

Conviene dividir la evolución del sistema en fases, tareas e hitos asociados a individuos al estilo Diagrama de Gantt, con el fin de poder llevar a cabo un seguimiento de la evolución que nos reporte las desviaciones y nos permita analizar los riesgos.  
**2 Contexto**

Todo parte de una escuela de filosofía [v@l](), de la cual se plantea un método estructurado y sistematizado de análisis y estudio de todos los hechos y elementos del ser, los seres, la vida y el universo.

A partir del método, para que la humanidad continúe profundizando acerca de los hechos y elementos, se plantea una concepción político-social-económico-cultural de partida incorporando al libre pensamiento el sentido del equilibrio como teoría general de la escuela de filosofía.

## **2.1 Declaración Universal**

La sociedad en su conjunto produce grandes desequilibrios naturales y humanos. Los estados y los entes actualmente no han tenido capacidad de concebir y aplicar un sistema y políticas que consigan el equilibrio-felicidad para toda la humanidad con el respeto a su medio natural.

## **2.2 Principios Universales**

La articulación de la sociedad se debe dar bajo premisas de:

* Participación  
* Equilibrio y Justicia  
* Solidaridad  
* Igualdad  
* Respeto

## **2.3 Teoría General (Social)**

El orden de la humanidad se articula bajo el principio de equilibrio e igualdad entre el medio y los seres humanos en los campos ambientales, económico, social y cultural.

**2.4 Normas Universales-Derecho-Ética**

La sociedad en su conjunto produce grandes desequilibrios naturales y humanos. Los estados y los entes actualmente no han tenido capacidad de concebir y aplicar un sistema que consiga el equilibrio-felicidad para toda la humanidad con el respeto a su medio natural.

Los cambios en la estrategia social llevados en los últimos siglos han sido inadecuados y vanos. Pobreza, nuevas enfermedades, conflictos étnicos, emigración, brecha social, cambio climático, terrorismo, urbanización: desequilibrios cada vez mas acuciantes y que directa o indirectamente nos influyen a todos.

¿Se puede vivir en una sociedad que se encuentre totalmente desequilibrada?

# **3 Análisis del Individuo**

## **3.1 Visión general**

Una vez visto el contexto y la problemática abordaremos el problema desde el punto de vista mas objetivo posible, definiendo un sistema abierto sin una herencia anterior que nos permita centrarnos en conceptos facilmente objetivables y extrapolables.

Basicamente, el individuo libre da sentido a su vida produciendo equilibrio-felicidad-creatividad mediante sus hechos. El individuo libre prevé el hecho de acuerdo con su ética y pensamiento, y de esta forma puede evitar que los hechos que produzca desequilibren el medio o a si mismo. El individuo libre planifica los hechos con el fin de que otros agentes no determinen su conducta y acaben produciendo desequilibrios en el medio o en si mismo.

Conviene enfatizar que la “Herramienta Individual de Análisis del Hecho-Equilibrado” (HIdAdHE) se basa en que toda relación de los individuos entre si y con el medio se realicen equilibradamente.

El **Sistema GloV@l** comprende el medio ambiente. Se entiende por **ambiente** el entorno o suma total de aquello que nos rodea y que afecta y condiciona especialmente las circunstancias de vida de las personas o la sociedad en su conjunto. Comprende el conjunto de valores naturales, sociales y culturales existentes en un lugar y un momento determinado, que influyen en la vida del hombre y en las generaciones venideras. Es decir, no se trata sólo del espacio en el que se desarrolla la vida sino que también abarca seres vivos, objetos, agua, suelo, aire y las relaciones entre ellos, así como elementos tan intangibles como la cultura. Ambiente solo hay uno y comprende toda la energía existente.

Cada una de las unidades elementales del sistema las denominamos subsistema. Nos centraremos en el subsistema al que nosotros pertenecemos: el subsistema Individuo. Los individuos son un ámbito energético parte del ambiente, con múltiples, variadas e irrepetibles instanciaciones. Existen otros subsistemas parte del ambiente que también tienen al igual que el Individuo como estrategia que no se disperse su energía (entropía), pero no entraremos en ellos puesto que se sale del alcance de la herramienta de Análisis del Hecho-Equilibrado. Además, se da el caso que hay multiples individuos conviviendo y compartiendo el mismo ambiente. Los posibles intercambios energéticos (relaciones) que nos incumben para realizar el método del hecho-equilibrado son individuo-ambiente y por inclusión individuo-individuo, con las premisas del espacio-tiempo.

Obviaremos las premisas espacio-tiempo por la complejidad que conllevan los modelos asociados. Es evidente que un individuo no puede estar a la vez en dos sitios, pero modelarlo también esta fuera del alcance.

## **3.2 Metodología**

El requerimiento principal es que mediante una caracterización del individuo incluido en el ambiente, seamos capaces de analizar si un hecho es equilibrado. Para ello, de una forma metodológica, se definirá un sistema agregado organizado y autocontenido: El Sistema GloV@l. Dado el alcande del documento, nos centraremos en la caracterización del subsistema Individuo y sus interfaces.

Con el fin de ser autocontenido el sistema dispondrá de un diccionario que definirá los terminos del mismo.

El método de objetivación del hecho-equilibrado será el método científico.

Cualquier individuo, de forma libre, podrá experimentar con el sistema ya sea un empresario de New York, una madre de familia de Bangladesh o un niño de Ruanda, independientemente de su origen, raza, credo o estatus social.

El individuo no quedará restringido a la naturaleza animal o natural, sino que también puede ser un individuo “artificial” implantable mediante un modelo computacional (Inteligencia Artificial, Sistemas Expertos, etc…).

Se adopta la licencia GPLv2 para el presente documento, permitiendose la copia, modificación y redistribución del mismo.

Como resumen de metodología general del sistema que nos permita realizar una herramienta de Análisis del Hecho-Equilibrado tenemos:

* Agregado y organizado.  
* Autocontenido mediante el diccionario del sistema.  
* Capaz de análizar de forma objetiva el hecho-equilibrado.  
* Objetivación mediante método científico.  
* De alcance integral y universal.  
* Implantable mediante modelo computacional.  
* Licencia GPLv2.


Integral es el todo entendiendo como todo materia y elemento que forma parte de la vida. Universal es la característica que se aplica sobre el todo.

Cabe destacar que el sistema no pretende ser un ningún método de adoctrinaje, ni substituir cualquier otra forma de pensamiento sobre la vida o la sociedad, sinó experimentar acerca de la búsqueda de la felicidad global. Tampoco se pretende hacer ninguna revolución que aplaste ningún sistema, pero si experimentar una evolución del individuo libre al equilibrio-felicidad.

## **3.3 Requerimientos del Subsistema Individuo**

Una vez vista la metodología, analizaremos los requerimientos del subsistema Individuo para caracterizarlo de forma genérica con su interfaz: el ambiente. Esta es una tarea totalmente creativa y está basada en un proceso de constante evolución. Nos basaremos en la identificación de los datos, procesos e interfaces del individuo dentro del ambiente para obtener un modelado.

La siguiente tabla presenta un resumen de los requerimientos del subsistema e interfaces:

| Subsistema | Tipo | Requerimientos |
| :---- | :---- | :---- |
| Ambiente | Dato | Eventos del Ambiente |
| Individuo | Interfaz | Sistema Nervioso de Entrada |
|  | Dato | Configuración Inicial |
|  | Proceso | Gestor Central de Conocimiento |
|  | Proceso | Métodos |
|  | Proceso | Formateador |
|  | Interfaz | Sistema Nervioso de Salida |

En lo que se refiere al ambiente, tan solo mencionaremos los datos que caracterizamos como Eventos del Ambiente, los cuales se comunican con el interfaz de entrada del individuo: El Sistema Nerviosos de Entrada.

El **Sistema Nerviosos de Entrada** son los interfaces que permiten al subsistema Individuo, a través de los sentidos, recibir, interpretar y elaborar la información proveniente de su ambiente, entorno o medio.

La **Configuración Inicial** debe ser introducida al sistema para conocer las normas básicas de funcionamiento. Originalmente contiene una estrategia básica de supervivencia y un manual de como aprender. Posteriormente se añade una ética.

El **Gestor Central de Conocimiento** (GcC) es elemento destinado a coordinar y armonizar los hechos.

Los **Métodos** son mecanismos de mejora del conocimiento mediante herramientas predefinidas que ayudan al Gestor Central de Conocimiento a tomar decisiones. Por ejemplo pueden agregar o correlar la información.

El **Formateador** de información procesa la información en términos de representación con el fin de que sean asimilados / entendidos por el Gestor Central de Conocimiento. Posibles formatos podrían ser un libro escrito en castellano, el Braille, cualquier lenguaje hablado o el HTML.

El **Sistema Nerviosos de Salida** son los interfaces que permiten al sistema la activación de los mecanismos de los músculos que pueden causar un movimiento o realizar un pensamiento interno.

Información (lectura de hechos por GdC ?) vs Conocimiento (dentro GdC?)

## **3.4 Modelado del Subsistema Individuo**

En el siguiente apartado identificaremos el modelo de datos y procesos así como la arquitectura del subsistema Individuo y sus intefaces.

### **3.4.1 Modelo de datos**

El modelo de datos define la forma como guardamos y recuperamos la información. Definiremos un modelo de datos abierto basado en entidades-relación con el fin de asegurar la integridad y simplificar los procesos.

Diferenciamos tres dominios de información: Hechos, Configuración y Enciclopedia. Dentro del dominio de los Hechos tenemos la entidad HECHO. Dentro del dominio Configuración tenemos las entidades INICIAL, ESTRATEGIA, ETICA. Dentro del dominio Enciclopedia tenemos las entidades DICCIONARIO, OBSERVATORIO, ESTADISTICA y CIENCIAS. El dominio enciclopedia puede tener entidades nuevas.

| Dominio | Nombre de Entidad | Descripción |
| :---- | :---- | :---- |
| Hechos | HECHO | Caracteriza eventos del medio |
| Configuración | INICIAL |  |
|  | ESTRATEGIA | Plan de acción para logro de metas |
|  | ETICA | Conducta o moral vivida |
| Enciclopedia | DICCIONARIO | Definición de términos |
|  | OBSERVATORIO |  |
|  | ESTADÍSTICA |  |
|  | CIENCIAS,… |  |

El dominio **Hechos** está formado por la entidad **HECHO,** que contiene la información que caracteriza los sucesos percibidos del ambiente. Esta información es introducida por el interfaz de entrada al sistema (Sistema Nervioso de Entrada) de forma totalmente automática y objetiva. No se permite la modificación ni eliminación de registros de la entidad; solo la inserción.

La función principal de la entidad HECHO es aportar conocimiento al GcC y también aportar información a los Métodos. El GcC tiene total disponibilidad de consulta sobre ella.

Hay dos tipos de hechos: internos y externos. Internos son los hechos relacionados con la configuración. Externos son los que ejecutamos o percibimos del ambiente.

El dominio **Configuración** se diferencia del de los Hechos en que la información puede ser inserida, modificada, borrada o consultada. Se modificará con la temporalidad y contenidos que determine el GcC. Su función principal es aportar conocimiento al GcC.

La entidad **INICIAL** contiene la información aportada por los individuos ascendentes (fenotipo y genoma) y por el ambiente inicial.

La entidad **ESTRATEGIA** contiene la información que permite al subsistema Individuo avanzar el en tiempo mediante una hoja de ruta que se lleva a cabo para lograr un determinado fin a largo plazo. Determina cuando y como realizar hechos para la consecución del fin deseado en formatos de idea o plan descrito.

La estrategia de supervivencia está precargada en el origen en todos los Individuos.

La entidad **ETICA** contiene la información suficiente para que el subsistema Individuo pueda elaborar, ejecutar y verificar afirmaciones o juicios. Esta sentencia ética, juicio moral o declaración normativa es una afirmación que contendrá términos tales como 'malo', 'bueno', 'correcto', 'incorrecto', 'obligatorio', 'permitido', etc, referido a un hecho.

El GcC dispone del Método de la Ética (ver apartado 3.6.7) para modificar la entidad ETICA estudiando qué es lo bueno y, desde este punto de vista, cómo se debe actuar. El Método de la Ética tiene los principios del equilibrio y el respeto.

Hecho equilibrado se define como una acción natural o artificial que se atiene a un conocimiento científico-técnico. Este equilibrio se fundamenta en el sentido (que haces, a donde vas,...) y el tiempo (cuando lo haces, cuanto tiempo te vas,...) buscando la armonía-equilibrio con el ambiente, entendiendo como medio el todo.

El dominio **Enciclopedia** permite que la información pueda ser inserida, modificada, borrada o consultada. Dispone de un número variable de entidades asociadas a fuentes de conocimiento que son modificadas con la temporalidad y contenidos que determine el método. Cada entidad de la Enciclopedia tiene un método asociado. Su función principal es aportar conocimiento al GcC. A modo de ejemplo se enumeran las siguientes entidades:

* DICCIONARIO  
* OBSERVATORIO  
* ESTADISTICA  
* ESTRUCTURA\_CULTURAL\_ANTROPOLOGICA  
* ESTRUCTURA\_ECONOMICO\_CONTABLE  
* Ciencias (LINGUISTICA, DERECHO, … )  
* HISTORIA  
* NORMAS ISO

La entidad **DICCIONARIO** contiene la información del nombre y descripción de forma enumerada de todos los hechos y elementos con una sola acepción. Es modificable por el GcC e integra todos los niveles de la estructura lingüística no gramatical.

Como ejemplos de diccionarios que pueden ser incluidos en el sistema se enumeran:  
• ISO  
• Diccionario del derecho

• Diccionario científico técnico

El diccionario de la real academia española no puede ser incluido dentro del sistema dado que hay palabras con varias acepciones, como por ejemplo banco (para sentarse y para robar dinero).

El sistema dispone de una estructura cultural-social-antropológica-estadística-observatorio integrada para la ordenación y sistematización de todas los métodos, elementos y hechos. Por ejemplo en la “Guia para la clasificación de los datos culturales” (Universidad Autónoma Metropolitana – Iztapalapa \- México 1989\) define la clasificación de Geografía como:

13 GEOGRAFÍA  
131 Localización  
132 Clima  
133 Topografía  
134 Suelos  
135 Recursos Minerales  
136 Fauna

137 Flora

La entidad **OBSERVATORIO** contiene la información de Hechos y/o elementos no agregados que aporta conocimiento numérico-temporal al GdC. El Método del Observatorio (ver apartado 3.6.7) modifica la entidad OBSERVATORIO contabilizando en todo momento.

La entidad **ESTADISTICA** contiene la información de Hechos y/o elementos agregados que aporta conocimiento numérico-temporal al GcC. El Método Estadístico (ver apartado 3.6.7) modifica la entidad ESTADISTICA agregando en todo momento.

### **3.4.2 Modelo de procesos**

El modelo de procesos que define el subsistema Individuo se realiza teniendo en cuenta los parámetros de entrada y de salida previamente descritos.

Los procesos que definen los requerimientos del sistema son el GESTOR CENTRAL DE CONOCIMIENTO, los METODOS y el FORMATEADOR.

| Proceso | Entradas | Salidas |
| :---- | ----- | :---- |
| GESTOR CENTRAL DE CONOCIMIENTO | FORMATO HECHO CONFIGURACIÓN ENCICLOPEDIA | HECHO CONFIGURACIÓN ENCICLOPEDIA SISTEMA NERVIOSO SALIDA |
| METODOS | HECHO CONFIGURACIÓN ENCICLOPEDIA | FORMATO |
| FORMATEADOR | METODO | GESTOR CENTRAL DE CONOCIMIENTO |

El **Gestor Central de Conocimiento** (GcC) es la Unidad central de proceso (CPU) natural / artificial que dispone de conexiones / interfaces de entrada y salida de conocimiento para marcar la estrategia del hecho.

La entrada de conocimientos puede ser de los Métodos (previamente formateados) o de cualquier repositorio (Hechos, Configuración y Enciclopedia). La salida aportada por el GdC siempre será un Hecho ( interno en algún repositorio o externo mediante el Sistema Nervioso de Salida, el cual reportará el nuevo hecho), quedando posteriormente registrado en la base de datos de Hechos). HACER UN DIAGRAMA DE FLUJO\!\!\!

Los conocimientos son operativos en su integridad y son procesados de acuerdo con la configuración, concluyendo como respuesta en un hecho que se encamina en base a la **estrategia** del hecho.

Los **METODOS** son ordenación / determinación y caracterización de secuencias de instrucciones que aportan conocimiento de cómo ejecutar acciones (educativas, proyectos, planes,...). Los métodos utilizan un determinado formato para aportar conocimientos al GcC. Estos métodos son aplicaciones mediante las cuales el individuo, libremente, opta por hacer uso de los  
mismos total o parcialmente. La función de los métodos es establecer forma y orden de ejecución de hechos y/o operaciones que ayuden al GcC a conseguir un plan.

El **FORMATO** es la caracterización de la representación de los conocimientos. Con el fin de que el GcC interprete un formato, previamente ha de ser precargado el conocimiento del mismo en la Configuración del subsistema Individuo. La función del formato es unificar la representación de conocimientos para  
ser procesados por el GcC.

### **3.4.3Arquitectura**

Una vez definidos el modelo de datos y procesos hay que unir datos y procesos para que funcione tal como deseamos mediante una arquitectura, que está formada por entidades.

A continuación se enumeran todas las entidades del subsistema Individuo.

* Interfaz de Entrada  
* Gestor Central de Conocimiento (GcC)  
* Métodos  
* Formateador  
* Repositorio de Hechos  
* Repositorio de Configuración  
* Repositorio de la Enciclopedia  
* Interfaz de Salida

El siguiente gráfico muestra la arquitectura del sistema V@l con sus entidades y relaciones:

![][image1]

El funcionamiento es el siguiente:

Inicialmente se carga la Base de Datos de Configuración. A partir de este momento se dota al Gestor Central de Conocimientos (GcC) de un conocimiento inicial de ética, estrategia, diccionario y una enciclopedia. Mediante la percepción del medio nutrimos la Base de Datos de Hechos. Por otro lado, disponemos de Métodos, que una vez Formateados aportan conocimientos para el GcC. El GcC en base a los conocimientos actualiza su configuración buscando optimizar la estrategia del hecho.

La Estrategia del Hecho es el procesamiento de toda la información disponible por parte del GcC con el objetivo de generar un hecho.

La emoción se divide en 3 fases:

* 1\. Entrada: Percepción interna (lectura de configuración) o externa (lectura de hecho)  
* 2\. Procesado  
* 3\. Salida: Hecho interno ( Cambio de la configuración) o Hecho externo y registro.

## **3.5 Protocolos de comunicación**

Con el fin de que se puedan realizar comunicaciones a distancia entre subsistemas, se definen cuatro niveles. Cada nivel tiene sus funciones propias y protocolos. Una capa solo tiene interfaces con las capas adyacentes. Cada uno contiene la información de los niveles anteriores mediante la agregación de unidades mínimas del nivel anterior, pero realzada. El nivel 1 define los hechos físicos asociados a la realidad objetiva. En nivel 4 define aplicaciones basadas en el conocimiento que solo tienen sentido en el estado de conciencia.

Los niveles definidos por GloV@l son:

* Nivel 1: Física (hechos) \- realidad  
* Nivel 2: Transporte (eventos)  
* Nivel 3: Presentación (información)  
* Nivel 4: Aplicación: (conocimiento) \- conciencia

**3.6 Métodos del Individuo**

Se definen métodos generales y específicos para el Individuo.

### **3.6.1 Metodos generales**

Se definen de forma genérica los siguientes métodos:

* Método de la Ética  
* Método de la Estrategia  
* Método del Hecho  
* Método del Día  
* Método del Trabajo  
* Método del Ocio y Tiempo Libre

#### **3.6.1.1 Método de la Ética**

El GcC dispone del Método de la Ética para modificar la entidad ETICA estudiando qué es lo bueno y, desde este punto de vista, cómo se debe actuar. El Método de la Ética tiene los principios del **equilibrio** y el **respeto**.

#### **3.6.1.2 Método de la estrategia**

El GcC dispone del Método de la Estrategia para modificar la entidad ESTRATEGIA diseñando el plan de acción del Individuo para el logro de su metas y objetivos. Concretamente incluye datos de orden, temporalidad y localización de los elementos y los hechos para la consecución del fin. El Método de la Estrategia tiene los principios del **equilibrio** y el **respeto**.

#### **3.6.1.3 Método del Hecho**

El GcC dispone del Método del Hecho para procesar toda la información disponible en los repositorios del Individuo para al final ejecutar un hecho sistematizando la acción buscando siempre la eficiencia.

La ejecución del método del hecho tiene como trigger otro hecho.

### **3.6.2 Métodos específicos**

Los métodos específicos están relacionados con las diferentes profesiones existentes.

**4 Agrupaciones de Individuo**

## **4.1 Grupos del Sistema [GloV@l]()**

### **4.1.1 Escuela de el libre pensamiento**

La Escuela del Libre Pensamiento es el conjunto de personas que piensan bajo una estructura común de filosofía y antropología de la vida.

### **4.1.2 Grupo Social Global**

El Grupo Social Global es un conjunto de Individuos que estarán presentes en todos los territorios participando de forma activa en las funciones propias de decisión y de acuerdo con los valores, principios y código ético del Grupo.

### **4.1.3 Grupo Economico**

El Grupo Económico es el conjunto de Individuos o agrupaciones de Individuos que prestan el conjunto de bienes y servicios a la comunidad bajo los principios y valores del Grupo que son el equilibrio económico y natural.

### **4.1.4 Club de Ocio y Tiempo Libre**

El Club de Ocio y Tiempo Libre es el conjunto de Individuos o agrupaciones de Individuos que bajo los principios y valores del Grupo realizan actividades conjuntas (en red) o individual de forma libre.

### **4.1.5 Medio Ambiente**

El Medio Ambiente es agrupación de Individuos del Grupo [GloV@l]() que analizan el ecosistema en su conjunto y determinan si el hecho realizado se adecua a la teoría del equilibrio del Sistema.

# **5 Diccionario**

TODO

# **6 Fuentes**

\[1\] El origen de las especies. Charles Darwin. 1859\.

\[2\] El “Shock” del futuro. Alvin Toffler. 1970\.

\[3\] Programa de Gestión de las Transformaciones Sociales (MOST) de la UNESCO.

\[4\] Ética [http://es.wikipedia.org/wiki/Ética](http://es.wikipedia.org/wiki/Ética)

\[5\] Lingüística [http://es.wikipedia.org/wiki/Lingüística](http://es.wikipedia.org/wiki/Lingüística)

\[6\] Estrategia [http://es.wikipedia.org/wiki/Estrategia](http://es.wikipedia.org/wiki/Estrategia)

\[7\] Conciencia  [http://es.wikipedia.org/wiki/Conciencia](http://es.wikipedia.org/wiki/Conciencia)  


[image1]: <data:image/png;base64,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>