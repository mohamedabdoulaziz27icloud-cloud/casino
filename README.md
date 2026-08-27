<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>1WIN GHANA - CASINO PRO</title>
<script src="https://telegram.org/js/telegram-web-app.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial}
body{background:#0a0e1a;color:#fff}
.header{background:linear-gradient(90deg,#00d1ff,#0066ff);padding:12px;display:flex;justify-content:space-between;align-items:center}
.balance{background:#0008;padding:8px 16px;border-radius:20px;font-weight:bold}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:12px}
.game{background:#151b2e;border-radius:12px;padding:16px;text-align:center;border:1px solid #2a3555;cursor:pointer}
.game .icon{font-size:36px;margin-bottom:6px}
.game h3{font-size:13px}
.hot{border-color:#ffcc00;box-shadow:0 0 10px #ffcc0044}
#playArea{padding:12px;display:none}
.btn{background:linear-gradient(90deg,#00d1ff,#0066ff);border:none;color:#fff;padding:12px 24px;border-radius:8px;font-weight:bold;width:100%;margin:6px 0}
.mult{font-size:42px;font-weight:bold;text-align:center;margin:20px 0;color:#00ff88}
.canvasWrap{background:#000;border-radius:12px;height:200px;position:relative;overflow:hidden;margin:10px 0}
.mines-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin:10px 0}
.mine{aspect-ratio:1;background:#1e2a4a;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:20px;cursor:pointer}
.mine.open{background:#00ff8855}
.mine.bomb{background:#ff004455}
input{width:100%;padding:12px;border-radius:8px;border:1px solid #333;background:#111;color:#fff;margin:8px 0}
</style>
</head>
<body>
<div class="header">
<div><b>1WIN GHANA</b> 🇬🇭</div>
<div class="balance" id="bal">100.00 GHS</div>
</div>
<div id="lobby">
<div style="padding:10px"><b>🔥 1XBET / 1WIN - 8 JEUX</b></div>
<div class="grid">
<div class="game hot" onclick="openGame('aviator')"><div class="icon">✈️</div><h3>AVIATOR</h3></div>
<div class="game hot" onclick="openGame('crash')"><div class="icon">📈</div><h3>CRASH</h3></div>
<div class="game" onclick="openGame('mines')"><div class="icon">💣</div><h3>MINES</h3></div>
<div class="game" onclick="openGame('dice')"><div class="icon">🎲</div><h3>DICE</h3></div>
<div class="game" onclick="openGame('plinko')"><div class="icon">🔴</div><h3>PLINKO</h3></div>
<div class="game" onclick="openGame('roulette')"><div class="icon">🎰</div><h3>ROULETTE</h3></div>
<div class="game" onclick="openGame('wheel')"><div class="icon">🎡</div><h3>WHEEL</h3></div>
<div class="game" onclick="openGame('slots')"><div class="icon">🍒</div><h3>SLOTS</h3></div>
</div>
</div>
<div id="playArea">
<button class="btn" onclick="closeGame()" style="background:#333">← RETOUR</button>
<div id="gameContent"></div>
</div>
<script>
let tg=window.Telegram.WebApp; tg.expand();
let solde=parseFloat(localStorage.getItem('solde')||'100');
let enJeu=false; let mise=10; let mult=1; let crashPoint=0; let currentGame='lobby';
function updateBal(){document.getElementById('bal').innerText=solde.toFixed(2)+' GHS'; localStorage.setItem('solde',solde)}
function syncToBot(type, amount){
  currentGame=currentGame;
  if(window.Telegram && Telegram.WebApp && Telegram.WebApp.sendData){
    try{Telegram.WebApp.sendData(JSON.stringify({action:type,amount:amount,game:currentGame}))}catch(e){}
  }
}
function openGame(name){
currentGame=name; document.getElementById('lobby').style.display='none';
document.getElementById('playArea').style.display='block';
if(name==='aviator') renderAviator();
if(name==='crash') renderCrash();
if(name==='mines') renderMines();
if(name==='dice') renderDice();
if(name==='plinko') renderPlinko();
if(name==='roulette') renderRoulette();
if(name==='wheel') renderWheel();
if(name==='slots') renderSlots();
}
function closeGame(){document.getElementById('playArea').style.display='none';document.getElementById('lobby').style.display='block'; enJeu=false}

function renderAviator(){
document.getElementById('gameContent').innerHTML=`
<h2>✈️ AVIATOR</h2>
<input id="miseA" type="number" value="10"><div class="canvasWrap"><div id="plane" style="position:absolute;left:20px;bottom:20px;font-size:30px">✈️</div><div class="mult" id="multA">1.00x</div></div>
<button class="btn" id="btnA" onclick="playAviator()">MISER 10 GHS</button>
<button class="btn" id="cashA" style="display:none;background:#00ff88;color:#000" onclick="cashAviator()">CASHOUT</button>`;
}
function playAviator(){
let m=parseFloat(document.getElementById('miseA').value)||10;
if(solde<m){alert('Solde insuffisant');return}
solde-=m; updateBal(); syncToBot('bet',m); mise=m; enJeu=true;
crashPoint=1+Math.random()*4+Math.random()*6; if(Math.random()<0.2) crashPoint=1+Math.random()*0.5;
let cur=1; document.getElementById('btnA').style.display='none'; document.getElementById('cashA').style.display='block';
let iv=setInterval(()=>{
if(!enJeu){clearInterval(iv);return}
cur+=0.05+cur*0.02; document.getElementById('multA').innerText=cur.toFixed(2)+'x';
document.getElementById('cashA').innerText=`CASHOUT ${cur.toFixed(2)}x ${(mise*cur).toFixed(2)} GHS`;
document.getElementById('plane').style.left=(20+cur*20)+'px';
document.getElementById('plane').style.bottom=(20+cur*15)+'px'; mult=cur;
if(cur>=crashPoint){clearInterval(iv); enJeu=false; document.getElementById('multA').innerText=`CRASH ${crashPoint.toFixed(2)}x`; document.getElementById('multA').style.color='#ff0044'; document.getElementById('cashA').style.display='none'; document.getElementById('btnA').style.display='block';}
},100)
}
function cashAviator(){
if(!enJeu) return; let gain=mise*mult; solde+=gain; updateBal(); syncToBot('win',gain); enJeu=false;
document.getElementById('multA').innerText=`GAGNE ${gain.toFixed(2)} GHS`; document.getElementById('multA').style.color='#00ff88';
document.getElementById('cashA').style.display='none'; document.getElementById('btnA').style.display='block';
}
function renderMines(){
document.getElementById('gameContent').innerHTML=`<h2>💣 MINES</h2><input id="miseM" type="number" value="10"><div class="mines-grid" id="gridM"></div><button class="btn" onclick="startMines()">COMMENCER</button><div id="infoM"></div>`;
startMines();
}
function startMines(){
let grid=document.getElementById('gridM'); grid.innerHTML=''; let bombPos=new Set(); while(bombPos.size<3){bombPos.add(Math.floor(Math.random()*25))}
let miseM=parseFloat(document.getElementById('miseM').value)||10;
for(let i=0;i<25;i++){
let d=document.createElement('div'); d.className='mine'; d.innerText='?';
d.onclick=()=>{
if(d.classList.contains('open')) return;
if(bombPos.has(i)){d.classList.add('bomb'); d.innerText='💣'; document.getElementById('infoM').innerText='BOOM Perdu '+miseM; solde-=miseM; updateBal(); syncToBot('bet',miseM); setTimeout(startMines,1200)}
else{d.classList.add('open'); d.innerText='💎'; let gain=miseM*1.3; document.getElementById('infoM').innerHTML=`Gain ${gain.toFixed(2)} <button class='btn' onclick='solde+=${gain};updateBal();syncToBot("win",${gain});document.getElementById("infoM").innerText="Gagne ${gain}"'>CASHOUT</button>`}
}; grid.appendChild(d);
}
}
function renderDice(){
document.getElementById('gameContent').innerHTML=`<h2>🎲 DICE</h2><input id="miseD" type="number" value="10"><button class="btn" onclick="playDice('low')">< 50 x1.98</button><button class="btn" onclick="playDice('high')">> 50 x1.98</button><div class="mult" id="resD">--</div>`;
}
function playDice(side){
let miseD=parseFloat(document.getElementById('miseD').value)||10; if(solde<miseD) return; solde-=miseD; updateBal(); syncToBot('bet',miseD);
let roll=Math.floor(Math.random()*100)+1; let win=(side==='low'&&roll<50)||(side==='high'&&roll>50);
document.getElementById('resD').innerText=roll;
if(win){let g=miseD*1.98; solde+=g; syncToBot('win',g); document.getElementById('resD').innerText+=` WIN ${g.toFixed(2)}`} else document.getElementById('resD').innerText+=' LOSE'; updateBal();
}
function renderPlinko(){
document.getElementById('gameContent').innerHTML=`<h2>🔴 PLINKO</h2><input id="miseP" type="number" value="10"><button class="btn" onclick="playPlinko()">LACHER</button><div class="mult" id="resP">--</div>`;
}
function playPlinko(){
let m=parseFloat(document.getElementById('miseP').value)||10; if(solde<m) return; solde-=m; updateBal(); syncToBot('bet',m);
let multis=[0.2,0.5,1,1.5,3,1.5,1,0.5,0.2]; let pick=multis[Math.floor(Math.random()*multis.length)];
let gain=m*pick; solde+=gain; syncToBot('win',gain); document.getElementById('resP').innerText=`x${pick} = ${gain.toFixed(2)}`; updateBal();
}
function renderRoulette(){
document.getElementById('gameContent').innerHTML=`<h2>🎰 ROULETTE</h2><input id="miseR" type="number" value="10"><div style="display:flex;gap:6px"><button class="btn" style="background:red" onclick="playRoulette('red')">ROUGE x2</button><button class="btn" style="background:#000" onclick="playRoulette('black')">NOIR x2</button><button class="btn" style="background:green" onclick="playRoulette('green')">0 x14</button></div><div class="mult" id="resR">--</div>`;
}
function playRoulette(c){
let m=parseFloat(document.getElementById('miseR').value)||10; if(solde<m) return; solde-=m; updateBal(); syncToBot('bet',m);
let r=Math.random(); let res=r<0.027?'green':(r<0.513?'red':'black');
document.getElementById('resR').innerText=res.toUpperCase();
if(res===c){let mult=c==='green'?14:2; let gain=m*mult; solde+=gain; syncToBot('win',gain); document.getElementById('resR').innerText+=` WIN ${gain}`} else document.getElementById('resR').innerText+=' LOSE'; updateBal();
}
function renderWheel(){
document.getElementById('gameContent').innerHTML=`<h2>🎡 WHEEL</h2><input id="miseW" type="number" value="10"><button class="btn" onclick="playWheel()">TOURNER</button><div class="mult" id="resW">--</div>`;
}
function playWheel(){
let m=parseFloat(document.getElementById('miseW').value)||10; if(solde<m) return; solde-=m; updateBal(); syncToBot('bet',m);
let segs=[0,0.2,0.5,1,2,5,10,50]; let s=segs[Math.floor(Math.random()*segs.length)];
let gain=m*s; solde+=gain; if(s>0) syncToBot('win',gain); document.getElementById('resW').innerText=`x${s} = ${gain.toFixed(2)}`; updateBal();
}
function renderSlots(){
document.getElementById('gameContent').innerHTML=`<h2>🍒 SLOTS</h2><input id="miseS" type="number" value="10"><button class="btn" onclick="playSlots()">SPIN</button><div class="mult" id="resS" style="font-size:40px">🍒 | 🍋 | 🔔</div>`;
}
function playSlots(){
let m=parseFloat(document.getElementById('miseS').value)||10; if(solde<m) return; solde-=m; updateBal(); syncToBot('bet',m);
let sym=['🍒','🍋','🔔','💎','7️⃣']; let a=sym[Math.floor(Math.random()*sym.length)]; let b=sym[Math.floor(Math.random()*sym.length)]; let c=sym[Math.floor(Math.random()*sym.length)];
document.getElementById('resS').innerText=`${a} | ${b} | ${c}`;
if(a===b&&b===c){let gain=m*(a==='7️⃣'?100:10); solde+=gain; syncToBot('win',gain); document.getElementById('resS').innerText+=` JACKPOT ${gain}`;}
else if(a===b||b===c||a===c){let gain=m*2; solde+=gain; syncToBot('win',gain); document.getElementById('resS').innerText+=` WIN ${gain}`} updateBal();
}
function renderCrash(){renderAviator(); document.querySelector('#gameContent h2').innerText='📈 CRASH x1000';}
updateBal();
</script>
</body>
</html>
