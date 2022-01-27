
const d=[12,15,13,21,14,26,12,13,15]
const k=[...d] 
const scroll=document.getElementById('myrange')
scroll.onclick=demo;
const split=document.getElementById('split')
split.onclick=dosplit;
let x=500
let y=100
let i=1;
function dosplit(){
	const v=d.pop(0);
	console.log(v,d);
}
function update(){
const value=scroll.value;
for (let i = 0; i < d.length; i++) {
	d[i]=k[i]+Math.round(value);
}
console.log(d[0])

}
function demo(){
	update()
	y=100;
	i=1;
var q=d3.select("svg")
 	.selectAll("circle")
 	.data(d)
 	.join("circle").attr("r",da=>da)
	.attr("transform",da=>{
		let s= `translate(${x},${y})`
		y+=d[i];
		y+=d[i-1];
		if(i<d.length-1)i++;
		console.log(da,d[i-1],s);
		return s
	});
}
function exec() { 
	update()
	y=100;
	i=1;
	var u=d3.select("svg")
 	.selectAll("circle")
 	.data(d);
	u.exit().remove();
	u.enter().merge(u).attr("r",da=>da)
	.attr("transform",da=>{
		let s= `translate(${x},${y})`
		y+=d[i];
		y+=d[i-1];
		if(i<d.length-1)i++;
		console.log(da,d[i-1],s);
		return s
	})
	; 
	
}
   




  //  var div = d3
  //               .select("body")
  //               .selectAll("div")
  //               .data(["geeks", "for", "geeks"])
  //               // Old dataset
  //               .enter()
  //               .append("div")
  //               .text(function (d) {
  //                   return d;
  //               });
  
  // function h(){
  //           div = div.data(["DIVS UPDATED", "GEEKS", 
  //                           "FOR", "GEEKS"], function (d) {
  //               return d;
  //           }); //Updated new data set.
  //           div.exit().remove();
  //           div.enter()
  //               .append("div")
  //               .text(function (d) {
  //                   return d;
  //               });
            
  //       }