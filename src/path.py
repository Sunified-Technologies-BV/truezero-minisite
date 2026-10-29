# Rewrite the pathway cards: consortium and podcast get hover tips and RHS drawer panels, EnergyTag becomes a small tile with its own panel.
import re
s = open('body.html', encoding='utf-8').read()
a = s.index('      <div class="pcard">\n        <div class="lbl">R&amp;D consortium</div>')
b = s.index('      <div class="pcard">\n        <div class="lbl">Open source · Hedera</div>')
thumb = re.search(r'<a class="thumb" href="https://www\.youtube\.com/watch\?v=g713YCFDrjc"[^>]*><img src="(data:image/jpeg;base64,[^"]+)"', s).group(1)

cards = f'''      <div class="pcard">
        <div class="lbl">R&amp;D consortium · Sardinia pilot</div>
        <div class="logo-row"><a class="logo-plate" href="https://denyse.org/" target="_blank" rel="noopener" aria-label="DENYSE, Sharing Energy"><img src="media/denyse-logo.png" alt="DENYSE, Sharing Energy" loading="lazy"></a><a class="logo-plate" href="https://cacip.it/en/about-us/" target="_blank" rel="noopener" aria-label="CACIP, Consorzio Industriale Provinciale di Cagliari"><img src="media/cacip-logo.png" alt="CACIP, Consorzio Industriale Provinciale di Cagliari" loading="lazy"></a></div>
        <button class="pd-open" type="button" data-panel="den" aria-haspopup="dialog" aria-controls="fly-drawer"><span><b>DENYSE and CACIP.</b><small>Consortium, partners and the pilot →</small></span><em class="tip" role="tooltip">Eurostars 3 consortium of five (Bausch Datacom, Hypha Energy, Chaintegrator, RITTEC, Sunified). Stage 1 pilot with CACIP, the Industrial Consortium of the Province of Cagliari, Sardinia, then TRL 7 and 8.<u>Click for the full picture →</u></em></button>
        <p class="hg-short">Sunified brings the UNITY chip, key management, the crypto anchor and the protocol to a five-partner Eurostars consortium.<sup class="ref"><a href="#r9">9</a></sup> The Stage 1 build runs at CACIP in Sardinia.</p>
        <div class="trl" aria-label="Pathway to TRL 7 and 8"><a class="on pilot" href="https://cacip.it/en/about-us/" target="_blank" rel="noopener" title="CACIP, Cagliari, Sardinia: the Stage 1 pilot site">Pilots · CACIP Sardinia ↗</a><span class="goal">TRL 7</span><span class="goal">TRL 8</span></div>
        <button class="btn primary pd-open hg-cta" type="button" data-panel="den" aria-haspopup="dialog" aria-controls="fly-drawer">Open the consortium panel →</button>
        <a class="lnk" href="https://denyse.org/" target="_blank" rel="noopener">denyse.org ↗</a>
      </div>
      <div class="pcard">
        <div class="lbl">Podcast · 2Tokens</div>
        <button class="pd-open" type="button" data-panel="pod" aria-haspopup="dialog" aria-controls="fly-drawer"><span><b>Tagging Energy.</b><small>The podcast, in one page →</small></span><em class="tip" role="tooltip">LGV with Killian Daly of EnergyTag, recorded for the 2Tokens podcast: why hourly, located certificates need a reading signed at the source.<u>Click for the full picture →</u></em></button>
        <a class="thumb neon" href="https://www.youtube.com/watch?v=g713YCFDrjc" target="_blank" rel="noopener" aria-label="Watch Tagging Energy on YouTube"><img src="{thumb}" alt="" loading="lazy"></a>
        <p class="hg-short">Leon-Gerard Vandenberg with Killian Daly of EnergyTag<sup class="ref"><a href="#r5">5</a></sup> on the importance of transparency in the energy market.<sup class="ref"><a href="#r10">10</a></sup></p>
        <button class="tile pd-open" type="button" data-panel="etag" aria-haspopup="dialog" aria-controls="fly-drawer" aria-label="EnergyTag, open the panel"><img src="media/energytag-logo.png" alt="EnergyTag" loading="lazy"><span>EnergyTag · hourly certificates →</span><em class="tip" role="tooltip">Sunified sits in all three EnergyTag working groups. UNITY supplies the timestamped, located reading beneath hourly Granular Certificates.<u>Click for the full picture →</u></em></button>
        <button class="btn primary pd-open hg-cta" type="button" data-panel="pod" aria-haspopup="dialog" aria-controls="fly-drawer">Open the podcast panel →</button>
        <a class="lnk" href="https://www.youtube.com/watch?v=g713YCFDrjc" target="_blank" rel="noopener">Watch on YouTube ↗</a>
      </div>
'''
s = s[:a] + cards + s[b:]

