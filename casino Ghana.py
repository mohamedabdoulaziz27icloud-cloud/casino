<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<title>1WIN Ghana Aviator</title>
<script src="https://telegram.org/js/telegram-web-app.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial}
body{background:#0b0e2a;color:#fff;overflow:hidden}
.header{background:#12152e;padding:12px;display:flex;justify-content:space-between;align-items:center}
.balance{background:#1e2142;padding:8px 15px;border-radius:20px;color:#00ff88;font-weight:bold}
.crash-history{display:flex;gap:5px;padding:10px;overflow-x:auto}
.crash-history span{background:#1e2142;padding:5px 10px;border-radius:12px;font-size:12px;min-width:45px;text-align:center}
.game-area{height:320px;background:radial-gradient(circle at 30% 70%, #1a1d4a, #0b0e2a);position:relative;border-bottom:2px solid #1e2142;overflow:hidden}
.plane{position:absolute;left:10%;bottom:30%;font-size:40px;transition:all 0.1s;z-index:2}
.multiplier{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:60px;font-weight:900;text-shadow:0 0 20px #ff0040}
.graph{position:absolute;bottom:0;left:0;width:100%;height:70%;}
.bet-area{padding:15px;background:#12152e}
.bet-card{background:#1e2142;border-radius:15px;padding:12px;margin-bottom:10px}
.bet-controls{display:flex;gap:10px;align-items:center;margin:10px 0}
.bet-controls button{width:40px;height:40px;border-radius:10px;border:none;background:#2a2d5a;color:#fff;font-size:20px}
.bet-controls input{flex:1;height:45px;border:none;border-radius:10px;background:#0b0e2a;color:#fff;text-align:center;font-size:18px;font-weight:bold}
.btn-bet{width:100%;height:55px;border:none;border-radius:15px;font-size:18px;font-weight:900;cursor:pointer}
.btn-green{background:#00e676;color:#000}
.btn-red{background:#ff1744;color:#fff}
.btn-yellow{background:#ffea00;color:#000}
.action-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px}
.action-grid button{height:45px;border:none;border-radius:12px;background:#2a2d5a;color:#fff;font-weight:bold}
.crashed{color:#ff1744;animation:shake 0.5s}
@keyframes shake{0%,100%{transform:translate(-50%,-50%)}25%{transform:translate(-53%,-50%)}75%{transform:translate(-47%,-50%)}}
</style>
</head>
<body>
<div class="header">
<div><b>1WIN</b> <small style="color:#888">GHANA</small></div>
<div class="balance" id="balance">100.00 GHS</div>
</div>
<div class="crash-history" id="history"></div>
<div class="game-area" id="gameArea">
<div class="multiplier" id="mult">1.00x</div>
<div class="plane" id="plane">✈️</div>
<canvas class="graph" id="graph"></canvas>
</div>
<div class="bet-area">
<div class="bet-card">
<div style="display:flex;justify-content:space-between"><span>Mise 1</span><span style="color:#00ff88">Auto <input type="checkbox" id="auto1"> <input type="number" id="autoCash1" value="2.0" style="width:50px;background:#0b0e2a;border:none;color:#fff;border-radius:5px;text-align:center"></span></div>
<div class="bet-controls">
<button onclick="changeBet(-10)">-</button>
<input type="number" id="bet1" value="10" min="1">
<button onclick="changeBet(10)">+</button>
</div>
<button class="btn-bet btn-green" id="btn1" onclick="placeBet(1)">MISE 10 GHS</button>
</div>
<div class="bet-card">
<div style="display:flex;justify-content:space-between"><span>Mise 2</span><span style="color:#00ff88">Auto <input type="checkbox" id="auto2"> <input type="number" id="autoCash2" value="3.0" style="width:50px;background:#0b0e2a;border:none;color:#fff;border-radius:5px;text-align:center"></span></div>
<div class="bet-controls">
<button onclick="changeBet2(-10)">-</button>
<input type="number" id="bet2" value="20" min="1">
<button onclick="changeBet2(10)">+</button>
</div>
<button class="btn-bet btn-green" id="btn2" onclick="placeBet(2)">MISE 20 GHS</button>
</div>
<div class="action-grid">
<button onclick="Telegram.WebApp.sendData('deposit')">💳 Recharger</button>
<button onclick="Telegram.WebApp.sendData('withdraw')">💸 Retirer</button>
</div>
</div>

<script>
let tg = window.Telegram.WebApp; tg.expand();
let solde = 100;
let crashPoint = 0;
let curMult = 1.0;
let isFlying = false;
let bet1Active=false, bet2Active=false;
let bet1Amount=0, bet2Amount=0;
let history = [2.34,1.12,5.67,1.01,12.5,1.34,2.10];

function updateBalance(){ document.getElementById('balance').innerText = solde.toFixed(2) + ' GHS'; }
function updateHistory(){
 let h = document.getElementById('history'); h.innerHTML='';
 history.slice(-12).forEach(v=>{
   let c = v<2?'#ff1744': v<5?'#ffea00':'#00e676';
   h.innerHTML += `<span style="color:${c}">${v.toFixed(2)}x</span>`;
 });
}
function changeBet(d){ let i=document.getElementById('bet1'); i.value=Math.max(1, parseInt(i.value||10)+d); updateBetButtons(); }
function changeBet2(d){ let i=document.getElementById('bet2'); i.value=Math.max(1, parseInt(i.value||10)+d); updateBetButtons(); }
function updateBetButtons(){
 if(!bet1Active) document.getElementById('btn1').innerText = 'MISE ' + document.getElementById('bet1').value + ' GHS';
 if(!bet2Active) document.getElementById('btn2').innerText = 'MISE ' + document.getElementById('bet2').value + ' GHS';
}
document.getElementById('bet1').oninput=updateBetButtons;
document.getElementById('bet2').oninput=updateBetButtons;

function placeBet(n){
 if(isFlying) return;
 if(n==1 && !bet1Active){
   let amt=parseFloat(document.getElementById('bet1').value);
   if(solde<amt) return alert('Solde insuffisant');
   solde-=amt; bet1Amount=amt; bet1Active=true;
   document.getElementById('btn1').innerText='CASHOUT '+amt.toFixed(2)+' GHS';
   document.getElementById('btn1').className='btn-bet btn-yellow';
 } else if(n==1 && bet1Active){
   cashout(1);
 } else if(n==2 && !bet2Active){
   let amt=parseFloat(document.getElementById('bet2').value);
   if(solde<amt) return alert('Solde insuffisant');
   solde-=amt; bet2Amount=amt; bet2Active=true;
   document.getElementById('btn2').innerText='CASHOUT '+amt.toFixed(2)+' GHS';
   document.getElementById('btn2').className='btn-bet btn-yellow';
 } else if(n==2 && bet2Active){
   cashout(2);
 }
 updateBalance();
 if(!isFlying) startRound();
}

function cashout(n){
 if(!isFlying) return;
 if(n==1 && bet1Active){
   let win = bet1Amount * curMult;
   solde+=win; bet1Active=false;
   document.getElementById('btn1').innerText='Gagné '+win.toFixed(2)+' GHS';
   document.getElementById('btn1').className='btn-bet btn-green';
   setTimeout(updateBetButtons,1000);
 } else if(n==2 && bet2Active){
   let win = bet2Amount * curMult;
   solde+=win; bet2Active=false;
   document.getElementById('btn2').innerText='Gagné '+win.toFixed(2)+' GHS';
   document.getElementById('btn2').className='btn-bet btn-green';
   setTimeout(updateBetButtons,1000);
 }
 updateBalance();
}

function getCrash(){
 let r=Math.random();
 if(r<0.07) return 1.0 + Math.random()*0.3;
 if(r<0.5) return 1.0 + Math.random()*2;
 if(r<0.85) return 2 + Math.random()*5;
 return 5 + Math.random()*20;
}

function startRound(){
 if(isFlying) return;
 crashPoint=getCrash();
 curMult=1.0; isFlying=true;
 document.getElementById('mult').classList.remove('crashed');
 document.getElementById('mult').style.color='#fff';
 let start=Date.now();
 let plane=document.getElementById('plane');
 let graph=document.getElementById('graph');
 let ctx=graph.getContext('2d');
 graph.width=graph.offsetWidth; graph.height=graph.offsetHeight;
 let points=[];

 function loop(){
   let elapsed=(Date.now()-start)/1000;
   curMult = Math.pow(1.08, elapsed*2);
   if(curMult>=crashPoint){
     curMult=crashPoint;
     isFlying=false;
     document.getElementById('mult').innerText='CRASHED '+curMult.toFixed(2)+'x';
     document.getElementById('mult').classList.add('crashed');
     document.getElementById('mult').style.color='#ff1744';
     history.push(crashPoint); updateHistory();
     if(bet1Active){
       bet1Active=false;
       document.getElementById('btn1').innerText='PERDU';
       document.getElementById('btn1').className='btn-bet btn-red';
       setTimeout(updateBetButtons,1000);
     }
     if(bet2Active){
       bet2Active=false;
       document.getElementById('btn2').innerText='PERDU';
       document.getElementById('btn2').className='btn-bet btn-red';
       setTimeout(updateBetButtons,1000);
     }
     setTimeout(startRound,3000);
     return;
   }
   document.getElementById('mult').innerText=curMult.toFixed(2)+'x';
   let progress=Math.min(curMult/10,1);
   plane.style.left=(10+progress*70)+'%';
   plane.style.bottom=(30+progress*40)+'%';
   // auto cashout
   if(bet1Active && document.getElementById('auto1').checked){
     let target=parseFloat(document.getElementById('autoCash1').value);
     if(curMult>=target) cashout(1);
   }
   if(bet2Active && document.getElementById('auto2').checked){
     let target=parseFloat(document.getElementById('autoCash2').value);
     if(curMult>=target) cashout(2);
   }
   // graph
   points.push({x:progress*graph.width, y:graph.height - progress*graph.height*0.8});
   if(points.length>100) points.shift();
   ctx.clearRect(0,0,graph.width,graph.height);
   ctx.beginPath(); ctx.strokeStyle='#ff0040'; ctx.lineWidth=3;
   points.forEach((p,i)=>{ if(i==0) ctx.moveTo(p.x,p.y); else ctx.lineTo(p.x,p.y); });
   ctx.stroke();
   requestAnimationFrame(loop);
 }
 loop();
}

updateBalance(); updateHistory(); updateBetButtons();
setTimeout(startRound,2000);
</script>
</body>
</html>