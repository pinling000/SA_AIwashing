const map = L.map('map').setView([0, 0], 16);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

//定義 marker 顏色
let mask;
//取出綠、橘、紅三個顏色來代表口罩數量的不同狀態
const greenIcon = new L.Icon({
    iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

const orangeIcon = new L.Icon({
    iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-orange.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});


const redIcon = new L.Icon({
    iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

const violetIcon = new L.Icon({
    iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-violet.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

if ('geolocation' in navigator) {
    // 如果定位可以運行，就印出 'geolocation available'
        console.log('geolocation available');
        // 取得使用者位置的經緯度
        navigator.geolocation.getCurrentPosition(position => {
        userLat = position.coords.latitude;
        userLng = position.coords.longitude;
        // 印出使用者位置的經緯度
        console.log(userLat, userLng);
        // 以使用者的經緯度取代 [0, 0]
        map.setView([userLat, userLng], 13);
        // 在使用者所在位置標上 marker
        marker.setLatLng([userLat,userLng]).bindPopup(
            `<h3>你的位置</h3>`)
            .openPopup();
        });
    } else {
    // 如果定位無法運行，就印出 'geolocation not available'
        console.log('geolocation not available');
    }

    let geoBtn = document.getElementById('jsGeoBtn');
    geoBtn.addEventListener('click',function(){
    map.setView([userLat, userLng], 13);
    marker.setLatLng([userLat,userLng]).bindPopup(
        `<h3>你的位置</h3>`)
        .openPopup();
    },false);

const marker = L.marker([0, 0] , {icon:violetIcon}).addTo(map);

function init(){
    getData();
}

let data;

function getData(){
    const xhr = new XMLHttpRequest;
    xhr.open('get','https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json',true)
    xhr.send(null);
    xhr.onload = function(){
        data = JSON.parse(xhr.responseText).features;
        addMarker();
    }
}

init();

const markers = new L.MarkerClusterGroup({ disableClusteringAtZoom: 18 }).addTo(map);

function addMarker(){
    for(let i = 0;i<data.length;i++){
        const pharmacyName = data[i].properties.name;
        const maskAdult = data[i].properties.mask_adult;
        const maskChild = data[i].properties.mask_child;
        const lat = data[i].geometry.coordinates[1];
        const lng = data[i].geometry.coordinates[0];
        const pharmacyAddress = data[i].properties.address;
        const pharmacyPhone = data[i].properties.phone;
        const pharmacyNote = data[i].properties.note;
        if(maskAdult == 0 || maskChild == 0){
            mask = redIcon;
        }else if (maskAdult < 100 && maskAdult !== 0 || maskChild < 100 && maskChild !== 0){
            mask = orangeIcon;
        }else{
            mask = greenIcon;
        }
        let maskAdultJudge;
        let maskChildJudge;

        if (maskAdult >= 100) {
            maskAdultJudge = 'bg-sufficient';
        } else if (maskAdult < 100 && maskAdult !== 0) {
            maskAdultJudge = 'bg-insufficient';
        } else {
            maskAdultJudge = 'bg-none';
        }
        if (maskChild >= 100) {
            maskChildJudge = 'bg-sufficient';
        } else if (maskChild < 100 && maskChild !== 0) {
            maskChildJudge = 'bg-insufficient';

        } else {
            maskChildJudge = 'bg-none';
        }
        // L.marker([lat,lng], {icon: mask}).addTo(map);
        markers.addLayer(L.marker([lat,lng], {icon: mask}).bindPopup(
        `<div class="popupInfo">
            <p class="popupTitle" data-name="${pharmacyName}"><span>${pharmacyName}</span></p>
            <hr>
            <p class="popupText"><i class="fas fa-map-marker-alt"></i> ${pharmacyAddress}</p>
            <p class="popupText"><i class="fas fa-phone-square-alt"></i> ${pharmacyPhone}</p>
            <p class="popupNote"> ${pharmacyNote}</p>
            <div class="panelMaskNum" data-name="${pharmacyName}">
                <div class="${maskAdultJudge}">
                    <div class="popupLayout">
                    成人:
                    <p class="popupMaskNum">${maskAdult}</p>
                    </div>
                </div>
                &nbsp;<div class="${maskChildJudge}">
                    <div class="popupLayout">
                    幼兒:
                    <p class="popupMaskNum">${maskChild}</p>
                    </div>
                </div>
            </div>
        </div>`
        ));
    }
    map.addLayer(markers);
}