# Hedera card: give its buttons the same data-panel mechanism
s = s.replace('<button class="hg-open" type="button" aria-haspopup="dialog" aria-controls="fly-drawer">', '<button class="hg-open pd-open" type="button" data-panel="hed" aria-haspopup="dialog" aria-controls="fly-drawer">')
s = s.replace('<button class="btn primary hg-open hg-cta" type="button" aria-haspopup="dialog" aria-controls="fly-drawer">Open the Hedera Guardian panel →</button>', '<button class="btn primary pd-open hg-cta" type="button" data-panel="hed" aria-haspopup="dialog" aria-controls="fly-drawer">Open the Hedera Guardian panel →</button>')

L = lambda t, u: f'<a href="{u}" target="_blank" rel="noopener">{t} ↗</a>'
DEN = ('<div class="hg-head"><img src="media/denyse-logo.png" alt="DENYSE" class="fd-logo"><div><div class="eye">R&amp;D consortium · Eurostars 3, project 5238</div><h3 id="fd-title">DENYSE and the Sardinia pilot</h3><p class="fd-who">Bausch Datacom · Hypha Energy (Value-X) · Chaintegrator (Zaisan) · RITTEC · Sunified</p></div></div>'
       '<p class="fd-lead">A digital infrastructure for decentralised and decarbonised energy: communities finance, own and share renewable energy, and Sunified supplies the signed data those assets depend on.</p>'
       '<p>DENYSE started in July 2023 and runs to February 2027 under Eurostars 3 (project 5238). The Consortium Agreement of 5 January 2024 names five parties. Sunified brings the UNITY chip, key management, the crypto anchor and the protocol; Bausch Datacom the gateway hardware; RITTEC the device management and IEC 62443 work; Hypha Energy the application layer and tokenisation; Chaintegrator the DLT backend.</p>'
       '<h4 class="fd-h4">The pilot: CACIP, Cagliari, Sardinia</h4><div class="hg-head"><img src="media/cacip-logo.png" alt="CACIP" class="fd-logo sm"><p>CACIP is the Industrial Consortium of the Province of Cagliari, founded in 1961, which manages one of the largest industrial and logistics zones in Europe. The Stage 1 build wires a live panel there to a Hedera Guardian policy: a signed reading from the panel, a certificate from the policy.</p></div>'
       '<h4 class="fd-h4">Pathway</h4><div class="trl fd-trl"><span class="on">Pilots</span><span class="goal">TRL 7</span><span class="goal">TRL 8</span></div><p>Consortium pilots first, then TRL 7 and 8 with the consortium partners. Telemetry is already live on a balcony solar system; the Stage 1 build is in procurement.</p>'
       '<div class="fd-ev"><div><i class="tg verified">VERIFIED</i><span>DENYSE Consortium Agreement, 5 January 2024, five parties.</span></div><div><i class="tg stated">STATED</i><span>Sardinia Stage 1 and the pathway, LGV, True Zero pitch, 29 Oct 2026.</span></div></div>'
       '<div class="fd-links">' + ''.join([L('DENYSE', 'https://denyse.org/'), L('CACIP', 'https://cacip.it/en/about-us/'), L('Bausch Datacom', 'https://www.bausch.eu/'), L('Hypha Energy', 'https://hypha.energy/'), L('Chaintegrator', 'https://chaintegrator.com/'), L('RITTEC', 'https://www.rittec.de/'), L('Sunified', 'https://www.sunified.com/')]) + '</div>')
