# Rebuild the #flywheel section: big slide, 8 compact boxes with hover tip + click drawer.
import re, json, html
s = open('body.html', encoding='utf-8').read()
a = s.index('<section id="flywheel"')
b = s.index('</section>', a) + len('</section>')

M = [
 dict(n='01', t='Park O&M', who='NovaSource Power Services', tag='STATED',
      tip='Per-panel temperature and health every 30 seconds, signed. Predictive maintenance first, predictive dispatch second. LGV on the call, 29 Oct 2026.',
      lead='Operators and asset managers get a signed per-panel reading instead of a site-level inference from one weather station.',
      body=['Panel efficiency is directly proportional to panel temperature. Today a solar farm infers temperature from one weather station on the site, and the temperature gradient across a large park changes with the wind. Per-panel temperature lets the operator build a data model that forecasts production properly.',
            'First-year benefits are predictive maintenance and predictive dispatch: faults are localised before a truck roll, soiling and string dropouts show up in the signal, and the P50, P90 and P99 of each asset rest on a reading nobody downstream can alter.',
            'Once a seasonal data set exists, the same data supports futures for the day-ahead and sub-day markets.'],
      quote=('We give a signal on the efficiency of each solar panel. Panel efficiency is directly proportional to panel temperature.', 'LGV, answer to Bodin Scepanovic, True Zero pitch, 29 Oct 2026 (45:22)'),
      ev=[('STATED', 'LGV on the call, 29 Oct 2026, named NovaSource as the O&M operator class.')],
      links=[('NovaSource Power Services', 'https://www.novasourcepower.com/')]),
 dict(n='02', t='Energy Communities', who='Prosume · DENYSE · CACIP', tag='VERIFIED',
      tip='Sunified is one of five DENYSE partners (Eurostars 3, project 5238). Stage 1 pilot with CACIP, Cagliari, Sardinia. Prosume is the community launch.',
      lead='Signed readings let a community divide the energy and the incentives among its members and reward green consumption.',
      body=['DENYSE is a Eurostars 3 R&D consortium (project 5238, start July 2023, extended to February 2027) building a digital infrastructure for decentralised and decarbonised energy. Five partners: Bausch Datacom, Value-X (now Hypha Energy), Zaisan (now Chaintegrator), RITTEC and Sunified. Sunified brings the UNITY chip, key management, the crypto anchor and the protocol.',
            'The Stage 1 build wires a live panel to a Hedera Guardian policy, with CACIP, the Industrial Consortium of the Province of Cagliari in Sardinia, as the reference site. Prosume is the Sunified energy-community launch, Sardinia first.',
            'Telemetry is already live on a balcony solar system, so a small system can prove what it produced without a utility meter.'],
      quote=('Energy communities, to divide the energy and the incentives and to reward green consumption.', 'LGV, True Zero pitch, 29 Oct 2026'),
      ev=[('VERIFIED', 'DENYSE Consortium Agreement, 5 January 2024, five parties.'), ('STATED', 'Prosume and the Sardinia pilot, LGV, 29 Oct 2026.')],
      links=[('Prosume', 'https://prosume.io/'), ('DENYSE', 'https://denyse.org/'), ('CACIP, Cagliari', 'https://cacip.it/en/about-us/'), ('Bausch Datacom', 'https://www.bausch.eu/'), ('Hypha Energy (Value-X)', 'https://hypha.energy/'), ('Chaintegrator (Zaisan)', 'https://chaintegrator.com/'), ('RITTEC', 'https://www.rittec.de/')]),
 dict(n='03', t='Grid Signalling', who='Gridcog · BitTrader', tag='STATED',
      tip='Ten signed samples per five-minute settlement interval: store, dispatch or curtail. Battery arbitrage for day-ahead and flex markets. BitTrader URL still open.',
      lead='Ten signed samples in every five-minute settlement window give the battery operator an edge the meter cannot.',
      body=['In Australia energy is traded and settled every five minutes. With ten samples in that window the operator decides whether to store the energy, dispatch it, or run a dump load under curtailment when export is not allowed. Forecasting that is the battery arbitrage market.',
            'Batteries are the holy grail, but they cannot cover 24/7 yet. As they move from two hours to four to eight, the signal matters more for arbitrage efficiency. The quants are looking for an algorithmic edge, and Sunified gives it to them with data from behind the meter.',
            'Gridcog is the modelling and optimisation partner candidate, introduction via TIG. BitTrader (UK, AI energy arbitrage) was named on the 12 October 2026 call; its web address is not yet confirmed.'],
      quote=('Ten samples per interval decide whether to store, dispatch, or dump load under curtailment. That is the battery arbitrage market.', 'LGV, answer to Bodin Scepanovic, 29 Oct 2026 (46:44)'),
      ev=[('STATED', 'LGV, pitch Q&A, 29 Oct 2026.'), ('OPEN', 'BitTrader company URL not confirmed; intro requested 12 Oct 2026.')],
      links=[('Gridcog', 'https://www.gridcog.com/')]),
 dict(n='04', t='Guarantee of Origin', who='EnergyTag', tag='VERIFIED',
      tip='Sunified sits in all three EnergyTag working groups. UNITY supplies the timestamped, located reading beneath hourly Granular Certificates.',
      lead='Hourly matching needs a reading that carries time and location. UNITY signs both at the panel.',
      body=['Guarantees of Origin track over a quarter of the electricity used in Europe, at a resolution designed twenty years ago. EnergyTag’s Granular Certificate standard cuts a GO into hourly certificates while keeping them linked, so the same unit of energy cannot go to two buyers.',
            'Sunified is a participant in all three EnergyTag working groups: WG1 Standard and Guidelines, WG3 Policy and Awareness, and the EU 24/7 CFE group. UNITY sits below the certificate layer as the attestation the standard assumes but does not specify.',
            'RED III already allows Guarantees of Origin in 1 Wh fractions and the proposed GHG Protocol Scope 2 revision moves toward hourly matching. Each asks for measurement that is expensive to fake.'],
      quote=('Carbon credits as a digital financial product, delivered on a blockchain or into a database such as EnergyTag, so energy attribute certificates carry time and location.', 'LGV, True Zero pitch, 29 Oct 2026'),
      ev=[('VERIFIED', 'EnergyTag working-group invitations, July 2026.'), ('VERIFIED', '2Tokens podcast “Tagging Energy” with Killian Daly, YouTube g713YCFDrjc.')],
      links=[('EnergyTag', 'https://energytag.org/'), ('Killian Daly, Executive Director', 'https://www.linkedin.com/in/killianpdaly/'), ('Podcast: Tagging Energy', 'https://www.youtube.com/watch?v=g713YCFDrjc')]),
 dict(n='05', t='Insurance', who='WTW · Munich Re', tag='VERIFIED',
      tip='WTW is Sunified’s appointed insurance broker since 1 June 2021. A signed per-panel reading turns a disputed yield or damage claim into a checkable fact.',
      lead='Insurers pay first. A signed per-panel reading turns a disputed yield or damage claim into a checkable fact.',
      body=['WTW (Willis Australia Limited, trading as Willis, a WTW business) has been Sunified’s appointed, non-exclusive insurance broker since 1 June 2021, covering D&O, renewables asset insurance and creditor insurance for green PPAs and park offtake.',
            'The insurance question on a panel-level dataset is “is the project demonstrably under control”. Is the panel clean, is it maintained, what are the P50, P90 and P99. Signed readings answer each of those without a site visit, which is what underwriters price.',
            'Munich Re is the target capacity provider for a per-panel insurance wrapper that pairs attestation with cover. That engagement is not yet on record.'],
      quote=('Insurance quants and risk allocators: is the panel clean, is it maintained, what are the P50, P90 and P99.', 'LGV, True Zero pitch, 29 Oct 2026'),
      ev=[('VERIFIED', 'Insurance Broker Letter of Appointment, signed 1 June 2021.'), ('OPEN', 'Munich Re capacity: no engagement on record.')],
      links=[('WTW', 'https://www.wtwco.com/en-us'), ('Munich Re', 'https://www.munichre.com/en.html')]),
 dict(n='06', t='Digital Finance', who='ABN AMRO · Liqwith · Prosume', tag='VERIFIED',
      tip='Dutch tokenisation partners for dividing park yield and making energy programmable. ABN AMRO and Rabobank are 2Tokens partners. Sunified stays middleware.',
      lead='Divide the yield of a park and make the energy programmable. Sunified issues no tokens and runs no market; licensed partners do.',
      body=['Digital finance with blockchain partners in the Netherlands and Benelux: dividing the energy yield of a park and making energy programmable, with trials moving to progressive deployments.',
            'ABN AMRO and Rabobank are partners of the 2Tokens foundation, the Dutch public and private tokenisation roadmap Sunified has worked with since 2021. Liqwith is a Dutch fintech on the same track.',
            'Sunified is middleware. Insurers, lenders and registries build on the data; the protocol is licensed on FRAND terms so every manufacturer can build it in and share the data revenue. The mission is locked into a Dutch foundation (STAK), the same structure used by IKEA, ABN AMRO and Triodos Bank.'],
      quote=('Solar fully digitised as a financial product for democratisation. A millennial in rainy Amsterdam can own a bit of solar in Spain.', 'LGV, True Zero pitch, 29 Oct 2026'),
      ev=[('VERIFIED', '2tokens.org partner list, read 29 Oct 2026.'), ('STATED', 'Liqwith and the Benelux trials, LGV, 29 Oct 2026.')],
      links=[('ABN AMRO', 'https://www.abnamro.com/en/home'), ('Liqwith', 'https://liqwith.io/'), ('Prosume', 'https://prosume.io/'), ('2Tokens', 'https://2tokens.org/')]),
 dict(n='07', t='Distributed Compute', who='Expanso.io', tag='STATED',
      tip='Compute moves to where the signed energy is. Expanso runs pipelines on the nodes where data is created. On the Sunified roadmap for inference compute at parks.',
      lead='Bits are cheaper to move than electrons. Inference compute belongs where the green energy is produced.',
      body=['Training runs need one large memory space in a big data centre. Inference does not: it is bursty and distributable, so it can run at solar parks and distributed data centres powered by the energy on site.',
            'Expanso runs data pipelines on the nodes where the data is created, which is the pattern Sunified needs for signed telemetry and compute co-located with generation.',
            'On the Sunified roadmap as the distributed compute partner; discussed by LGV and Hicham Batou on 26 August 2026 and with Ben and Michael on 20 July 2026.'],
      quote=('You cannot keep on routing electrons, it costs you physically. But bits are free.', 'LGV, 26 Aug 2026'),
      ev=[('STATED', 'Sunified roadmap, LGV, 26 Aug 2026.')],
      links=[('Expanso', 'https://expanso.io/')]),
 dict(n='08', t='Programmable Energy', who='IBM · 2Tokens', tag='VERIFIED',
      tip='Crypto anchors (IBM Research) underpin the trust engine. 2Tokens is the Dutch tokenisation roadmap. Hedera Guardian minted a certificate from a signed reading on 22 Sep 2026.',
      lead='A reading signed on the die is a crypto anchor. That is what makes energy programmable without an oracle you have to trust.',
      body=['Crypto anchors, as described by IBM Research, bind a physical object to a digital record with a key that cannot be separated from the object. UNITY applies the idea to the energy measurement itself: the key never leaves the silicon, so the reading can be checked by anyone with no call to Sunified.',
            '2Tokens is the Dutch public and private initiative that maps how tokenisation reshapes finance; its partners include ABN AMRO and Rabobank. LGV recorded the “Tagging Energy” podcast with Killian Daly of EnergyTag under its banner.',
            'On 22 September 2026 a signed test credential was sent to a Hedera Guardian policy on testnet. The valid reading minted a certificate; a tampered copy was refused. If a carbon credit can be digitally defined, it can be financed and held as collateral.'],
      quote=('If I can’t digitally define it, it’s going to be really hard to finance, which means it’s not going to live as collateral.', 'Wes Geisenberger, Hashgraph, GBBC Blockchain Central UNGA, posted by @hedera 26 Oct 2026'),
      ev=[('VERIFIED', 'Crypto anchors, IBM Research, data room folder 3.'), ('VERIFIED', 'Hedera testnet credential, 22 Sep 2026.')],
      links=[('IBM', 'https://www.ibm.com/'), ('2Tokens', 'https://2tokens.org/'), ('Hedera Guardian', 'https://hedera.com/guardian'), ('Podcast: Tagging Energy', 'https://www.youtube.com/watch?v=g713YCFDrjc')]),
]

