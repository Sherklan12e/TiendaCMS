TiendaCMS

La tienda online es una plataforma web que permite a los usuarios navegar por un catálogo de productos, agregar artículos al carrito, realizar compras y gestionar pedidos. Los administradores pueden gestionar productos, categorías, inventario y pedidos desde un panel de administración.
2. 🎯 Objetivos del Sistema

    Permitir a los clientes comprar productos de forma segura.

    Ofrecer una interfaz intuitiva para el usuario.

    Proporcionar un panel de administración para la gestión eficiente de productos y pedidos.

    Gestionar pagos en línea.

    Ofrecer historial de compras a los usuarios registrados.

3. 👤 Tipos de Usuario
Tipo de Usuario	Descripción
Cliente	Usuario que navega por la tienda, realiza compras y gestiona su cuenta.
Administrador	Usuario con privilegios para gestionar productos, pedidos y usuarios.
4. ✅ Requisitos Funcionales

    Registro y Autenticación

        Registro de nuevos usuarios.

        Inicio de sesión y cierre de sesión.

        Recuperación de contraseña.

        Verificación por correo electrónico (opcional).

    Gestión de Productos

        Crear, editar, eliminar y listar productos (admin).

        Ver detalles de productos (cliente).

        Filtros por categoría, precio, etc.

    Carrito de Compras

        Agregar productos al carrito.

        Eliminar productos del carrito.

        Ver contenido del carrito y total a pagar.

    Proceso de Compra (Checkout)

        Ingreso de dirección de envío.

        Selección del método de pago.

        Confirmación de pedido.

    Pagos

        Integración con pasarela de pago (ej. PayPal, Stripe, MercadoPago).

        Confirmación automática del pago.

    Gestión de Pedidos

        Visualización de pedidos por parte del cliente.

        Estado del pedido (pendiente, enviado, entregado).

        Gestión de pedidos por parte del admin.

    Perfil de Usuario

        Ver y editar datos personales.

        Ver historial de compras.

    Panel de Administración

        CRUD de productos y categorías.

        Gestión de usuarios.

        Gestión de pedidos.

5. ❌ Requisitos No Funcionales

    Seguridad:

        Uso de HTTPS.

        Encriptación de contraseñas (hash).

        Validación de formularios.

    Escalabilidad:

        Arquitectura que permita escalar fácilmente (API REST, base de datos relacional).

    Usabilidad:

        Interfaz clara y adaptada a dispositivos móviles (responsive design).

    Rendimiento:

        Carga rápida de páginas.

        Paginación y búsqueda optimizada.

    Compatibilidad:

        Compatible con navegadores modernos (Chrome, Firefox, Safari, Edge).

6. 🗃️ Tecnologías Sugeridas

    Frontend: ReactJS, Bootstrap o Tailwind.

    Backend: Django + Django Rest Framework o Node.js + Express.

    Base de Datos: PostgreSQL, MySQL o SQLite.

    Autenticación: JWT o sesión con cookies.

    Pasarela de Pago: Stripe, PayPal o MercadoPago.

