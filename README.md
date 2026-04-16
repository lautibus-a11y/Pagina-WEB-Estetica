# Ethereal Beauty - Centro de Estética

## Estructura del Proyecto

```
Estetica/
├── index.html          # Página principal
├── vercel.json         # Configuración de despliegue Vercel
├── .gitignore         # Archivos ignorados por Git
├── code.html          # Versión original del diseño
├── DESIGN.md          # Documentación del sistema de diseño
├── screen.png         # Captura de pantalla
└── images/
    ├── hero/          # Imágenes del Hero
    │   └── hero-1.jpg
    ├── gallery/      # Imágenes de la Galería
    │   ├── gallery-1.jpg
    │   ├── gallery-2.jpg
    │   ├── gallery-3.jpg
    │   └── gallery-4.jpg
    └── team/          # Imágenes del Equipo
        ├── team-1.jpg
        ├── team-2.jpg
        ├── team-3.jpg
        ├── team-4.jpg
        └── team-5.jpg
```

## Cómo agregar imágenes

### 1. Hero Section
Coloca las imágenes del hero en `images/hero/` y actualiza la ruta en `index.html`:

```html
<!-- Línea 463 aproximadamente -->
<img src="images/hero/tu-imagen.jpg" alt="Hero"/>
```

### 2. Galería
Coloca las imágenes en `images/gallery/` y actualiza:

```html
<!-- Líneas aprox. 540-555 -->
<img src="images/gallery/tu-imagen.jpg" alt="Galería"/>
```

### 3. Carrousel de Ofertas
Las imágenes están en las líneas del carrousel (aprox. 470-540). Actualiza las URLs.

### 4. Equipo (Slider)
Coloca las fotos del equipo en `images/team/` y actualiza en el carrousel del equipo.

## Despliegue en Vercel

### Opción 1: Via GitHub (Recomendado)

1. Sube este proyecto a un repositorio de GitHub
2. Ve a [vercel.com](https://vercel.com)
3. Click en "New Project"
4. Importa tu repositorio de GitHub
5. Vercel detectará automáticamente que es un sitio estático
6. Click en "Deploy"

### Opción 2: Via Vercel CLI

```bash
# Instalar Vercel CLI
npm i -g vercel

# Iniciar sesión
vercel login

# Desplegar
vercel

# Desplegar en producción
vercel --prod
```

### Opción 3: Drag & Drop

1. Ve a [vercel.com](https://vercel.com)
2. Click en "Add New" → "Project"
3. Selecciona "Import Third-Party Git Repository" → "Or import a local project via CLI"
4. Arrastra esta carpeta al área de deployment

## Tecnologías Utilizadas

- **HTML5** - Estructura
- **Tailwind CSS** (CDN) - Estilos
- **Google Fonts** - Tipografía (Playfair Display + Poppins)
- **Vanilla JavaScript** - Interactividad

## Características

- ✨ Diseño responsive (Mobile First)
- 🎨 Paleta de colores rosa pastel y beige
- 📱 Compatible con todos los dispositivos
- ⚡ Animaciones suaves
- 💬 Integración con WhatsApp para reservas

## Notas de Desarrollo

- El proyecto usa Tailwind CSS via CDN (no requiere build)
- Todas las imágenes externas son de Unsplash (para desarrollo)
- Para producción, reemplaza las URLs de Unsplash con tus imágenes locales

---

© 2024 Ethereal Beauty Center
