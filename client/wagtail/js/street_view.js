window.onload = function () {


    const panoIdField = document.getElementById("id_panorama_id");
    const panoId = panoIdField.value;

    const positionLat = document.getElementById("id_lat");
    const panoLat = positionLat.value;

    const positionLng = document.getElementById("id_lng");
    const panoLng = positionLng.value;

    const headingField = document.getElementById("id_heading");
    const panoHeading = headingField.value;

    const elevationField = document.getElementById("id_elevation");
    const panoElevation = elevationField.value;

    const zoomField = document.getElementById("id_zoom_level");
    const panoZoom = zoomField.value;

    const panorama = new google.maps.StreetViewPanorama(
        pano,
        {
            position: { lat: panoLat * 1, lng: panoLng * 1 },
            pov: {
                heading: panoHeading * 1,
                pitch: panoElevation * 1,
                zoom: Math.floor(panoZoom),
            },
            panControl: false,
            clickToGo: false,
            /* other options */
            // visible: false,
            // addressControl: false,
            // fullscreenControl: false,
            // motionTracking: false,
            // motionTrackingControl: false,
        }
    );

    panorama.addListener('pano_changed', function () {
        panoIdField.value = panorama.getPano();
    });

    panorama.addListener("position_changed", function () {
        const latlng = panorama.position.toJSON();
        positionLat.value = latlng.lat;
        positionLng.value = latlng.lng;
    });

    panorama.addListener("pov_changed", function () {
        headingField.value = panorama.getPov().heading;
        elevationField.value = panorama.getPov().pitch;
        if (panorama.getPov().zoom < 1) {
            zoomField.value = 0;
        } else {
            zoomField.value = panorama.getPov().zoom;
        }
    });
}
