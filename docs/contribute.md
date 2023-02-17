# Developer setup

Developer documentation is still been worked on.

## Install the package in editable mode

Activate your virtual environment and run the following commands.

```bash
pip install -e ".[testing]"
make migrate
make load
```

Run the testing app.

```bash
make run
```

## Frontend

If you wish to alter the css or javascript.

```bash
nvm use
npm install
npm run build
```

## Start URLS

[Cinema](https://www.google.com/maps/place/Regal+Cinema+Evesham/@52.0908374,-1.9398567,3a,90y,335.58h,97.94t/data=!3m8!1e1!3m6!1sAF1QipOgxIjSzz29Zm6sXKgCrla-pWHvK2mKnjzybldG!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOgxIjSzz29Zm6sXKgCrla-pWHvK2mKnjzybldG%3Dw203-h100-k-no-pi-30.000002-ya83.87635-ro-0-fo100!7i13312!8i6656!4m8!3m7!1s0x4870dde2a3c124f9:0x540b84f32ae5f6ab!8m2!3d52.090865!4d-1.939927!14m1!1BCgIgARICCAI!16s%2Fg%2F11h0tfkgc)

[Wedding Venue](https://www.google.com/maps/place/Manor+Hill+House+Weddings/@52.3186733,-2.1176422,3a,75y,135.12h,96.59t/data=!3m8!1e1!3m6!1sAF1QipNCY-B2vds3c63LlfIH-Dk6VBla3QdJALVecd-8!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipNCY-B2vds3c63LlfIH-Dk6VBla3QdJALVecd-8%3Dw224-h298-k-no-pi-0-ya237.14285-ro0-fo100!7i8000!8i4000!4m8!3m7!1s0x4870ece053171809:0x99ab2060fe09039b!8m2!3d52.3184969!4d-2.1174893!14m1!1BCgIgARICCAI!16s%2Fg%2F1tdlgr2z)

[Restaurant](https://www.google.com/maps/place/Bullocks+Bistro+and+bar/@52.2681251,-2.146122,3a,90y,183.06h,117.51t/data=!3m8!1e1!3m6!1sAF1QipN3_M3OONDMhBcz6leUfD5PvDWFwb__RvMVSeh8!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipN3_M3OONDMhBcz6leUfD5PvDWFwb__RvMVSeh8%3Dw203-h100-k-no-pi-20-ya1.5714489-ro-0-fo100!7i13312!8i6656!4m8!3m7!1s0x4870ede88ffe2963:0x65d2e616db4b051b!8m2!3d52.2680806!4d-2.1461306!14m1!1BCgIgARICCAI!16s%2Fg%2F11ckvlphp4)
