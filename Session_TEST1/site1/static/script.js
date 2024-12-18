document.addEventListener("DOMContentLoaded", () => {
    const lightingEffect = document.getElementById("lighting-effect");

    // Function to trigger the lighting effect
    function triggerLightingEffect() {
        lightingEffect.classList.add("active");

        // Remove the 'active' class after the animation ends to reset
        setTimeout(() => {
            lightingEffect.classList.remove("active");
        }, 500); // Duration matches the CSS animation length (0.5 seconds)
    }

    // Trigger the effect for the first time after 3 seconds
    setTimeout(triggerLightingEffect, 3000);

    // Repeat the lighting effect every 6 seconds
    setInterval(triggerLightingEffect, 9000);
});
