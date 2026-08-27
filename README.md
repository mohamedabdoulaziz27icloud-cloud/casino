<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>1WIN Ghana</title>
<script src="https://telegram.org/js/telegram-web-app.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial}
body{background:#0b0e2a;color:#fff}
.header{background:#12152e;padding:12px;display:flex;justify-content:space-between}
.balance{background:#1e2142;padding:8px 15px;border-radius:20px;color:#00ff88;font-weight:bold}
.game{height:300px;background:radial-gradient(circle,#1a1d4a,#0b0e2a);position:relative;display:flex;align-items:center;justify-content:center}
.mult{font-size:55px;font-weight:900}
.bet{padding:15px;background:#12152e}
.card{background:#1e2142;border-radius:15px;padding:12px;margin-bottom:10px}
input{width:100%;height:45px;background:#0b0e2a;border:none;color:#fff;text-align:center;border-radius:10px;font-size:18px;margin:10px 0}
.btn{width:100%;height:55px;border:none;border-radius:15px;font-weight:900;font-size:18px}
.green{background:#00e676} .yellow{background:#ffea00} .red{background:#ff1744;color:#fff}
</style>
</head>
<body>
<div class="header"><b>1WIN GHANA</b><div class="balance" id="bal">100.00 GHS</div></div>
<div class="game"><div class="mult" id="mult">1.00x</div></div>
<div class="bet">
<div class="card">
<input type="number" id="bet" value="10">
<button class="btn green" id="btn" onclick="bet()">MISE 10 GHS</button>
</div>
<button onclick="Telegram.WebApp.sendData('deposit')" style="width:48%;height:40px;border:none;border-radius:10px;background:#2a2d5a;color:#fff">Recharger</button>
<button onclick="Telegram.WebApp.sendData('withdraw')" style="width:48%;height:40px;border:none;border-radius:10px;background:#2a2d5a;color:#fff">Retirer</button>
</div>
<script>
let tg=Telegram.WebApp;tg.expand();
let solde=100, crash=0, cur=1, flying=false, mise=0, active=false;
let bal=document.getElementById('bal'), mult=document.getElementById('mult'), btn=document.getElementById('btn');
function upd(){bal.innerText=solde.toFixed(2)+' GHS';}
function getCrash(){let r=Math.random(); if(r<0.1)return 1+Math.random(); if(r<0.6)return 1+Math.random()*3; return 3+Math.random()*10;}
function bet(){
 if(!flying && !active){
  mise=parseFloat(document.getElementById('bet').value);
  if(solde<mise)return alert('Solde insuffisant');
  solde-=mise; active=true; btn.innerText='En attente...'; btn.className='btn yellow'; upd();
  if(!flying)start();
 }else if(active && flying){ 
  let win=mise*cur; solde+=win; active=false; btn.innerText='Gagné '+win.toFixed(2); btn.className='btn green'; setTimeout(()=>{btn.innerText='MISE '+document.getElementById('bet').value+' GHS'},1000); upd();
 }
}
function start(){
 crash=getCrash(); cur=1; flying=true; mult.style.color='#fff'; mult.innerText='1.00x';
 let t=Date.now();
 function loop(){
  let e=(Date.now()-t)/1000; cur=Math.pow(1.09, e*2);
  if(cur>=crash){cur=crash; flying=false; mult.innerText='CRASH '+crash.toFixed(2)+'x'; mult.style.color='red';
   if(active){active=false; btn.innerText='PERDU'; btn.className='btn red'; setTimeout(()=>{btn.innerText='MISE '+document.getElementById('bet').value+' GHS'; btn.className='btn green'},1000);}
   setTimeout(start,2000); return;
  }
  mult.innerText=cur.toFixed(2)+'x';
  if(active){btn.innerText='CASHOUT '+ (mise*cur).toFixed(2)+' GHS ('+cur.toFixed(2)+'x)';}
  requestAnimationFrame(loop);
 }
 loop();
}
document.getElementById('bet').oninput=()=>{if(!active)btn.innerText='MISE '+document.getElementById('bet').value+' GHS';}
upd(); setTimeout(start,1000);
</script>
</body>
</html>
