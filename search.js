// Recherche sur le site.
// Pour rendre une nouvelle page cherchable, ajoute-la dans PAGES.
const PAGES = [
  { url: 'index.html', title: 'Accueil' },
];

(function () {
  const toggle = document.querySelector('.search-toggle');
  const panel = document.getElementById('search-panel');
  const form = panel.querySelector('.search-form');
  const input = panel.querySelector('.search-input');
  const results = panel.querySelector('.search-results');
  let index = null;

  const normalize = (s) => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  const escapeHtml = (s) => s.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

  async function loadIndex() {
    if (index) return index;
    index = await Promise.all(PAGES.map(async (page) => {
      try {
        const html = await (await fetch(page.url)).text();
        const doc = new DOMParser().parseFromString(html, 'text/html');
        doc.querySelectorAll('script, style, header, footer').forEach((el) => el.remove());
        const text = (doc.querySelector('main') || doc.body).textContent.replace(/\s+/g, ' ').trim();
        return { ...page, text };
      } catch {
        return { ...page, text: '' };
      }
    }));
    return index;
  }

  function snippet(text, pos, len) {
    const start = Math.max(0, pos - 40);
    const end = Math.min(text.length, pos + len + 60);
    return (start > 0 ? '…' : '') +
      escapeHtml(text.slice(start, pos)) +
      '<mark>' + escapeHtml(text.slice(pos, pos + len)) + '</mark>' +
      escapeHtml(text.slice(pos + len, end)) +
      (end < text.length ? '…' : '');
  }

  async function search() {
    const q = input.value.trim();
    if (!q) { results.innerHTML = ''; return; }
    const nq = normalize(q);
    const pages = await loadIndex();
    const hits = [];
    for (const p of pages) {
      const inTitle = normalize(p.title).includes(nq);
      const pos = normalize(p.text).indexOf(nq);
      if (inTitle || pos !== -1) {
        hits.push({ p, html: pos !== -1 ? snippet(p.text, pos, q.length) : escapeHtml(p.text.slice(0, 100)) });
      }
    }
    results.innerHTML = hits.length
      ? hits.map(({ p, html }) =>
          `<li><a href="${p.url}"><span class="r-title">${escapeHtml(p.title)}</span><span class="r-snippet">${html}</span></a></li>`).join('')
      : `<li class="r-empty">Aucun résultat pour « ${escapeHtml(q)} »</li>`;
  }

  function setOpen(open) {
    panel.hidden = !open;
    toggle.setAttribute('aria-expanded', String(open));
    if (open) { input.focus(); loadIndex(); }
  }

  toggle.addEventListener('click', () => setOpen(panel.hidden));
  input.addEventListener('input', search);
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const first = results.querySelector('a');
    if (first) first.click();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !panel.hidden) { setOpen(false); toggle.focus(); }
  });
  document.addEventListener('click', (e) => {
    if (!panel.hidden && !e.target.closest('.topbar')) setOpen(false);
  });
})();
