// ============================================================
// SCRIPT: Crear estructura RENDIMENSION 2026 en Google Drive
// INSTRUCCIONES:
//   1. Abre https://drive.google.com en Chrome
//   2. Presiona F12 → Console
//   3. Pega TODO este código y presiona Enter
//   4. Espera ~30 segundos hasta ver "✅ ESTRUCTURA COMPLETA"
// ============================================================

(async () => {
  // Get auth token from gapi (already loaded on drive.google.com)
  const tok = window.gapi?.auth2?.getAuthInstance?.()?.currentUser?.get?.()?.getAuthResponse?.()?.access_token
           || window.gapi?.client?.getToken?.()?.access_token;

  if (!tok) {
    console.error('❌ No se encontró token. Asegúrate de estar en drive.google.com y logueado.');
    return;
  }

  async function mkFolder(name, parentId) {
    const body = { name, mimeType: 'application/vnd.google-apps.folder' };
    if (parentId) body.parents = [parentId];
    const r = await fetch('https://www.googleapis.com/drive/v3/files', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer ' + tok, 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });
    const d = await r.json();
    if (d.id) console.log('  ✅ Creada:', name, '→', d.id);
    else console.error('  ❌ Error en:', name, d.error?.message);
    return d;
  }

  console.log('🚀 Iniciando creación de estructura RENDIMENSION 2026...\n');

  // 1. Carpeta raíz
  const root = await mkFolder('RENDIMENSION 2026', null);
  if (!root.id) return console.error('❌ Falló la carpeta raíz. Abortando.');
  const rootId = root.id;

  // 2. Subcarpetas principales
  console.log('\n📁 Creando carpetas principales...');
  const [clientes, empresa, marketing, activos, archivo] = await Promise.all([
    mkFolder('CLIENTES', rootId),
    mkFolder('EMPRESA', rootId),
    mkFolder('MARKETING', rootId),
    mkFolder('PROYECTOS ACTIVOS', rootId),
    mkFolder('ARCHIVO', rootId),
  ]);

  // 3. Subcarpetas de EMPRESA
  console.log('\n📁 Creando subcarpetas de EMPRESA...');
  await Promise.all([
    mkFolder('Legal', empresa.id),
    mkFolder('Logos & Brand', empresa.id),
    mkFolder('Finanzas', empresa.id),
    mkFolder('Templates', empresa.id),
  ]);

  // 4. Subcarpetas de MARKETING
  console.log('\n📁 Creando subcarpetas de MARKETING...');
  await Promise.all([
    mkFolder('Social Media', marketing.id),
    mkFolder('Portfolio', marketing.id),
    mkFolder('Samples', marketing.id),
    mkFolder('Campanias', marketing.id),
  ]);

  // 5. Subcarpetas de ARCHIVO (por año)
  console.log('\n📁 Creando subcarpetas de ARCHIVO...');
  await Promise.all([
    mkFolder('2022', archivo.id),
    mkFolder('2023', archivo.id),
    mkFolder('2024', archivo.id),
    mkFolder('2025', archivo.id),
  ]);

  // 6. Carpetas de los 5 leads dormidos dentro de CLIENTES
  console.log('\n👥 Creando carpetas de leads dormidos en CLIENTES...');
  await Promise.all([
    mkFolder('Robin Wells - 2026', clientes.id),
    mkFolder('Justin Utley - 2026', clientes.id),
    mkFolder('Lama Khoury - 2026', clientes.id),
    mkFolder('Thu Hoang - 2026', clientes.id),
    mkFolder('Anne Grice - 2026', clientes.id),
  ]);

  // 7. Carpetas de clientes activos identificados
  console.log('\n👥 Creando carpetas de clientes activos en CLIENTES...');
  await Promise.all([
    mkFolder('Debi House - 2022', clientes.id),
    mkFolder('Jorge Castillo - 2024', clientes.id),
    mkFolder('New Harbor Project - 2025', clientes.id),
    mkFolder('Mark House - 2025', clientes.id),
    mkFolder('Maestrall-Nautian - 2025', clientes.id),
    mkFolder('Brown Troop - 2025', clientes.id),
    mkFolder('Carruseles Prestige - 2026', clientes.id),
    mkFolder('Gubb House - 2022', clientes.id),
    mkFolder('Mike Pleasant - 2022', clientes.id),
    mkFolder('NF Renderings North Fork - 2024', clientes.id),
    mkFolder('250 Lanark - 2024', clientes.id),
    mkFolder('No More U Closets - 2025', clientes.id),
    mkFolder('No More U Fences - 2025', clientes.id),
    mkFolder('JC Website - 2025', clientes.id),
    mkFolder('RICK BOLT - 2025', clientes.id),
  ]);

  console.log('\n✅ ESTRUCTURA COMPLETA CREADA');
  console.log('📂 RENDIMENSION 2026 ID:', rootId);
  console.log('📂 CLIENTES ID:', clientes.id);
  console.log('📂 EMPRESA ID:', empresa.id);
  console.log('📂 MARKETING ID:', marketing.id);
  console.log('\n👉 Navega a: https://drive.google.com/drive/folders/' + rootId);
})();
