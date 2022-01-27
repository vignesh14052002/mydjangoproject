var mymap = L
  .map('map')
  .setView([50, -0.1], 1);

  L.tileLayer(
    'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
    maxZoom: 12,
    }).addTo(mymap);

    // Add a svg layer to the map
L.svg().addTo(mymap);

// Create data for circles:
var markers = [
  {long: 9.083, lat: 42.149}, // corsica
  {long: 7.26, lat: 43.71}, // nice
  {long: 2.349, lat: 48.864}, // Paris
  {long: -1.397, lat: 43.664}, // Hossegor
  {long: 3.075, lat: 50.640}, // Lille
  {long: -3.83, lat: 48}, // Morlaix
];
d3.json("./data.json",(d)=>{
  h(d);
})
// Select the svg area and add circles:
function h(data){
  console.log(data)
  let q=d3.select("#map")
    .select("svg")
    .selectAll("myCircles")
    .data(data)
    .enter()
    .append("circle")
      .attr("cx", function(d){ return mymap.latLngToLayerPoint([d.lat, d.lon]).x })
      .attr("cy", function(d){ return mymap.latLngToLayerPoint([d.lat, d.lon]).y })
      .attr("r", 14)
      q.style("fill", "red")
      .attr("class","normal")
      .attr("stroke", "red")
      .attr("stroke-width", 3)
      .attr("fill-opacity", .4)
      q.on("mousemove",function(d){
        console.log("enter")
        return d3.select(this).attr("class","hover")
      })
}
// Function that update circle position if something change
function update() {
  d3.selectAll("circle")
    .attr("cx", function(d){ return mymap.latLngToLayerPoint([d.lat, d.lon]).x })
    .attr("cy", function(d){ return mymap.latLngToLayerPoint([d.lat, d.lon]).y })
}

// If the user change the map (zoom or drag), I update circle position:
mymap.on("moveend", update)

// import { OpenStreetMapProvider } from 'leaflet-geosearch';

// const provider = new OpenStreetMapProvider();
