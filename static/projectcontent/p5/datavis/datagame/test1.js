let width=1000;      //canvas width
let height=1000;    //canvas height
let img_w=1000;      //image width
let img_h=1000;      //image height
let img=new Image();
img.width=img_w
img.height=img_h
img.src="./flower.jpg"
var canvas = document.getElementById('mycanvas');
var context = canvas.getContext('2d');
canvas.width = width;
canvas.height = height;
let pixels,scannedimg;
img.onload=()=>{
context.drawImage(img, 0, 0,width,height );
scannedimg = context.getImageData(0, 0, img.width, img.height);
pixels=scannedimg.data
console.log(pixels)
redraw();
}

let row=4*img_w;
let col=img_h;

let f=0;
let i=0,j=0;
function redraw(){
    if(f==1){
        for(let i=0;i<row;i+=4){
        
            colsort(i,j,0,f);
            colsort(i,j,1,f);
            colsort(i,j,2,f);
            colsort(i,j,3,f);
        }
}else{
    for(let j=0;j<col-1;j++){
    colsort(i,j,0,f);
    colsort(i,j,1,f);
    colsort(i,j,2,f);
    colsort(i,j,3,f);
}

}
   scannedimg.data=pixels;
    console.log(1);
    context.putImageData(scannedimg,0,0,0,0,width,height);
    if(f==0){
        if(i<row){
        i+=4;
        setTimeout(redraw,20)
    }
}else{
    
    if(j<col){
        j++;
        setTimeout(redraw,20)
}
}
}
function colsort(i,j,off,f){
    let v=pixels[i+j*row+off];
    let mi=i,mj=j;
    if(f==1){
    for(let k=j+1;k<col;k++){
        if(pixels[i+k*row+off]<v){
            mi=i;
            mj=k;
            v=pixels[i+k*row+off];
        }
    }
}else{
    for(let k=i+4;k<row;k+=4){
        if(pixels[k+j*row+off]>v){
            mi=k;
            mj=j;
            v=pixels[k+j*row+off];
        }
    }
}
    let temp=pixels[i+j*row+off];
    pixels[i+j*row+off]=pixels[mi+mj*row+off];
    pixels[mi+mj*row+off]=temp;
}
