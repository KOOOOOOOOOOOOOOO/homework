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

addMarker(new kakao.maps.LatLng(33.450701, 126.570667));

function addMarker(position) {

    var imageSrc = "/static/images/cat_marker.png",
        imageSize = new kakao.maps.Size(64, 69), // 마커이미지의 크기입니다
        imageOption = {offset: new kakao.maps.Point(27, 69)}; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.

    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption);

    var marker = new kakao.maps.Marker({
        position: position,
        image: markerImage
    });

    marker.setMap(map);

    markers.push(marker);


    var content = '<div class="wrap">' +
        '    <div class="info">' +
        '        <div class="title">' +
        '            쫑쫑이' +
        '            <div class="close" onclick="closeOverlay()" title="닫기"></div>' +
        '        </div>' +
        '        <div class="body">' +
        '            <div class="img">' +
        '                <img src="https://images.mypetlife.co.kr/content/uploads/2019/09/06144600/zach-reiner-YVpr0OdSUe0-unsplash.jpg" width="73" height="70">' +
        '           </div>' +
        '            <div class="desc">' +
        '                <div class="ellipsis">00시 00동 어쩌구 저쩌구</div>' +
        '                <div class="comment">고목 나무 옆 쓰레기통에서 기웃거림.</div>' +
        '            </div>' +
        '        </div>' +
        '    </div>' +
        '</div>';

    var overlay = new kakao.maps.CustomOverlay({
        content: content,
        map: map,
        position: marker.getPosition()
    });

    kakao.maps.event.addListener(marker, 'click', function() {
        overlay.setMap(map);
    });

     function closeOverlay() {
        overlay.setMap(null);
    }

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
