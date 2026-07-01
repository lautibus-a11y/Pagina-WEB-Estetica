import re
import urllib.parse

def generate_service_html(service_str):
    if " — " in service_str:
        name, price = service_str.split(" — ", 1)
    else:
        name = service_str
        price = "Consultar"
        
    encoded_name = urllib.parse.quote(name)
    
    return f"""                    <div class="service-item" onclick="toggleService(this)">
                        <div class="service-item-header"><svg class="w-5 h-5 check" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg><span>{name} — {price}</span><svg class="chevron" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></div>
                        <div class="service-item-body"><p class="service-desc">Para más detalles y agendar un turno, contáctanos por WhatsApp.</p><button onclick="event.stopPropagation(); window.open('https://wa.me/5491144445555?text=Hola%20GS%20Estetica%20Integral%2C%20quiero%20agendar%20un%20turno%20para%20{encoded_name}', '_blank')" class="service-whatsapp-btn"><svg fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg> Agendar</button></div>
                    </div>"""

def generate_js_array(items):
    lines = []
    for item in items:
        name = item.split(" — ")[0] if " — " in item else item
        lines.append(f"                '{name}',")
    # remove last comma
    if lines:
        lines[-1] = lines[-1].rstrip(',')
    return "\n".join(lines)


# Define new services
cosme = [
    "Facial para adolescente (acné) — $20.000",
    "Facial + aparatología (antiage) — $22.000",
    "Peeling — $25.000",
    "Peeling con dermaplaning — $25.000",
    "Dermapen — $30.000",
    "Hilos cosmetológicos — $35.000",
    "Aparatología facial — Consultar precio"
]

bienestar = [
    "Tratamientos para estrías — Consultar precio",
    "Tratamientos reductores — Promos desde $30.000",
    "Vacumterapia — Consultar precio",
    "Cavitador — Consultar precio",
    "Ondas rusas — Consultar precio",
    "Radiofrecuencia — Consultar precio",
    "HIFU, Velaslim, etc. — Consultar precio"
]

manos = [
    "Masajes relajantes — $25.000",
    "Masajes con elementos — Consultar precio",
    "Pulidos corporales — $25.000",
    "Depilación con cera integral — Consultar precio"
]

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Cosmetologia HTML list
cosme_html = "\n".join(generate_service_html(s) for s in cosme)
html = re.sub(
    r'(<div id="modal-cosmetologia".*?<div class="service-list">)(.*?)(</div>\s*</div>\s*</div>\s*</div>)',
    lambda m: m.group(1) + "\n" + cosme_html + "\n                " + m.group(3),
    html,
    flags=re.DOTALL
)

# Replace Bienestar HTML list
bienestar_html = "\n".join(generate_service_html(s) for s in bienestar)
html = re.sub(
    r'(<div id="modal-bienestar".*?<div class="service-list">)(.*?)(</div>\s*</div>\s*</div>\s*</div>)',
    lambda m: m.group(1) + "\n" + bienestar_html + "\n                " + m.group(3),
    html,
    flags=re.DOTALL
)

# Replace Manos HTML list
manos_html = "\n".join(generate_service_html(s) for s in manos)
html = re.sub(
    r'(<div id="modal-manos".*?<div class="service-list">)(.*?)(</div>\s*</div>\s*</div>\s*</div>)',
    lambda m: m.group(1) + "\n" + manos_html + "\n                " + m.group(3),
    html,
    flags=re.DOTALL
)

# Rename "Manos y Pies" to "Manicuria y podologia" in modal header
html = html.replace('<h3 class="font-serif text-2xl text-pink-800">Manos y Pies</h3>', '<h3 class="font-serif text-2xl text-pink-800">Manicuria y podologia</h3>')
# Also rename in bento grid
html = html.replace('<h3>Manos y Pies</h3>', '<h3>Manicuria y podologia</h3>')
# Also rename in option
html = html.replace('<option value="Manos y Pies">Manos y Pies</option>', '<option value="Manicuria y podologia">Manicuria y podologia</option>')

# Update JS data
cosme_js = generate_js_array(cosme)
html = re.sub(
    r"('Cosmetología': \[)(.*?)(\])",
    lambda m: m.group(1) + "\n" + cosme_js + "\n            " + m.group(3),
    html,
    flags=re.DOTALL
)

bienestar_js = generate_js_array(bienestar)
html = re.sub(
    r"('Bienestar Integral': \[)(.*?)(\])",
    lambda m: m.group(1) + "\n" + bienestar_js + "\n            " + m.group(3),
    html,
    flags=re.DOTALL
)

manos_js = generate_js_array(manos)
html = re.sub(
    r"('Manos y Pies': \[)(.*?)(\])",
    lambda m: "'Manicuria y podologia': [\n" + manos_js + "\n            ]",
    html,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done")
