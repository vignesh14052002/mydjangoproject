let i=0;
const f=d3.image("./flower.jpg")
let gr=300
let a=[{id:i,x:gr,y:gr,r:gr,parent:{id:-1,x:0,y:0,r:0}}]
function h(){
var q=d3.select("svg")
.selectAll("circle")
.data(a,(d)=>d.id)
.join("circle")
.attr("cx",(d)=>d.parent.x)
.attr("cy",(d)=>d.parent.y)
.attr("r",(d)=>d.parent.r);
const t = d3.transition()
    .duration(20);
q.transition(t)
.attr("r",(d)=>d.r)
.attr("cx",(d)=>d.x)
.attr("cy",(d)=>d.y)
.attr("fill",(d)=>{
	delete d.parent
	d.parent=d;
	const x=Math.round(d.x*(50/gr));
	const y=Math.round(d.y*(50/gr));
	return `rgba(${pixels[400*y+x*4]},${pixels[400*y+x*4+1]},${pixels[400*y+x*4+2]},${pixels[400*y+x*4+3]})`
});
setTimeout(()=>{
q.on("mouseenter",function g(aa,b) {
	// //
	// d3.select(this).enter()
	// d3.select(this).remove()
	const nr=b.r/2;
	if(nr>1){
	let f;
	const re = a.some( function(d,i){f=i;return d.x == b.x && d.y==b.y} );
	a.splice(f,1)
	a.push({id:i++,x:b.x+nr,y:b.y+nr,r:nr,parent:b})
	a.push({id:i++,x:b.x+nr,y:b.y-nr,r:nr,parent:b})
	a.push({id:i++,x:b.x-nr,y:b.y+nr,r:nr,parent:b})
	a.push({id:i++,x:b.x-nr,y:b.y-nr,r:nr,parent:b})
	//console.log(b)
	h()
}
})
},50)}

let img=new Image();
img.width=100
img.height=100
img.src="./flower.jpg"
var canvas = document.createElement('canvas');
var context = canvas.getContext('2d');
canvas.width = img.width;
canvas.height = img.height;
let pixels;
img.onload=()=>{
context.drawImage(img, 0, 0,100,100 );
pixels = context.getImageData(0, 0, img.width, img.height).data;
h();}