POD = ('<div class="hg-head"><div><div class="eye">Podcast · 2Tokens</div><h3 id="fd-title">Tagging Energy</h3><p class="fd-who">Leon-Gerard Vandenberg, Sunified · Killian Daly, EnergyTag</p></div></div>'
       f'<a class="thumb neon fd-thumb" href="https://www.youtube.com/watch?v=g713YCFDrjc" target="_blank" rel="noopener" aria-label="Watch Tagging Energy on YouTube"><img src="{thumb}" alt=""></a>'
       '<p class="fd-lead">Transparency in the energy market: why a certificate is only as good as the reading underneath it.</p>'
       '<p>Recorded for the 2Tokens podcast, the Dutch public and private tokenisation roadmap whose partners include ABN AMRO and Rabobank. Killian Daly runs EnergyTag, the standard that cuts a Guarantee of Origin into hourly Granular Certificates so the same unit of energy cannot go to two buyers. LGV’s side: the certificate layer assumes a trustworthy measurement and does not specify one, and UNITY signs that measurement on the panel.</p>'
       '<p>Europe settles in fifteen minutes, Australia in five; hourly matching takes the power market as its mental model. A reading that carries time and location, signed where it is made, is what makes that match checkable.</p>'
       '<div class="fd-ev"><div><i class="tg verified">VERIFIED</i><span>2Tokens Foundation, “Tagging Energy: the importance of transparency in the energy market”, YouTube g713YCFDrjc.</span></div></div>'
       '<div class="fd-links">' + ''.join([L('Watch on YouTube', 'https://www.youtube.com/watch?v=g713YCFDrjc'), L('2Tokens', 'https://2tokens.org/'), L('EnergyTag', 'https://energytag.org/'), L('Killian Daly on LinkedIn', 'https://www.linkedin.com/in/killianpdaly/'), L('LGV on LinkedIn', 'https://www.linkedin.com/in/leongvandenberg')]) + '</div>')
ETAG = ('<div class="hg-head"><div class="logo-plate fd-plate"><img src="media/energytag-logo.png" alt="EnergyTag"></div><div><div class="eye">Standard · hourly matching</div><h3 id="fd-title">EnergyTag</h3><p class="fd-who">Independent non-profit, London. Granular Certificate standard for hourly, located energy attribute certificates.</p></div></div>'
        '<p class="fd-lead">Hourly matching needs a reading that carries time and location. UNITY signs both at the panel.</p>'
        '<p>Guarantees of Origin track over a quarter of the electricity used in Europe, at a resolution designed twenty years ago. EnergyTag’s Granular Certificate standard cuts a GO into hourly certificates while keeping them linked. Sunified is a participant in all three EnergyTag working groups: WG1 Standard and Guidelines, WG3 Policy and Awareness, and the EU 24/7 CFE group.</p>'
        '<p>UNITY sits below the certificate layer as the attestation the standard assumes but does not specify. RED III already allows Guarantees of Origin in 1 Wh fractions and the proposed GHG Protocol Scope 2 revision moves toward hourly matching; each asks for measurement that is expensive to fake.</p>'
        '<div class="fd-ev"><div><i class="tg verified">VERIFIED</i><span>EnergyTag working-group invitations, July 2026.</span></div><div><i class="tg verified">VERIFIED</i><span>energytag.org/about-us, read 29 Oct 2026.</span></div></div>'
        '<div class="fd-links">' + ''.join([L('energytag.org', 'https://energytag.org/'), L('Killian Daly, Executive Director', 'https://www.linkedin.com/in/killianpdaly/'), L('Podcast: Tagging Energy', 'https://www.youtube.com/watch?v=g713YCFDrjc')]) + '</div>')

def js(x): return "'" + x.replace('\\', '\\\\').replace("'", "\\'") + "'"
old = "document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.hg-open');if(b){last=b;openHTML(HED);}});"
assert old in s
new = ("var PANELS={hed:HED,den:" + js(DEN) + ",pod:" + js(POD) + ",etag:" + js(ETAG) + "};\n"
       "document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.pd-open');if(b&&PANELS[b.dataset.panel]){last=b;openHTML(PANELS[b.dataset.panel]);}});")
s = s.replace(old, new)
open('body.html', 'w', encoding='utf-8').write(s)
print('ok', s.count('pd-open'))
