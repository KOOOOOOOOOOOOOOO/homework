var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(37.54699, 127.09598), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };
var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

kakao.maps.event.addListener(map, 'click',function (mouseEvent){

    var latlng = mouseEvent.latLng;
    $("#la").val(latlng.La);
    $("#ma").val(latlng.Ma);
    if($("#post-box").css("display") == "block"){
        alert("데이터를 입력해주세요!");
        return false;
    }else {
        cat_info();
        addMarker(mouseEvent.latLng);
    }
})

var markers = [];

function showCatsInfo(){
    $.ajax({
        type: 'GET',
        url: '/markers',
        data: {},
        success: function (response) {
            let markers = response['markers'];
            for (let i = 0; i < markers.length; i++) {

            }
        }
    })
}

addMarker(new kakao.maps.LatLng(33.450701, 126.570667));

function addMarker(position) {

    var positions = [
        {
            content: '<div>test</div>',
            latlng : position
        }
    ];

    for (var i = 0; i < positions.length; i++) {

        var imageSrc = "/static/images/cat_marker.png",
            imageSize = new kakao.maps.Size(64, 69), // 마커이미지의 크기입니다
            imageOption = {offset: new kakao.maps.Point(27, 69)}; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.

        var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption);

        var marker = new kakao.maps.Marker({
            map: map,
            position: positions[i].latlng,
            image: markerImage
        });
           var infowindow = new kakao.maps.InfoWindow({
            content: positions[i].content // 인포윈도우에 표시할 내용
        });
    }

    kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, infowindow));
    kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));

    marker.setMap(map);

    markers.push(marker);

}

function makeOverListener(map, marker, infowindow) {
    return function() {
        infowindow.open(map, marker);
    };
}

    // 인포윈도우를 닫는 클로저를 만드는 함수입니다
function makeOutListener(infowindow) {
    return function() {
        infowindow.close();
    };
}

function setMarkers(map){
    for (var i=0; i<markers.length; i++){
        markers[i].setMap(map);
    }
}

function showMarkers(){
    showCatsmarker()
}

function hideMarkers(){
    setMarkers(null);
}

function cat_info(){
        $("#post-box").show();
}