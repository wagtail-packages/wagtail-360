
# Build a virtual tour

1. Search for a business on google maps. E.g. [Hotel](https://www.google.com/maps/place/Northwick+Hotel/@52.0903113,-1.9447408,17z/data=!3m1!4b1!4m9!3m8!1s0x4870de07f481bdfd:0x4fbce822a88eff7a!5m2!4m1!1i2!8m2!3d52.090308!4d-1.9425521!16s%2Fg%2F1hc4ksp1p)

2. On the left scroll down to the Street View & 360 images and click in the picture icon.

3. Click around to find a suitable starting view. [Try this link](https://www.google.com/maps/place/Northwick+Hotel/@52.0901131,-1.9423237,3a,75y,8.77h,85.01t/data=!3m7!1e1!3m5!1sAF1QipMVE-i3cvipAlUVg33jA3sM-mMkF_K0L_eYZexO!2e10!3e2!7i13312!8i6656!4m11!3m10!1s0x4870de07f481bdfd:0x4fbce822a88eff7a!5m2!4m1!1i2!8m2!3d52.090308!4d-1.9425521!14m1!1BCgIgARICCAI!16s%2Fg%2F1hc4ksp1p)

4. Copy the url from the browser address bar. Or use this:

    ```text
    https://www.google.com/maps/place/Aquatics+%26+Reptiles/@52.1870119,-2.234866,3a,75y,334.08h,91.65t/data=!3m7!1e1!3m5!1sAF1QipMOrPzw37q0zV2sRnLBG43s9F4dJmf1XX2zyyxv!2e10!3e13!7i13312!8i6656!4m7!3m6!1s0x0:0x87d71961c90b1709!8m2!3d52.187041!4d-2.234878!14m1!1BCgIgARICCAI
    ```

5. In the Wagtail admin create a new **Tour Page** and paste in the url you copied. You should see that the url is valid and the maps data has been extracted to the correct fields. **Now give the page a title and save it.**

## Panorama Page

1. View the Tour Page and create a new child page, the only one available is the Panorama Page so you should see the edit page. The initial panorama view will be copied over from the Tour Page fields.
2. Click around to set the view you like. As you do that the page fields will be updated with new values. You can: **Move to a new place using the arrows** | **Spin the parorama around to find the best view** | **Zoom in or out** | **Set the elevation**
3. Give the view a title and save the page.
4. Add another panorama child page. This time the initial view will be the same view you set on the previous panorama.
5. Repeat steps 1 - 4 until you have all the views you need.
6. Use live preview to see the virtual tour with menu navigation.
