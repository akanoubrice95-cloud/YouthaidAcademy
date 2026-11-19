// Youthaid Academy — menu, recherche et formulaires.
(function () {
  const root = document.documentElement;
  const lang = root.lang === 'en' ? 'en' : 'fr';
  const base = root.dataset.base || '';
  const T = {
    fr: { none: 'Aucun résultat pour', sent: 'Votre messagerie va s’ouvrir avec votre message prêt à envoyer. Il ne vous reste qu’à cliquer sur « Envoyer ».' },
    en: { none: 'No results for', sent: 'Your email app will open with your message ready to send. Just click “Send”.' },
  }[lang];

  // ---- Menu mobile ----
  const nav = document.querySelector('.main-nav');
  const menuBtn = document.querySelector('.menu-toggle');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', String(open));
    });
  }
  document.querySelectorAll('.nav-parent').forEach((btn) => {
    btn.addEventListener('click', () => {
      const li = btn.closest('.has-sub');
      const open = li.classList.toggle('open');
      btn.setAttribute('aria-expanded', String(open));
    });
  });

  // ---- Recherche ----
  const toggle = document.querySelector('.search-toggle');
  const panel = document.getElementById('search-panel');
  if (toggle && panel) {
    const input = panel.querySelector('.search-input');
    const results = panel.querySelector('.search-results');
    let index = null;
    const norm = (s) => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
    const esc = (s) => s.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

    async function load() {
      if (index) return index;
      try {
        const res = await fetch(base + 'assets/search-' + lang + '.json?v=' + (root.dataset.v || ''));
        index = await res.json();
      } catch { index = []; }
      return index;
    }
    function snippet(text, pos, len) {
      const s = Math.max(0, pos - 50), e = Math.min(text.length, pos + len + 70);
      return (s > 0 ? '…' : '') + esc(text.slice(s, pos)) + '<mark>' + esc(text.slice(pos, pos + len)) + '</mark>' + esc(text.slice(pos + len, e)) + (e < text.length ? '…' : '');
    }
    async function search() {
      const q = input.value.trim();
      if (!q) { results.innerHTML = ''; return; }
      const nq = norm(q);
      const pages = await load();
      const hits = [];
      for (const p of pages) {
        const t = norm(p.title).includes(nq);
        const pos = norm(p.text).indexOf(nq);
        if (t || pos !== -1) hits.push({ p, html: pos !== -1 ? snippet(p.text, pos, q.length) : esc(p.text.slice(0, 110)) + '…', score: t ? 0 : 1 });
      }
      hits.sort((a, b) => a.score - b.score);
      results.innerHTML = hits.length
        ? hits.slice(0, 12).map(({ p, html }) => `<li><a href="${base}${p.url}"><span class="r-title">${esc(p.title)}</span><span class="r-snippet">${html}</span></a></li>`).join('')
        : `<li class="r-empty">${T.none} « ${esc(q)} »</li>`;
    }
    function setOpen(open) {
      panel.hidden = !open;
      toggle.setAttribute('aria-expanded', String(open));
      if (open) { input.focus(); load(); }
    }
    toggle.addEventListener('click', () => setOpen(panel.hidden));
    input.addEventListener('input', search);
    panel.querySelector('form').addEventListener('submit', (e) => {
      e.preventDefault();
      const first = results.querySelector('a');
      if (first) first.click();
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !panel.hidden) { setOpen(false); toggle.focus(); }
    });
    document.addEventListener('click', (e) => {
      if (!panel.hidden && !e.target.closest('.search-wrap')) setOpen(false);
    });
  }

  // ---- Formulaires : ouverture de la messagerie avec le message pré-rempli ----
  document.querySelectorAll('form[data-mailto]').forEach((form) => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const lines = [];
      form.querySelectorAll('[name]').forEach((el) => {
        if (el.type === 'checkbox') { if (el.checked) lines.push('- ' + el.dataset.label); return; }
        if (!el.value) return;
        const label = form.querySelector(`label[for="${el.id}"]`);
        lines.push((label ? label.textContent.replace(/\s*\*$/, '') : el.name) + ' : ' + el.value);
      });
      const href = 'mailto:' + form.dataset.mailto + '?subject=' + encodeURIComponent(form.dataset.subject || 'Youthaid Academy') + '&body=' + encodeURIComponent(lines.join('\n'));
      window.location.href = href;
      const status = form.querySelector('.form-status');
      if (status) { status.textContent = T.sent; status.hidden = false; }
    });
  });

  // ---- Année du pied de page ----
  document.querySelectorAll('.year').forEach((el) => { el.textContent = new Date().getFullYear(); });
})();
