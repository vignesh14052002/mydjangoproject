let pixelsWidth = 300;
let pixelsHeight = 300;
let finalWidth = 1000;
let finalHeight = 1000;
let tempCanvas = document.createElement('canvas');
let tempContext = tempCanvas.getContext('2d');
tempCanvas.width = pixelsWidth;
tempCanvas.height = pixelsHeight;
let pixelData;
let img = new Image();
img.crossOrigin = 'anonymous';
img.onload = (e) => {
  let scale = e.target.naturalWidth >= e.target.naturalHeight ? pixelsWidth / e.target.naturalWidth : pixelsHeight / e.target.naturalHeight;
  let tempWidth = e.target.naturalWidth * scale;
  let tempHeight = e.target.naturalHeight * scale;
  tempContext.drawImage(e.target,0,0, tempWidth, tempHeight);
  pixelData = tempContext.getImageData(0, 0, pixelsWidth, pixelsHeight);
  redraw();
}
img.src = './flower.jpg';

function redraw() {
  let canvas = document.getElementById('mycanvas');
  let context = canvas.getContext('2d');
  canvas.width = finalWidth;
  canvas.height = finalHeight;
  tempContext.putImageData(pixelData, 0, 0);
  context.drawImage(tempCanvas, 0, 0, finalWidth, finalHeight);}
