document.addEventListener("DOMContentLoaded", () => {
    const globeContainer = document.getElementById('globe-viz');
    if (!globeContainer) return;

    // Check if Globe.gl is loaded
    if (typeof Globe === 'undefined') {
        console.error('Globe.gl is not loaded');
        return;
    }

    // Coordinates for India (Origin - Nashik Head Office)
    const IND = { lat: 20.0112, lng: 73.7902, name: "Growviax - Nashik - India", code: "in" };

    // Coordinates for Destinations
    const destinations = [
        { lat: 55.3781, lng: -3.4360, name: "UK", code: "gb" },
        { lat: 4.2105, lng: 101.9758, name: "Malaysia", code: "my" },
        { lat: 14.0583, lng: 108.2772, name: "Vietnam", code: "vn" },
        { lat: 23.4241, lng: 53.8478, name: "UAE", code: "ae" },
        { lat: 25.3548, lng: 51.1839, name: "Qatar", code: "qa" },
        { lat: 15.8700, lng: 100.9925, name: "Thailand", code: "th" },
        { lat: -0.7893, lng: 113.9213, name: "Indonesia", code: "id" },
        { lat: 51.1657, lng: 10.4515, name: "Germany", code: "de" },
        { lat: 61.9241, lng: 25.7482, name: "Finland", code: "fi" },
        { lat: 60.4720, lng: 8.4689, name: "Norway", code: "no" },
        { lat: 1.3521, lng: 103.8198, name: "Singapore", code: "sg" }
    ];

    // Create Arc Data
    const arcsData = destinations.map(dest => ({
        startLat: IND.lat,
        startLng: IND.lng,
        endLat: dest.lat,
        endLng: dest.lng,
        color: ['#8BC34A', '#2E7D32'], // Light green to Primary green
        name: `${IND.name} -> ${dest.name}`
    }));

    // Include origin in points
    const pointsData = destinations.concat([IND]);

    // Initialize Globe
    const globe = Globe()(globeContainer)
        .globeImageUrl('https://unpkg.com/three-globe/example/img/earth-dark.jpg')
        .bumpImageUrl('https://unpkg.com/three-globe/example/img/earth-topology.png')
        .backgroundColor('rgba(0,0,0,0)')
        
        // Arc settings
        .arcsData(arcsData)
        .arcColor('color')
        .arcDashLength(0.4)
        .arcDashGap(4)
        .arcDashInitialGap(() => Math.random() * 5)
        .arcDashAnimateTime(2000)
        .arcStroke(1.5)
        
        // Points settings (Highlight countries)
        .pointsData(pointsData)
        .pointColor(() => '#8BC34A')
        .pointAltitude(0.01)
        .pointRadius(0.4)
        
        // HTML Elements for Flags and Names
        .htmlElementsData(pointsData)
        .htmlElement(d => {
            const el = document.createElement('div');
            el.innerHTML = `
              <div class="globe-label">
                <img src="https://flagcdn.com/w20/${d.code}.png" alt="flag">
                <span class="globe-label-text">${d.name}</span>
              </div>
            `;
            return el;
        });

    // Inject CSS for interactive labels
    const style = document.createElement('style');
    style.innerHTML = `
      .globe-label {
        display: flex;
        align-items: center;
        background: rgba(0,0,0,0.7);
        border: 2px solid rgba(139, 195, 74, 0.8);
        border-radius: 20px;
        padding: 2px;
        cursor: pointer;
        pointer-events: auto;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        overflow: hidden;
        transform: translate(-50%, -50%);
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
      }
      .globe-label:hover {
        background: rgba(139, 195, 74, 0.95);
        border-color: #fff;
        padding-right: 12px;
        z-index: 1000;
        box-shadow: 0 0 15px rgba(139,195,74,0.8);
      }
      .globe-label img {
        width: 22px;
        height: 22px;
        border-radius: 50%;
        object-fit: cover;
      }
      .globe-label .globe-label-text {
        color: white;
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        font-weight: 600;
        max-width: 0;
        opacity: 0;
        white-space: nowrap;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        padding-left: 0;
      }
      .globe-label:hover .globe-label-text {
        max-width: 120px;
        opacity: 1;
        padding-left: 8px;
      }
    `;
    document.head.appendChild(style);

    // Initial positioning to focus roughly around India/Middle East
    setTimeout(() => {
        globe.pointOfView({ lat: 20, lng: 70, altitude: 1.8 }, 1000);
    }, 500);

    // Auto rotate slowly
    globe.controls().autoRotate = true;
    globe.controls().autoRotateSpeed = 0.5;
    
    // Disable zoom so the mouse wheel scrolls the page instead of getting trapped
    globe.controls().enableZoom = false;

    // Handle Resize
    window.addEventListener('resize', () => {
        globe.width(globeContainer.clientWidth);
        globe.height(globeContainer.clientHeight);
    });
});
