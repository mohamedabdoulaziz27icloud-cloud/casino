<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>1X NIGER 1M - TEST HTTPS</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial}
body{background:#081324;color:#fff}
.header{background:#0f1c2e;padding:14px;display:flex;justify-content:space-between;align-items:center;border-bottom:3px solid #2ecc71}
.logo{font-weight:900;font-size:22px} .logo span{background:#2ecc71;color:#000;padding:3px 7px;border-radius:5px}
.badge{background:#ffcc00;color:#000;font-size:10px;padding:4px 8px;border-radius:20px;font-weight:800}
.solde-bar{background:#121f33;padding:12px;display:flex;justify-content:space-between;border-bottom:1px solid #1e3a5f}
.solde-bar b{color:#ffcc00;font-size:18px}
.card{background:#121f33;margin:10px;border-radius:12px;padding:14px;border:1px solid #1e3a5f}
.btn{width:100%;padding:14px;border:none;border-radius:10px;font-weight:800;font-size:14px;cursor:pointer}
.btn-green{background:#2ecc71;color:#000} .btn-red{background:#ff3b30;color:#fff}
input{width:100%;padding:12px;background:#050d1a;border:1px solid #1e3a5f;border-radius:8px;color:#fff;margin:6px 0}
.admin-link{font-size:10px;color:#555;text-align:center;margin:10px}
</style>
</head>
<body>

<div class="header">
<div class="logo">1X <span>NIGER</span></div>
<div class="badge">HTTPS TEST 1M</div>
</div>

<div class="solde-bar">
<div>SOLDE<br><b id="solde">0 XOF</b></div>
<div style="text-align:right"><div style="font-size:10px;color:#2ecc71">MAISON 80%</div><div style="font-size:10px;color:#8da0b8">Panel: admin.html</div></div>
</div>

<div class="card">
<h4 style="font-size:13px;margin-bottom:6px">💰 DÉPÔT TEST (sans CinetPay)</h4>
<input id="montant" type="number" value="1000" placeholder="500 min">
<button class="btn btn-green" onclick="depot()">+ CRÉDITER TEST 1000 XOF</button>
<p style="font-size:10px;color:#8da0b8;margin-top:6px">Mode test HTTPS - crédite instant pour tester Aviator</p>
</div>

<div class="card">
<div style="display:flex;justify-content:space-between"><h4>✈️ AVIATOR MAISON 80%</h4><span style="font-size:10px;color:#ff3b30">60% crash <1.8x</span></div>
<div style="text-align:center;margin:14px 0">
<div id="mult" style="font-size:48px;font-weight:900;color:#2ecc71">1.00x</div>
<div id="plane" style="font-size:32px;margin-top:4px">✈️</div>
</div>
<div style="display:flex;gap:8px">
<input id="mise" value="500" style="flex:1" type="number">
<button id="betBtn" onclick="bet()" class="btn btn-green" style="flex:1">PARIER</button>
</div>
<button id="cashBtn" onclick="cash()" class="btn btn-red" style="display:none;margin-top:8px">CASHOUT 0 XOF</button>
<div id="hist" style="background:#000;height:80px;overflow:auto;font-size:11px;padding:8px;border-radius:8px;margin-top:8px"></div>
</div>

<div class="card">
<h4 style="font-size:13px">📤 RETRAIT TEST</h4>
<input id="retNum" placeholder="+227 XX XX XX XX">
<input id="retMont" placeholder="Montant">
<button class="btn btn-red" onclick="retrait()">DEMANDER RETRAIT TEST</button>
</div>

<div class="admin-link"><a href="admin.html" style="color:#555">Panel Admin 1M -> admin.html (code 227227)</a></div>

<script>
let solde=parseInt(localStorage.getItem('solde_1m')||'0');
let enJeu=false,mise=0,mult=1,crash=1.8;
let historique=JSON.parse(localStorage.getItem('hist_1m')||'[]');

function upd(){document.getElementById('solde').innerText=solde+' XOF'; localStorage.setItem('solde_1m',solde);}

function depot(){
let m=parseInt(document.getElementById('montant').value)||1000;
solde+=m; upd(); addHist('DEPOT','+'+m,true);
alert('✅ TEST HTTPS: +'+m+' XOF crédité\nSolde: '+solde+' XOF\n\nSur GitHub c’est bien HTTPS');
}

function genCrash(){
let r=Math.random();
if(r<0.60) return 1.01+Math.random()*0.79; // 60% <1.8x = maison 80%
if(r<0.85) return 1.8+Math.random()*1.2;  // 25% 1.8-3x
return 3+Math.random()*7; // 15% >3x
}

function bet(){
let m=parseInt(document.getElementById('mise').value);
if(m>solde) return alert('Solde insuffisant - fais dépôt test');
if(enJeu) return;
solde-=m; mise=m; enJeu=true; crash=genCrash(); mult=1; upd();
document.getElementById('betBtn').style.display='none';
document.getElementById('cashBtn').style.display='block';
document.getElementById('mult').style.color='#2ecc71';
let i=0;
let loop=setInterval(()=>{
if(!enJeu){clearInterval(loop);return;}
i++; mult=1+i*0.09;
document.getElementById('mult').innerText=mult.toFixed(2)+'x';
document.getElementById('plane').style.transform='translateX('+(i*2)+'px)';
document.getElementById('cashBtn').innerText='CASHOUT '+(m*mult).toFixed(0)+' XOF';
if(mult>=crash){
clearInterval(loop); enJeu=false;
document.getElementById('mult').innerText='💥 '+crash.toFixed(2)+'x';
document.getElementById('mult').style.color='#ff3b30';
document.getElementById('betBtn').style.display='block';
document.getElementById('cashBtn').style.display='none';
addHist('CRASH '+crash.toFixed(2)+'x','-'+m,false);
document.getElementById('plane').style.transform='translateX(0)';
setTimeout(()=>{document.getElementById('mult').style.color='#2ecc71'; document.getElementById('mult').innerText='1.00x';},1200);
}
},110);
}

function cash(){
if(!enJeu) return;
// 8% chance trop tard maison 80%
if(Math.random()<0.08){enJeu=false; solde-=0; document.getElementById('betBtn').style.display='block'; document.getElementById('cashBtn').style.display='none'; addHist('TROP TARD','-'+mise,false); alert('Trop tard - Maison 80%'); return;}
let g=Math.floor(mise*mult); solde+=g; enJeu=false; upd();
document.getElementById('betBtn').style.display='block';
document.getElementById('cashBtn').style.display='none';
addHist('WIN '+mult.toFixed(2)+'x','+'+g,true);
}

function retrait(){
let m=parseInt(document.getElementById('retMont').value);
if(m>solde) return alert('Solde insuffisant');
solde-=m; upd(); addHist('RETRAIT '+document.getElementById('retNum').value,'-'+m,false);
alert('Demande retrait '+m+' XOF enregistrée (TEST)');
}

function addHist(t,mm,win){
let d=new Date().toLocaleTimeString();
let c=win?'#2ecc71':'#ff3b30';
document.getElementById('hist').innerHTML=`<div style="display:flex;justify-content:space-between"><span>${d} ${t}</span><span style="color:${c}">${mm}</span></div>`+document.getElementById('hist').innerHTML;
historique.unshift({t,mm,d}); if(historique.length>20) historique.pop(); localStorage.setItem('hist_1m',JSON.stringify(historique));
}

upd();
// charge hist
historique.forEach(h=>{
let c=h.mm.includes('+')?'#2ecc71':'#ff3b30';
document.getElementById('hist').innerHTML+=`<div style="display:flex;justify-content:space-between"><span>${h.d} ${h.t}</span><span style="color:${c}">${h.mm}</span></div>`;
});
</script>
</body>
</html>
