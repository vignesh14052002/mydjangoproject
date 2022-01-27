let width=1000;      //canvas width
let height=1000;    //canvas height
let img_w=100;      //image width
let img_h=100;      //image height
let img=new Image();
img.width=img_w
img.height=img_h
img.src="./flower.jpg"
var canvas = document.getElementById('mycanvas');
var context = canvas.getContext('2d');
canvas.width = img_w;
canvas.height = img_h;
let pixels,scannedimg;
img.onload=()=>{
context.drawImage(img, 0, 0,img_w,img_h );
scannedimg = context.getImageData(0, 0, img.width, img.height);
pixels=scannedimg.data
console.log(pixels)
canvas.width = width;
canvas.height = height;

redraw();
}

let row=4*img_w;
let col=img_h;

function redraw(){
    for(let i=0;i<row;i+=4){
        for(let j=0;j<col;j++){
            pixels[i+j*row]=0;
            pixels[i+j*row+1]=0;
            pixels[i+j*row+2]=0;
            //pixels[i+j*400+3]=0;
        }
    }
   scannedimg.data=pixels;
    console.log(scannedimg);
    context.putImageData(scannedimg,0,0);
    context.drawImage(canvas, 0, 0,width,height );
}