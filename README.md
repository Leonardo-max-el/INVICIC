# 🧾 Sistema de Digitalización de Inventarios - Continental

Este proyecto está orientado a digitalizar y optimizar la gestión de inventarios para la organización **Instituto Continental**. Desarrollado con **Python**, el framework **Django** y **MySQL** como base de datos, incorpora herramientas para la carga masiva de datos, generación automática de documentos y control detallado de activos.

---

## 🚀 Funcionalidades principales

- 📥 **Carga de datos desde Excel**: Permite importar información de usuarios y activos desde archivos `.xls`, utilizando las librerías `openpyxl` y `pandas`.
- 🔍 **Filtrado avanzado**: Posibilita buscar activos por usuario, estado de entrega o uso.
- 📝 **Generación automática de actas de entrega**: Crea documentos Word con la información del usuario y los activos asignados, gracias a `python-docx`.
- 🗂 **Historial de entregas**: Las actas generadas se almacenan dentro del sistema como registro histórico.
- 🔁 **Gestión de devoluciones**: Permite registrar la devolución de activos, incluyendo la fecha de retorno.
- 🟢🟡🔴 **Control de estados de activos**: Los activos pueden estar en uno de tres estados: `ACTIVO`, `ASIGNADO` o `DE BAJA`.
- ⚙️ **Funciones adicionales**: Incluye herramientas complementarias para una gestión de inventarios integral.

---

## 🛠 Tecnologías utilizadas

- Python
- Django
- MySQL
- openpyxl
- pandas
- python-docx

---

## ⚙️ Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

