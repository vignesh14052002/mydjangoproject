let x,y,i,j,a;
let windowWidth=355,windowHeight=300;
//let size=document.getElementById("myRange").value;
let size=50;
function setup() {
  let canvas = createCanvas(windowWidth, windowHeight);
  canvas.parent('sketch-container');
 x=windowWidth/2,y= windowHeight/2,i=12,j=20,a=1;
}

function draw() {
   background(0);
  if (x<size/2 || x>windowWidth-size/2){i=-i;a=1}
  if (y<size/2 || y>windowHeight-size/2){j=-j;a=1}
  x+=i*a
  y+=j*a
   ellipse(x,y, size, size);
   fill('#07C');
   noStroke();
}

function windowResized() {
   resizeCanvas(windowWidth, windowHeight);
}

//document.getElementById("myRange").oninput = 
/*let aa={slider}
function slider(){
    //myFunction()
    size=document.getElementById("myRange").value;
  console.log(size)
}
*/