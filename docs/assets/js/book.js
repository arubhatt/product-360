/* The Product 360 Handbook: theme, navigation, search, copy and checklists. */
(function () {
  var doc = document.documentElement;
  function store(k, v) {
    try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; }
  }

  // theme
  var themeBtn = document.getElementById("theme-btn");
  if (themeBtn) themeBtn.addEventListener("click", function () {
    var t = doc.dataset.theme === "light" ? "dark" : "light";
    doc.dataset.theme = t;
    store("p360-theme", t);
  });

  // mobile sidebar
  var side = document.getElementById("side"), scrim = document.getElementById("scrim"), menu = document.getElementById("menu-btn");
  function toggleSide(open) { side.classList.toggle("open", open); scrim.classList.toggle("open", open); }
  if (menu) menu.addEventListener("click", function () { toggleSide(!side.classList.contains("open")); });
  if (scrim) scrim.addEventListener("click", function () { toggleSide(false); });
  var on = side && side.querySelector(".nav-l.on");
  if (on) on.scrollIntoView({ block: "center" });

  // reading progress
  var bar = document.querySelector(".progress span");
  function progress() {
    var h = doc.scrollHeight - innerHeight;
    if (bar) bar.style.width = (h > 0 ? (scrollY / h) * 100 : 0) + "%";
  }
  addEventListener("scroll", progress, { passive: true });
  progress();

  // scrollspy for the right rail
  var links = [].slice.call(document.querySelectorAll(".rail-l a"));
  if (links.length) {
    var heads = links.map(function (a) { return document.getElementById(decodeURIComponent(a.hash.slice(1))); });
    var spy = function () {
      var idx = 0;
      for (var i = 0; i < heads.length; i++) if (heads[i] && heads[i].getBoundingClientRect().top < 120) idx = i;
      links.forEach(function (a, i) { a.classList.toggle("on", i === idx); });
    };
    addEventListener("scroll", spy, { passive: true });
    spy();
  }

  // copy and fold buttons on prompts and templates
  document.addEventListener("click", function (ev) {
    var b = ev.target.closest(".blk-copy");
    if (b) {
      var text = b.closest(".blk").querySelector("pre code").innerText;
      var done = function () { b.textContent = "Copied"; b.classList.add("ok"); setTimeout(function () { b.textContent = "Copy"; b.classList.remove("ok"); }, 1600); };
      if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(done);
      else { var ta = document.createElement("textarea"); ta.value = text; document.body.appendChild(ta); ta.select(); document.execCommand("copy"); ta.remove(); done(); }
      return;
    }
    var t = ev.target.closest(".blk-toggle");
    if (t) { var blk = t.closest(".blk"); blk.classList.toggle("open"); t.textContent = blk.classList.contains("open") ? "Hide" : "Show"; }
  });

  // checklists remember their state in this browser
  [].forEach.call(document.querySelectorAll(".chk input"), function (c) {
    if (store("p360-chk-" + c.dataset.k) === "1") c.checked = true;
    c.addEventListener("change", function () { store("p360-chk-" + c.dataset.k, c.checked ? "1" : "0"); });
  });

  // search
  var modal = document.getElementById("search-modal"), input = document.getElementById("search-input"), results = document.getElementById("search-results");
  var index = window.P360_INDEX || [], sel = 0, hits = [];
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function openSearch() { modal.hidden = false; input.value = ""; render(); setTimeout(function () { input.focus(); }, 10); }
  function closeSearch() { modal.hidden = true; }
  function snippet(x, terms) {
    var low = x.toLowerCase(), pos = low.indexOf(terms[0]);
    var start = Math.max(0, pos - 60), s = (start ? "…" : "") + x.slice(start, start + 220) + "…";
    s = esc(s);
    terms.forEach(function (t) { if (t.length > 1) s = s.replace(new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig"), "<mark>$1</mark>"); });
    return s;
  }
  function render() {
    var q = input.value.trim().toLowerCase();
    if (!q) { results.innerHTML = '<div class="sr-empty">Search chapters, frameworks, templates and prompts.</div>'; hits = []; return; }
    var terms = q.split(/\s+/);
    hits = [];
    index.forEach(function (r) {
      var hay = (r.h + " " + r.x).toLowerCase(), score = 0;
      for (var i = 0; i < terms.length; i++) { if (hay.indexOf(terms[i]) < 0) return; score += r.h.toLowerCase().indexOf(terms[i]) >= 0 ? 5 : 1; }
      hits.push({ r: r, s: score });
    });
    hits.sort(function (a, b) { return b.s - a.s; });
    hits = hits.slice(0, 30);
    sel = 0;
    results.innerHTML = hits.length ? hits.map(function (h, i) {
      return '<a class="sr' + (i === 0 ? " on" : "") + '" href="' + h.r.u + '"><div class="sr-c">' + esc((h.r.n ? h.r.n + " · " : "") + h.r.c) + '</div><div class="sr-h">' + esc(h.r.h) + '</div><div class="sr-x">' + snippet(h.r.x, terms) + "</div></a>";
    }).join("") : '<div class="sr-empty">No results for “' + esc(q) + '”.</div>';
  }
  function move(d) {
    var els = results.querySelectorAll(".sr");
    if (!els.length) return;
    els[sel].classList.remove("on");
    sel = (sel + d + els.length) % els.length;
    els[sel].classList.add("on");
    els[sel].scrollIntoView({ block: "nearest" });
  }
  [].forEach.call(document.querySelectorAll("[data-search-open]"), function (b) { b.addEventListener("click", openSearch); });
  if (input) {
    input.addEventListener("input", render);
    input.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown") { e.preventDefault(); move(1); }
      else if (e.key === "ArrowUp") { e.preventDefault(); move(-1); }
      else if (e.key === "Enter") { var a = results.querySelectorAll(".sr")[sel]; if (a) location.href = a.href; }
    });
  }
  if (modal) modal.addEventListener("click", function (e) { if (e.target === modal) closeSearch(); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "/" && modal.hidden && !/input|textarea/i.test(document.activeElement.tagName)) { e.preventDefault(); openSearch(); }
    else if (e.key === "Escape" && !modal.hidden) closeSearch();
  });
})();
