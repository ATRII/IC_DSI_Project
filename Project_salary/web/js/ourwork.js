// Creating map options
var mapOptions = {
    center: [39, -95],
    zoom: 5
}
// Creating a map object
var map = new L.map('htmap', mapOptions);
// Creating a Layer object
var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
// Adding layer to the map
map.addLayer(layer);

$.ajax({
    url: "../json/demo.json",//json文件位置，文件名
    type: "GET",//请求方式为get
    dataType: "json", //返回数据格式为json
    success: function (data) {//请求成功完成后要执行的方法
        var cfg = {
            minOpacity: 0.5,
            radius: 20,
            gradient: { 0.3: 'blue', 0.65: 'lime', 0.8: 'rgb(255,69,0)', 1: 'rgb(128, 0, 0)' }
        };
        var points = Array.from(Array(data.length), () => new Array(2));
        for (var i = 0; i < data.length; i++) {
            points[i][0] = data[i].lng;
            points[i][1] = data[i].lat;
            console.log(points[i]);
        }
        var heat = L.heatLayer(points, cfg).addTo(map);
    }
})