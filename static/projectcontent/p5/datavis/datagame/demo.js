const f=d3.image("./flower.jpg")
let gr=200
let a=[{x:gr,y:gr,r:gr}]
function h(){
d3.select("svg")
.selectAll("circle")
.data(a)
.join("circle")
.attr("r",(d)=>d.r)
.attr("cx",(d)=>d.x)
.attr("cy",(d)=>d.y)
.attr("fill",(d)=>{
	const x=Math.round(d.x*(50/gr));
	const y=Math.round(d.y*(50/gr));
	return `rgba(${pixels[400*y+x*4]},${pixels[400*y+x*4+1]},${pixels[400*y+x*4+2]},${pixels[400*y+x*4+3]})`
})
.on("mouseenter",function g(aa,b) {
	//d3.select(this).remove()
	const nr=b.r/2;
	if(nr>1){
	let f;
	const re = a.some( function(d,i){f=i;return d.x == b.x && d.y==b.y} );
	a.splice(f,1)
	a.push({x:b.x+nr,y:b.y+nr,r:nr})
	a.push({x:b.x+nr,y:b.y-nr,r:nr})
	a.push({x:b.x-nr,y:b.y+nr,r:nr})
	a.push({x:b.x-nr,y:b.y-nr,r:nr})
	//console.log(b)
	h()
}
})
}
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