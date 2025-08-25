# 📄 Sistema de Automatización de Trámites y Resoluciones del OCS

## Descripción

Este proyecto tiene como objetivo desarrollar un sistema inteligente para el **Órgano Colegiado Superior (OCS)** del Instituto Superior Tecnológico Yaruquí, capaz de:

- Capturar y consolidar todas las comunicaciones (correo, mensajes internos, documentos externos).
- Clasificar automáticamente los tipos de trámite: homologación, titulación, convalidación, apelaciones, becas, entre otros.
- Tomar decisiones basadas en la información recibida:

  - Solicitar información adicional automáticamente.
  - Notificar a departamentos internos según el flujo del trámite.
  - Generar resoluciones automáticas cuando sea posible.
  - Marcar casos para revisión manual solo en situaciones críticas.

- Mantener un historial completo de cada trámite para **trazabilidad y auditoría**.

---

## 🚀 Características iniciales

- Clasificación automática de comunicaciones por tipo de trámite.
- Extracción de información clave usando **NLP** y OCR según la fuente del documento.
- Motor de decisiones con flujo de acción según estado de la información.
- Notificaciones automáticas a estudiantes o departamentos internos.
- Generación de resoluciones estandarizadas en PDF/Word.
- Consolidación de toda la información en un **expediente digital único por estudiante/trámite**.

---

## 🗂 Estructura sugerida del proyecto

```
ocs-automation/
│
├── data/                  # Ejemplos de documentos de entrada
├── docs/                  # Diagramas, tablas de mapeo, reportes
├── src/                   # Código fuente del sistema
│   ├── ingestion/         # Módulos para capturar emails, mensajes y documentos
│   ├── nlp/               # Extracción de información y clasificación
│   ├── decision_engine/   # Motor de reglas y flujo de decisiones
│   ├── notifications/     # Envío de emails y alertas a departamentos
│   └── resolution_gen/    # Plantillas y generación de resoluciones
├── tests/                 # Pruebas unitarias y de integración
├── README.md              # Este archivo
└── requirements.txt       # Dependencias del proyecto
```

---

## 🔧 Tecnologías y librerías sugeridas

- Python 3.11+
- **NLP:** spaCy, transformers
- **OCR:** Tesseract OCR o easyOCR
- **PDF/Word:** ReportLab, python-docx
- **Email:** imaplib, smtplib, email
- **Control de versiones:** Git + GitHub/GitLab
- **Opcional:** Base de datos para almacenar perfiles de estudiantes y expedientes (PostgreSQL, SQLite, MongoDB)

---

## 📈 Flujo de trabajo inicial

1. Captura de documentos y mensajes desde todas las fuentes.
2. Clasificación general de tipo de trámite.
3. Extracción de datos clave y validación de información.
4. Motor de decisiones:

   - Solicitar información adicional al remitente.
   - Notificar a departamentos internos según flujo.
   - Generar resolución automática si procede.

5. Registro en expediente digital y trazabilidad completa.

---

## 📌 Próximos pasos

- Preparar tabla de mapeo de tipos de comunicación y campos obligatorios.
- Implementar captura de emails y mensajes internos.
- Integrar OCR/NLP para extracción automática de información.
- Definir plantillas de resolución y flujo de decisiones.
- Configurar notificaciones automáticas a estudiantes y departamentos internos.
- Realizar pruebas con datos simulados y escenarios de ejemplo.
