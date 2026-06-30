# Design System Document: High-End Editorial Beauty & Wellness

## 1. Overview & Creative North Star: "GS Estetica Integral"
Sitio web profesional para GS Estetica Integral, un centro de estética con enfoque en bienestar y belleza personalizada.

## 2. Colors: Pastel Pink & White Aurora Mesh
Paleta suave de rosas pastel sobre base blanca con efecto aurora mesh.

### Aurora Mesh Background
El fondo principal usa un gradiente mesh estático compuesto de múltiples radial-gradients superpuestos en tonos rosados pastel sobre blanco, creando un efecto etéreo y fresco.

### Color Palette
*   **Primary:** Pastel pinks (`#FFD1DC`, `#FFB7C5`, `#FF9EB5`)
*   **Base:** White (`#FFFFFF`) and very light pink (`#FFF5F7`)
*   **Deepest accent:** `#FF85A1`

---

## 3. Typography: The Editorial Voice
The contrast between a high-character Serif and a functional Sans-Serif provides the "Premium" anchor.

*   **Display & Headlines (Noto Serif):** These are our "hero" moments. Use `display-lg` with generous letter-spacing (-0.02em) to evoke luxury fashion mastheads.
*   **Body & Titles (Be Vietnam Pro):** A clean, modern sans-serif that ensures readability. Use `body-lg` (1rem) for general descriptions to keep the layout feeling light and airy.
*   **The Hierarchy Strategy:** Headlines should always be `primary` (#71585b) to provide authority, while body text stays at `on-surface-variant` (#4f4445) to maintain a soft, low-contrast elegance.

---

## 4. Elevation & Depth: Tonal Layering
Traditional shadows are too "tech." We use ambient light.

*   **The Layering Principle:** Stacking is our primary tool. 
    *   *Lowest:* `surface-container-low` (#f6f3f3)
    *   *Mid:* `surface` (#fcf9f9)
    *   *Highest:* `surface-container-lowest` (#ffffff)
*   **Ambient Shadows:** When a hover-lift is required (e.g., on a treatment card), use an extra-diffused shadow: `box-shadow: 0 20px 40px rgba(113, 88, 91, 0.06)`. Note the use of a tinted shadow (using the `primary` hue) rather than black.
*   **The "Ghost Border" Fallback:** If a container needs definition against a white background, use `outline-variant` (#d2c3c4) at **15% opacity**. It should be felt, not seen.

---

## 5. Components: Soft & Purposeful

### Buttons
*   **Primary:** Background: `primary` (#71585b); Text: `on-primary` (#ffffff). Shape: `medium` (moderate roundedness).
*   **Secondary:** Background: `secondary-container` (#efe0d4); Text: `on-secondary-container`.
*   **Interaction:** On hover, primary buttons should scale slightly (1.02x) and deepen in tone. Avoid "glow" effects.

### Input Fields
*   **Style:** Minimalist underline or moderate-radius container using `surface-container-high`.
*   **Focus State:** Transition the background to `primary-container` (#f8d7da) with a 2px `primary` bottom-border. No "blue" defaults.

### Cards & Treatment Lists
*   **Rule:** Forbid divider lines.
*   **Implementation:** Use a `0.75rem` (md) or `1rem` (lg) corner radius to ensure a soft but defined look. Separate list items with `20px` of vertical white space and use a very subtle background shift on hover (`surface-bright`).

### Specialized Components
*   **Floating WhatsApp:** A `surface-container-lowest` circle with a `primary` icon and a 10% opacity `primary` shadow. Positioned with `24px` padding from the viewport edge.
*   **The "GS" Loader:** A soft fading transition between pages rather than a spinning wheel, maintaining the spa's "flow."

---

## 6. Do’s and Don’ts

### Do:
*   **Embrace Asymmetry:** Place an image slightly off-center from the text block to create a custom, high-end feel.
*   **Use Balanced Margins:** Ensure elements have enough room to breathe without feeling disconnected.
*   **Tint Everything:** Use the `primary` or `secondary` tones even in your grays to keep the warmth.

### Don't:
*   **No Sharp Edges:** Avoid `0px` or `2px` radiuses. Maintain the moderate softness established in the theme.
*   **No Pure Black:** Never use #000000. Use `on-surface` (#1b1b1c) for the deepest tones.
*   **No Grid-Lock:** Don't feel forced to align every card in a perfectly square grid. Vary the heights (Masonry-lite) to keep the "Editorial" feel alive.