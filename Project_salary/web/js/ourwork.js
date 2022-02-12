var color = ['#fff7fb', '#ece7f2', '#d0d1e6', '#a6bddb', '#74a9cf', '#3690c0', '#0570b0', '#034e7b'];
var threshold = [0, 3, 6, 10, 20, 40, 80, 150];
function getColor(d) {
    for (var i = threshold.length - 1; i > -1; i--)
        if (d >= threshold[i])
            return color[i];
}

var mapboxAccessToken = 'pk.eyJ1Ijoic2xpdGhlcnkiLCJhIjoiY2t6Y3Mxa3dpMnI5cjJvb2Z2N2Jsb2s0MCJ9.AzaxEHz6ytBZJNoQ231GWg';
var map = L.map('htmap').setView([37.8, -96], 5);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=' + mapboxAccessToken, {
    id: 'mapbox/light-v9',
    tileSize: 512,
    zoomOffset: -1
}).addTo(map);

function style(feature) {
    return {
        fillColor: getColor(feature.properties.density),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}
var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this.update();
    return this._div;
};

// method that we will use to update the control based on feature properties passed
info.update = function (props) {
    this._div.innerHTML = '<h4>US Post Distribution of Data Scientists</h4>' + (props ?
        '<b>' + props.name + '</b><br />' + props.density + ' Data Science Post'
        : 'Hover over a state');
};

info.addTo(map);
function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        height: 5,
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
    info.update(layer.feature.properties);
}
function resetHighlight(e) {
    geojson.resetStyle(e.target);
    info.update();
}
var geojson;
function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
}
function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature
    });
}
$.ajax({
    url: "./json/job.json",//json文件位置，文件名
    type: "GET",//请求方式为get
    dataType: "json", //返回数据格式为json
    success: function (data) {//请求成功完成后要执行的方法
        geojson = L.geoJson(data, {
            style: style,
            onEachFeature: onEachFeature
        }).addTo(map);
    }
})
var legend = L.control({ position: 'bottomright' });

var legend = L.control({ position: 'bottomright' });

legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend');

    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < threshold.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(threshold[i] + 1) + '"></i> ' +
            threshold[i] + (threshold[i + 1] ? '-' + threshold[i + 1] + '<br>' : '+');
    }

    return div;
};

legend.addTo(map);


// // Creating map options
// var mapOptions = {
//     center: [39, -95],
//     zoom: 5
// }
// // Creating a map object
// var map = new L.map('htmap', mapOptions);
// // Creating a Layer object
// var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
// // Adding layer to the map
// map.addLayer(layer);

// $.ajax({
//     url: "./json/demo.json",//json文件位置，文件名
//     type: "GET",//请求方式为get
//     dataType: "json", //返回数据格式为json
//     success: function (data) {//请求成功完成后要执行的方法
//         var cfg = {  //热力图的配置项
//             radius: 25,      //设置每一个热力点的半径
//             maxOpacity: 0.9,        //设置最大的不透明度
//             minOpacity: 0.3,    //设置最小的不透明度
//             scaleRadius: false,      //设置热力点是否平滑过渡
//             blur: 0.75,            //系数越高，渐变越平滑，默认是0.85,
//             //滤镜系数将应用于所有热点数据。
//             useLocalExtrema: false,  //使用局部极值
//             latField: 'latitude',  //维度
//             lngField: 'longitude',  //经度
//             valueField: 'count',    //热力点的值
//             gradient: {
//                 "0.99": "rgba(255,110,110,0.8)",
//                 "0.9": "rgba(255,255,110,0.8)",
//                 "0.8": "rgba(110,255,110,0.8)",
//                 "0.5": "rgba(110,255,255,0.8)",
//                 "0": "rgba(110,110,255,0.8)"
//             }
//         }
//         var points = Array.from(Array(data.length), () => new Array(2));
//         for (var i = 0; i < data.length; i++) {
//             points[i][0] = data[i].lng;
//             points[i][1] = data[i].lat;
//             console.log(points[i]);
//         }
//         var heat = L.heatLayer(points, cfg).addTo(map);
//     }
// })