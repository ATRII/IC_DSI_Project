var color = [['#fff7fb', '#ece7f2', '#d0d1e6', '#a6bddb', '#74a9cf', '#3690c0', '#0570b0', '#034e7b']
    , ['#fff7ec', '#fee8c8', '#fdd49e', '#fdbb84', '#fc8d59', '#ef6548', '#d7301f', '#990000']
    , ['#ffffe5', '#f7fcb9', '#d9f0a3', '#addd8e', '#78c679', '#41ab5d', '#238443', '#005a32']];
var threshold = [[0, 3, 6, 10, 20, 40, 80, 150], [0, 80, 85, 90, 95, 100, 105, 110], [0, 5, 10, 15, 20, 40, 60, 100]];
var mapboxAccessToken = 'pk.eyJ1Ijoic2xpdGhlcnkiLCJhIjoiY2t6Y3Mxa3dpMnI5cjJvb2Z2N2Jsb2s0MCJ9.AzaxEHz6ytBZJNoQ231GWg';
var map = L.map('htmap').setView([37.8, -96], 5);
var info = [L.control(), L.control(), L.control()];
var handle;
var Data = new Array(3);
var legend = [L.control({ position: 'bottomright' }), L.control({ position: 'bottomright' }), L.control({ position: 'bottomright' })];
var num = 0;
var url = ["../json/job.json", "../json/job_avg.json", "../json/company.json"];
var title = ['<h4>US Post Distribution of Data Scientists</h4>', '<h4>US Average income distribution of Data Scientists</h4>', '<h4>Distribution of US Companies recruiting Data Scientists</h4>'];
var untex = ['', '$', ''];
var unt = [' Data Science Post', 'K', 'Company'];

init();
function roundFun(value, n) {
    return Math.round(value * Math.pow(10, n)) / Math.pow(10, n);
}
function deletelast() {
    console.log(num);
    map.removeLayer(hold);
    info[num].remove();
    legend[num].remove();
}
function draw() {
    console.log(num);
    hold = L.geoJson(Data[num], {
        style: style,
        onEachFeature: onEachFeature
    }).addTo(map);
    info[num].addTo(map);
    legend[num].addTo(map);
}
function change(n) {
    deletelast();
    num = n;
    draw();
}
function init() {
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=' + mapboxAccessToken, {
        id: 'mapbox/light-v9',
        tileSize: 512,
        zoomOffset: -1
    }).addTo(map);
    for (var I = 2; I >= 0; I--) {
        num = I;
        info[I].onAdd = function (map) {
            this._div = L.DomUtil.create('div', 'info');
            this.update();
            return this._div;
        };
        info[I].update = function (props) {
            this._div.innerHTML = title[num] + (props ?
                ('<b>' + props.name + '</b><br />' + (props.density ?
                    (untex[num] + roundFun(props.density, 2) + unt[num]) : 'no data'))
                : 'Hover over a state');
        };
        legend[I].onAdd = function (map) {
            var div = L.DomUtil.create('div', 'info legend');
            for (var j = -1; j < threshold[num].length; j++) {
                div.innerHTML += ((j == -1) ? ('<i style="background:' + getColor(0, 0) + '"></i> ' + 'no data<br>') :
                    ('<i style="background:' + getColor(threshold[num][j] + 1, num) + '"></i> ' +
                        threshold[num][j] + (threshold[num][j + 1] ? ('-' + threshold[num][j + 1] + '<br>') : '+')));
            }
            return div;
        };
        read(I);
    }
    info[0].addTo(map);
    legend[0].addTo(map);
    hold = L.geoJson(Data[0], {
        style: style,
        onEachFeature: onEachFeature
    }).addTo(map);
}
function read(i) {
    $.ajax({
        url: url[i],//json????????????????????????
        type: "GET",//???????????????get
        dataType: "json", //?????????????????????json
        success: function (data) {//???????????????????????????????????????
            Data[i] = data;
        }
    })
}
function getColor(d, num) {
    if (d == 0) return 'rgba(255,255,255,0.7)'
    for (var i = threshold[0].length - 1; i > -1; i--)
        if (d >= threshold[num][i])
            return color[num][i];
}
function style(feature) {
    return {
        fillColor: getColor(feature.properties.density, num),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}
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
    info[num].update(layer.feature.properties);
}
function resetHighlight(e) {
    hold.resetStyle(e.target);
    info[num].update();
}
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
//     url: "./json/demo.json",//json????????????????????????
//     type: "GET",//???????????????get
//     dataType: "json", //?????????????????????json
//     success: function (data) {//???????????????????????????????????????
//         var cfg = {  //?????????????????????
//             radius: 25,      //?????????????????????????????????
//             maxOpacity: 0.9,        //???????????????????????????
//             minOpacity: 0.3,    //???????????????????????????
//             scaleRadius: false,      //?????????????????????????????????
//             blur: 0.75,            //??????????????????????????????????????????0.85,
//             //?????????????????????????????????????????????
//             useLocalExtrema: false,  //??????????????????
//             latField: 'latitude',  //??????
//             lngField: 'longitude',  //??????
//             valueField: 'count',    //???????????????
//             gradient: {
//                 "0.99": "rgba(255,120,120,0.8)",
//                 "0.9": "rgba(255,255,120,0.8)",
//                 "0.8": "rgba(120,255,120,0.8)",
//                 "0.5": "rgba(120,255,255,0.8)",
//                 "0": "rgba(120,120,255,0.8)"
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