def esc(x): return html.escape(x, quote=True)
boxes = ''
for m in M:
    boxes += f'''        <button class="mk mk-btn" type="button" data-i="{int(m['n'])-1}" aria-haspopup="dialog" aria-controls="fly-drawer"><div class="n">{m['n']} <i class="tg {m['tag'].lower()}">{m['tag']}</i></div><b>{esc(m['t'])}</b><span>{esc(m['who'])}</span><em class="tip" role="tooltip">{esc(m['tip'])}<u>Click for the full picture →</u></em></button>\n'''

section = f'''<section id="flywheel" class="light slide" aria-labelledby="h-fly" style="border-top:1px solid var(--border-subtle)">
  <div class="dots"></div>
  <div class="wrap">
    <div class="eye">Unity · Solar Digitised</div>
    <h2 id="h-fly" style="font-size:clamp(32px,4vw,48px);margin-top:16px">Data Flywheel.</h2>
    <p class="lede-l">One verified data source. Concurrent, compounding revenue streams. Each Unity-signed reading serves eight markets at once; aggregated across parks, network effects compound value across the energy value chain.</p>
    <figure class="fly-fig"><img src="media/slide-5.jpg" alt="Slide 5, Data Flywheel: eight markets around the Unity Trust Engine" loading="lazy"><figcaption>Hover a market for the short version. Click it for the partners, the evidence and the links.</figcaption></figure>
    <div class="markets fly-grid">
{boxes}    </div>
    <p class="src" style="margin-top:16px">Outcome: a fully digitised energy smartgrid. Source: Unity Chip-enabled data from solar parks and BESS, signed at the source.</p>
    <div class="foot"><span>© 2026 Sunified Group BV</span><span>05 / 07</span></div>
  </div>
</section>
<div id="fly-overlay" class="fly-overlay" hidden></div>
<aside id="fly-drawer" class="fly-drawer" role="dialog" aria-modal="true" aria-labelledby="fd-title" hidden>
  <div class="fd-bar"><button type="button" class="fd-nav" id="fd-prev" aria-label="Previous market">←</button><span id="fd-count"></span><button type="button" class="fd-nav" id="fd-next" aria-label="Next market">→</button><button type="button" class="fd-close" id="fd-close" aria-label="Close">✕</button></div>
  <div class="fd-body" id="fd-body"></div>
</aside>
<script>
(function(){{
var M={json.dumps([dict(n=m['n'],t=m['t'],who=m['who'],tag=m['tag'],lead=m['lead'],body=m['body'],quote=m['quote'],ev=m['ev'],links=m['links']) for m in M], ensure_ascii=False)};
var dr=document.getElementById('fly-drawer'),ov=document.getElementById('fly-overlay'),bd=document.getElementById('fd-body'),ct=document.getElementById('fd-count'),cur=0,last=null;
function esc(s){{return String(s).replace(/[&<>"]/g,function(c){{return{{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]}})}}
function render(i){{cur=(i+8)%8;var m=M[cur];ct.textContent=m.n+' / 08';
 var h='<div class="eye">Market '+m.n+' · <i class="tg '+m.tag.toLowerCase()+'">'+m.tag+'</i></div><h3 id="fd-title">'+esc(m.t)+'</h3><p class="fd-who">'+esc(m.who)+'</p><p class="fd-lead">'+esc(m.lead)+'</p>';
 m.body.forEach(function(p){{h+='<p>'+esc(p)+'</p>'}});
 h+='<blockquote class="fd-q"><p>“'+esc(m.quote[0])+'”</p><footer>'+esc(m.quote[1])+'</footer></blockquote>';
 h+='<div class="fd-ev">'+m.ev.map(function(e){{return '<div><i class="tg '+e[0].toLowerCase()+'">'+e[0]+'</i><span>'+esc(e[1])+'</span></div>'}}).join('')+'</div>';
 h+='<div class="fd-links">'+m.links.map(function(l){{return '<a href="'+esc(l[1])+'" target="_blank" rel="noopener">'+esc(l[0])+' ↗</a>'}}).join('')+'</div>';
 bd.innerHTML=h;bd.scrollTop=0;}}
function open(i){{render(i);dr.hidden=false;ov.hidden=false;requestAnimationFrame(function(){{dr.classList.add('on');ov.classList.add('on')}});document.body.classList.add('fly-lock');document.getElementById('fd-close').focus();}}
function close(){{dr.classList.remove('on');ov.classList.remove('on');document.body.classList.remove('fly-lock');setTimeout(function(){{dr.hidden=true;ov.hidden=true;if(last)last.focus();}},260);}}
document.querySelectorAll('.mk-btn').forEach(function(b){{b.addEventListener('click',function(){{last=b;open(+b.dataset.i)}})}});
document.getElementById('fd-close').addEventListener('click',close);ov.addEventListener('click',close);
document.getElementById('fd-prev').addEventListener('click',function(){{render(cur-1)}});
document.getElementById('fd-next').addEventListener('click',function(){{render(cur+1)}});
document.addEventListener('keydown',function(e){{if(dr.hidden)return;if(e.key==='Escape')close();if(e.key==='ArrowLeft')render(cur-1);if(e.key==='ArrowRight')render(cur+1);}});
}})();
</script>'''
s = s[:a] + section + s[b:]
open('body.html', 'w', encoding='utf-8').write(s)
print('ok', s.count('mk-btn'))
