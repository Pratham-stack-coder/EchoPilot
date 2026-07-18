async function refresh(){
const r=await fetch('/stats'); const d=await r.json();
cpu.textContent=d.cpu+'%'; ram.textContent=d.ram+'%'; disk.textContent=d.disk+'%';
battery.textContent=d.battery; time.textContent=d.time;
}
async function openChrome(){await fetch('/open/chrome',{method:'POST'});}
setInterval(refresh,1000); refresh();
