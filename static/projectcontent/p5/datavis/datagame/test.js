let d;
d3.csv("./programminglanguage.csv").then((da)=>{d=da});
let i=-1;
let p=document.getElementById("date")
function plot() {
	i++;
	i=i%d.length;

	let val=range.value;
	let data=d[i]
	let date=data.Date
	delete data.Date
	p.innerText=date
	var q=d3.select("svg")
	.selectAll("rect")
	.data(Object.keys(data))
	q.join("text")
	.text((da)=>da)
	.attr("x",90)
	.attr("y",(d,i)=>i*10)
	.attr("style",`font-size:10px;text-anchor:end`)
	q.join("rect")
	.attr("width",(da)=>data[da]*3)
	.attr("height",(d,i)=>10)
	.attr("y",(d,i)=>i*10)
	.attr("x",100)
	.on("mouseenter",function k(){
		d3.select(this)
		.attr("fill","green");
		console.log("yes")
	});
}

const range=document.getElementById('myrange')
range.onclick=plot; 
//setInterval(plot,100)
//plot()