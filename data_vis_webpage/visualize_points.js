
var fill = d3.scale.category10();



var url = "http://127.0.0.1:5300/api/points"; // "http://theossrv2.epfl.ch/aiida_assignment2/api/points/";
var old =d3.json(url, function (json) {

  var vis = d3.select("#chart")
      .append("svg:svg")
      .attr("width", json.range.max_x)
      .attr("height", json.range.max_y);

  var allCircles = [];
  for (i = 0; i < json.circles.length; i++) {
    allCircles.push(json.circles[i]);

      vis.selectAll("circle")
        .data(allCircles)
        .enter().append("svg:circle")
        .attr("cx", json.circles[i].x )
        .attr("cy", json.circles[i].y )
        .attr("r", 10)
        .style("fill", function(d) { return fill(d.id); })
        .style("stroke", 'black')
        .style("stroke-width", 3)

   }; 

});
var n=0;
var t=1;
function updateData() {
  
  n++;
  console.log(n);
  old = d3.select("circle");
  if (n<4) {
  d3.selectAll("circle").style("opacity", function(d) { t= 1-0.25*n; return t});
  } else if (n==4){
       t=n;
         for (i = 0; i < t; i++) {
      for (j = 0; j < t; j++) {
      d3.select("circle").remove()
      d3.select("circle").remove()
      console.log("eccomi")
      location.href=location.href
     };

     };
   
  }
  
  d3.json(url, function (json) {
  
  var vis = d3.select("#chart")
      .selectAll("svg")
      .append("svg:svg")
      .attr("width", json.range.max_x)
      .attr("height", json.range.max_y);

        var allCircles = [];

  for (i = 0; i < json.circles.length; i++) {

    allCircles.push(json.circles[i]);
      vis.selectAll("circle")
        .data(allCircles)
        .enter().append("svg:circle")
        .attr("cx", json.circles[i].x )
        .attr("cy", json.circles[i].y )
        .attr("r", 10)
        .style("fill", function(d) { return fill(d.id); })
        .style("stroke", 'black')
        .style("stroke-width", 3)
        
        

   };

   
});


}






