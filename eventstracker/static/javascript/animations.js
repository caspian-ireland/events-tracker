/**
 * A function that fades out and removes the specified element from the DOM.
 * @param {string} selector - The selector of the element to fade out and remove.
 * @param {number} waitTime - The time to wait before fading out the element.
 * @param {number} fadeTime - The time it takes for the element to fade out.
 * * @param {number} fadeTime - The time it takes for the element to slide up.
 */
function fadeOut(selector,
                 waitTime = 2000,
                 fadeTime = 2000,
                 slideTime = 500) {
    $(document).ready(function () {
        setTimeout(function () {
            $(selector).fadeTo(fadeTime, 0).slideUp(slideTime, function () {
                $(this).remove();
            });
        }, waitTime);
    });
}
