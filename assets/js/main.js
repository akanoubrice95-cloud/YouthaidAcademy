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
  const norm = (s) => s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  const esc = (s) => s.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  let searchIndex = null;
  async function loadIndex() {
    if (searchIndex) return searchIndex;
    try {
      const res = await fetch(base + 'assets/search-' + lang + '.json?v=' + (root.dataset.v || ''));
      searchIndex = await res.json();
    } catch { searchIndex = []; }
    return searchIndex;
  }
  function snippet(text, pos, len) {
    const s = Math.max(0, pos - 50), e = Math.min(text.length, pos + len + 70);
    return (s > 0 ? '…' : '') + esc(text.slice(s, pos)) + '<mark>' + esc(text.slice(pos, pos + len)) + '</mark>' + esc(text.slice(pos + len, e)) + (e < text.length ? '…' : '');
  }
  function bindSearch(input, results, form) {
    async function search() {
      const q = input.value.trim();
      if (!q) { results.innerHTML = ''; return; }
      const nq = norm(q);
      const pages = await loadIndex();
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
    input.addEventListener('input', search);
    input.addEventListener('focus', loadIndex, { once: true });
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      await search();
      const first = results.querySelector('a');
      if (first) first.click();
    });
    return search;
  }

  // Loupe en haut à droite
  const toggle = document.querySelector('.search-toggle');
  const panel = document.getElementById('search-panel');
  if (toggle && panel) {
    const input = panel.querySelector('.search-input');
    bindSearch(input, panel.querySelector('.search-results'), panel.querySelector('form'));
    function setOpen(open) {
      panel.hidden = !open;
      toggle.setAttribute('aria-expanded', String(open));
      if (open) { input.focus(); loadIndex(); }
    }
    toggle.addEventListener('click', () => setOpen(panel.hidden));
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !panel.hidden) { setOpen(false); toggle.focus(); }
    });
    document.addEventListener('click', (e) => {
      if (!panel.hidden && !e.target.closest('.search-wrap')) setOpen(false);
    });
  }

  // Barre de recherche de l'accueil
  const heroSearch = document.querySelector('.hero-search');
  if (heroSearch) {
    const results = heroSearch.querySelector('.search-results');
    bindSearch(heroSearch.querySelector('.search-input'), results, heroSearch.querySelector('form'));
    document.addEventListener('click', (e) => { if (!e.target.closest('.hero-search')) results.innerHTML = ''; });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') results.innerHTML = ''; });
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

  // ==========================================================
  // MOTION — animations & interactions (désactivées si « réduire les animations »)
  // ==========================================================
  const motion = root.classList.contains('motion');
  const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));

  // Découpe un élément en mots (en conservant les balises internes).
  function splitWords(el, outer, inner) {
    let i = 0;
    const walk = (node) => {
      [...node.childNodes].forEach((child) => {
        if (child.nodeType === 3) {
          const frag = document.createDocumentFragment();
          child.textContent.split(/(\s+)/).forEach((part) => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            const w = document.createElement('span');
            w.className = outer;
            if (inner) {
              const wi = document.createElement('span');
              wi.className = inner; wi.style.setProperty('--i', i); wi.textContent = part;
              w.appendChild(wi);
            } else { w.textContent = part; }
            w.dataset.i = i++;
            frag.appendChild(w);
          });
          child.replaceWith(frag);
        } else if (child.nodeType === 1) { walk(child); }
      });
    };
    walk(el);
    return i;
  }

  // Barre de progression + en-tête compact (toujours actifs : purement informatifs)
  const header = document.querySelector('.site-header');
  const bar = document.querySelector('.scroll-progress');
  let ticking = false;
  const scrubs = [];
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      const y = window.scrollY;
      const max = document.documentElement.scrollHeight - window.innerHeight;
      if (bar) bar.style.setProperty('--p', max > 0 ? (y / max).toFixed(4) : 0);
      if (header) header.classList.toggle('scrolled', y > 12);
      scrubs.forEach((fn) => fn());
      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });

  if (motion) {
    // 1. Titre du hero : les mots montent un à un
    const h1 = document.querySelector('.hero h1');
    if (h1) { splitWords(h1, 'wm', 'wi'); h1.classList.add('split'); }

    // 2. Texte qui s'illumine mot à mot au défilement
    document.querySelectorAll('[data-scrub]').forEach((el) => {
      const n = splitWords(el, 'sw');
      const words = el.querySelectorAll('.sw');
      const marks = el.querySelectorAll('.mark');
      el.classList.add('scrub-ready');
      scrubs.push(() => {
        const r = el.getBoundingClientRect();
        const vh = window.innerHeight;
        const prog = clamp((vh * 0.85 - r.top) / (r.height + vh * 0.35), 0, 1);
        const lit = Math.round(prog * n);
        words.forEach((w, k) => w.classList.toggle('on', k < lit));
        marks.forEach((m) => {
          const last = m.querySelectorAll('.sw');
          m.classList.toggle('on', last.length && last[last.length - 1].classList.contains('on'));
        });
      });
    });

    // 3. Apparition des blocs au défilement, en cascade
    const targets = document.querySelectorAll(
      'main .section-head, main .grid > *, main .step, main .cta-band, main .statement .lead, main .prose, main .follow-band, main .faq details, main .empty, main .form'
    );
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries) => {
        entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
      targets.forEach((el) => {
        if (el.closest('.hero')) return;
        const sibs = [...el.parentElement.children].filter((c) => c.matches(el.tagName.toLowerCase() + (el.className ? '.' + el.className.trim().split(/\s+/)[0] : '')));
        el.style.setProperty('--d', (Math.max(0, sibs.indexOf(el)) % 6) * 0.09 + 's');
        el.classList.add('rv');
        io.observe(el);
      });
    }

    if (finePointer) {
      // 4. Parallaxe du visuel du hero (lissée)
      const pv = document.querySelector('[data-parallax]');
      const hero = document.querySelector('.hero');
      if (pv && hero) {
        let tx = 0, ty = 0, cx = 0, cy = 0, raf = null;
        const loop = () => {
          cx += (tx - cx) * 0.08; cy += (ty - cy) * 0.08;
          pv.style.setProperty('--px', cx.toFixed(3)); pv.style.setProperty('--py', cy.toFixed(3));
          raf = Math.abs(tx - cx) + Math.abs(ty - cy) > 0.001 ? requestAnimationFrame(loop) : null;
        };
        const kick = () => { if (!raf) raf = requestAnimationFrame(loop); };
        hero.addEventListener('pointermove', (e) => {
          const r = hero.getBoundingClientRect();
          tx = ((e.clientX - r.left) / r.width - 0.5) * 2;
          ty = ((e.clientY - r.top) / r.height - 0.5) * 2;
          kick();
        });
        hero.addEventListener('pointerleave', () => { tx = 0; ty = 0; kick(); });
      }

      // 5. Cartes en 3D + halo qui suit le pointeur
      document.querySelectorAll('.card.hover').forEach((card) => {
        card.addEventListener('pointermove', (e) => {
          const r = card.getBoundingClientRect();
          const x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
          card.classList.add('tilting');
          card.style.transform = `perspective(900px) rotateX(${(0.5 - y) * 8}deg) rotateY(${(x - 0.5) * 10}deg) translateY(-6px)`;
          card.style.setProperty('--sx', x * 100 + '%'); card.style.setProperty('--sy', y * 100 + '%');
        });
        card.addEventListener('pointerleave', () => { card.classList.remove('tilting'); card.style.transform = ''; });
      });

      // 6. Boutons magnétiques
      document.querySelectorAll('main .btn, .btn-don').forEach((b) => {
        b.addEventListener('pointermove', (e) => {
          const r = b.getBoundingClientRect();
          b.style.translate = `${(e.clientX - r.left - r.width / 2) * 0.22}px ${(e.clientY - r.top - r.height / 2) * 0.3}px`;
        });
        b.addEventListener('pointerleave', () => { b.style.translate = ''; });
      });
    }

    // 7. Suggestions qui s'écrivent dans la barre de recherche
    document.querySelectorAll('[data-typewriter]').forEach((input) => {
      const words = input.dataset.typewriter.split('|');
      const original = input.placeholder;
      let w = 0, c = 0, del = false, timer = null;
      const step = () => {
        if (document.activeElement === input || input.value) { input.placeholder = original; timer = setTimeout(step, 600); return; }
        const word = words[w];
        c += del ? -1 : 1;
        input.placeholder = word.slice(0, c) + (c < word.length || del ? '|' : '…');
        let wait = del ? 40 : 85;
        if (!del && c === word.length) { del = true; wait = 1500; }
        else if (del && c === 0) { del = false; w = (w + 1) % words.length; wait = 350; }
        timer = setTimeout(step, wait);
      };
      timer = setTimeout(step, 1800);
    });
  }
  onScroll();

  // ---- Année du pied de page ----
  document.querySelectorAll('.year').forEach((el) => { el.textContent = new Date().getFullYear(); });
})();
