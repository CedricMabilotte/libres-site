(function(){var a=document.getElementById("x-a"),b=document.getElementById("x-b"),o=document.getElementById("x-sortie");if(!a)return;
fetch("../donnees/analyses.json").then(function(r){return r.json()}).then(function(A){var V=A.variables,ks=Object.keys(V).sort(function(x,y){return V[x].localeCompare(V[y],"fr")});
ks.forEach(function(k){[a,b].forEach(function(s){var e=document.createElement("option");e.value=k;e.textContent=V[k];s.appendChild(e)})});a.value="famille";b.value="P2";
function esc(t){return String(t).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function lib(x){return esc(String(x).replace(/_/g," "))}
function go(){var k=a.value+"|"+b.value,inv=false,c=A.paires[k];if(!c){c=A.paires[b.value+"|"+a.value];inv=true}
if(a.value===b.value){o.innerHTML="<p class=petit>Choisissez deux dimensions différentes.</p>";return}
if(!c){o.innerHTML="<p class=petit>Croisement non calculé : effectif insuffisant, ou variables liées par construction.</p>";return}
var L=inv?c.table.colonnes:c.table.lignes,C=inv?c.table.lignes:c.table.colonnes,T=c.table.valeurs,g=function(i,j){return inv?T[j][i]:T[i][j]};
var h="<table class=croise><caption class=petit>"+esc(V[a.value])+" × "+esc(V[b.value])+" — n = "+c.n+", V = "+c.v.toFixed(2)+", p = "+c.p.toFixed(3)+(c.mecanique?" — association attendue par construction":"")+(c.fragile?" — tableau creux : lecture prudente":"")+"</caption><thead><tr><th></th>";
C.forEach(function(x){h+="<th class=n>"+lib(x)+"</th>"});h+="<th class=n>total</th></tr></thead><tbody>";
L.forEach(function(x,i){var tot=0;C.forEach(function(_,j){tot+=g(i,j)});h+="<tr><th scope=row>"+lib(x)+"</th>";C.forEach(function(_,j){var v=g(i,j),pc=tot?Math.round(100*v/tot):0;h+="<td class=n>"+v+"<span class=bar style='width:"+pc+"%'></span></td>"});h+="<td class=n>"+tot+"</td></tr>"});
o.innerHTML=h+"</tbody></table><p class=petit>Barre : part de la ligne.</p>"}
a.addEventListener("change",go);b.addEventListener("change",go);go()}).catch(function(){o.textContent="Croisements indisponibles."})})();
