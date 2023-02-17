window.onload = function () {
    const firstPanorama = document.querySelector('.link.active');
    const body = document.getElementById('body');

    const panoramaContainer = document.querySelector('.panorama-container');
    panoramaContainer.addEventListener("click", function () {
        /*
        pass back the pano data to the current link to
        remember the view position
        */
        const currentLink = document.querySelector('.link.active');
        currentLink.setAttribute('data-id', panorama.getPano());
        currentLink.setAttribute('data-heading', panorama.getPov().heading);
        currentLink.setAttribute('data-elevation', panorama.getPov().pitch);
        currentLink.setAttribute('data-zoom-level', panorama.getPov().zoom);
        reset.style.opacity = 1;
        reset.classList.add('active');
    });

    const panorama = new google.maps.StreetViewPanorama(
        panoramaContainer,
        {
            panControl: false,
            clickToGo: false,
            addressControl: false,
            /* other options visible: false, fullscreenControl: false, 
            motionTracking: false, motionTrackingControl: false, */
        }

    );
    const links = document.querySelectorAll('.link');
    /* setup initial navigation */
    for (let i = 0; i < links.length; i++) {
        links[i].addEventListener('click', function (e) {
            e.preventDefault();
            clearActive();
            e.target.classList.add('active');
            changePanorama(e.target);
            body.innerHTML = e.target.getAttribute('data-body');
        });
    }

    const linksCached = [];
    /* cache the initial navigation */
    for (let i = 0; i < links.length; i++) {
        linksCached[i] = {
            id: links[i].getAttribute('data-id'),
            heading: links[i].getAttribute('data-heading'),
            elevation: links[i].getAttribute('data-elevation'),
            zoomLevel: links[i].getAttribute('data-zoom-level'),
        };
    }

    const reset = document.querySelector('.menu-reset');
    reset.style.opacity = 0;
    /* reset the initial panorama view */
    reset.addEventListener('click', function (e) {
        e.preventDefault();

        if (getComputedStyle(reset).opacity === '1') {
            clearActive();
            for (let i = 0; i < links.length; i++) {
                links[i].setAttribute('data-id', linksCached[i].id);
                links[i].setAttribute('data-heading', linksCached[i].heading);
                links[i].setAttribute('data-elevation', linksCached[i].elevation);
                links[i].setAttribute('data-zoom-level', linksCached[i].zoomLevel);
            }
            firstPanorama.classList.add('active');
            changePanorama(firstPanorama);
            reset.style.opacity = 0;
            reset.classList.remove('active');
        }
    });

    /* helpers */
    function clearActive() {
        for (let i = 0; i < links.length; i++) {
            links[i].classList.remove('active');
        }
    }
    function changePanorama(link) {
        const panoid = link.getAttributeNode('data-id').value;
        panorama.setPov({
            heading: link.getAttributeNode('data-heading').value * 1,
            pitch: link.getAttributeNode('data-elevation').value * 1,
            zoom: Math.floor(link.getAttributeNode('data-zoom-level').value),
        });
        panorama.setPano(panoid);
    }

    const qs = window.location.search;
    const urlParams = new URLSearchParams(qs);
    const panoramaId = urlParams.get('panorama');
    if (panoramaId) {
        /* set the initial panorama view for previews */
        const link = document.querySelector(`.link[data-id="${panoramaId}"]`);
        if (link) {
            link.click();
        }
    } else {
        /* set the first panorama as default */
        links[0].click();
    }

};
