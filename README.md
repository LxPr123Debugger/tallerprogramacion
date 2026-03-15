SIGEF - Sistema de Gestión de Flotas


SIGEF (Sistema Integrado de Gestión de Flotas) es una aplicación web desarrollada para empresas del sector logístico y de transporte de carga que buscan optimizar la administración de sus vehículos, conductores, mantenimientos y documentación legal. El sistema permite una gestión centralizada, automatizada y escalable, reduciendo errores humanos y mejorando la eficiencia operativa.



Objetivo General
Desarrollar un sistema modular que permita el control integral de flotas vehiculares, abarcando mantenimiento preventivo, consumo de combustible, documentación legal y asignación de conductores, con el fin de minimizar costos operativos y garantizar el cumplimiento normativo.


Alcance del Proyecto
Dentro del alcance:
Gestión del inventario de vehículos (alta, modificación y baja).

Control y actualización del odómetro por unidad.

Generación automática de órdenes de mantenimiento preventivo (por tiempo o kilometraje).

Registro y análisis de consumo de combustible.

Almacenamiento digital de documentos legales (SOAT, revisión técnica, permisos) con control de vencimientos.

Notificaciones automáticas por tablero y correo electrónico.

Asignación de conductores con validación de licencias vigentes.

Generación de reportes gerenciales en PDF (costos operativos y eficiencia de combustible).

Fuera del alcance (futuras expansiones):
Integración en tiempo real con dispositivos GPS o sensores IoT.

Gestión de nómina o liquidación de conductores.

Módulos de facturación o contabilidad.

Tecnologías Utilizadas
Componente	Tecnología
Backend	Python (Django / Flask)
Base de Datos	PostgreSQL
ORM	SQLAlchemy / Django ORM
Tareas Programadas	Celery + Redis
Análisis de Datos	Pandas
Frontend	HTML, CSS, Bootstrap (responsive)
Autenticación	RBAC (Roles: Administrador, Operador, Auditor)
Reportes	Generación de PDF
Arquitectura del Sistema
El sistema sigue el patrón Modelo-Vista-Controlador (MVC) para separar la lógica de negocio de la interfaz de usuario. Esto permite una mejor organización del código, escalabilidad y mantenibilidad.

Modelo: Representa los datos y la lógica de negocio (vehículos, conductores, mantenimientos, etc.).

Vista: Interfaz de usuario responsiva, accesible desde escritorio, tablet y móvil.

Controlador: Maneja las peticiones del usuario, interactúa con el modelo y retorna respuestas a la vista.

Funcionalidades Clave
Gestión de Flota
Registro y administración de vehículos (marca, modelo, placa, VIN, año).

Actualización diaria del kilometraje.

Mantenimiento Preventivo
Generación automática de órdenes de mantenimiento según intervalos de tiempo o kilometraje.

Alertas anticipadas para mantenimientos próximos.

Control de Combustible
Registro de cargas de combustible con costo, cantidad y kilometraje.

Cálculo del rendimiento por unidad.

Documentación Legal
Almacenamiento digital de documentos (SOAT, revisión técnica, permisos).

Control de fechas de vencimiento con notificaciones automáticas.

Gestión de Conductores
Asignación de conductores a vehículos.

Validación automática de licencias vigentes.

Reportes Gerenciales
Generación de informes PDF con:

Costo operativo por vehículo.

Eficiencia de combustible mensual.

Notificaciones
Alertas visuales en el tablero y por correo electrónico (15 días antes de vencimientos).

Seguridad y Calidad
Control de acceso basado en roles (RBAC): Administrador, Operador, Auditor.

Auditoría: Registro inmutable de modificaciones en la base de datos.

Disponibilidad: 99.5% garantizada durante operación continua (24/7).

Rendimiento: Respuesta en menos de 2 segundos en consultas típicas.

Portabilidad: Compatible con navegadores modernos (Chrome, Firefox, Edge).

Justificación
El sistema SIGEF responde a la necesidad del sector logístico de reducir la incertidumbre operativa, evitar sanciones legales por documentación vencida y minimizar costos asociados a mantenimientos correctivos y consumo ineficiente de combustible. La elección de Python y PostgreSQL garantiza una solución escalable, segura y preparada para futuras integraciones con tecnologías emergentes como telemetría o IoT.

Proyecciones Futuras
Integración con dispositivos GPS para seguimiento en tiempo real.

Conexión con sensores IoT para telemetría avanzada.

Expansión a módulos de facturación y contabilidad.

Implementación de dashboards dinámicos con visualización de datos en tiempo real.

Bibliografía Recomendada
Amat, J. (2021). Control de gestión y costes logísticos. Editorial UOC.

Aris, A. (2020). Python para principiantes. Ediciones de la U.

Cervantes, J., & García, A. (2022). Fundamentos de bases de datos relacionales con PostgreSQL. Alfaomega.

Chonillo, L., & Meza, J. (2023). Sistemas de gestión de transporte (TMS). Revista de Logística y Distribución.

Mora, L. A. (2021). Gestión logística integral. Ecoe Ediciones.

Sommerville, I. (2019). Ingeniería de software. Pearson Educación.


Autores:

Edwin David Wilches Caicedo
José Leonardo Peñuela León
Ángel Manuel Garzón Patiño



Docente: Diana Marcela Toquica Rodríguez
Universidad Manuela Beltrán
Ingeniería de Software - 2026

