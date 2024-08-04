from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def get():
    return Html(
        Head(
            Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap"),
            Style("""
                body { display: flex; justify-content: center; align-items: center; height: 100vh; background: black; color: #0f0; font-family: 'Roboto Mono', monospace; margin: 0; overflow: hidden; }
                #clock { font-size: 5em; text-shadow: 0 0 5px #0f0, 0 0 10px #0f0, 0 0 20px #0f0, 0 0 30px #0f0; animation: pulse 1s infinite; }
                @keyframes pulse {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.05); }
                    100% { transform: scale(1); }
                }
                .matrix {
                    position: absolute;
                    width: 100%;
                    height: 100%;
                    z-index: -1;
                }
                .matrix canvas {
                    display: block;
                    position: absolute;
                    top: 0;
                    left: 0;
                }
            """)
        ),
        Body(
            Div(Class="matrix", Id="matrix"),
            Div(Id="clock"),
            Script("""
                function updateClock() {
                    const now = new Date();
                    const hours = String(now.getHours()).padStart(2, '0');
                    const minutes = String(now.getMinutes()).padStart(2, '0');
                    const seconds = String(now.getSeconds()).padStart(2, '0');
                    document.getElementById('clock').textContent = `${hours}:${minutes}:${seconds}`;
                }
                setInterval(updateClock, 1000);
                updateClock();

                // Matrix effect
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');
                document.getElementById('matrix').appendChild(canvas);

                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;

                const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
                const fontSize = 10;
                const columns = canvas.width / fontSize;
                const drops = Array(Math.floor(columns)).fill(1);

                function draw() {
                    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                    ctx.fillStyle = '#0f0';
                    ctx.font = fontSize + 'px monospace';

                    for (let i = 0; i < drops.length; i++) {
                        const text = letters[Math.floor(Math.random() * letters.length)];
                        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                            drops[i] = 0;
                        }
                        drops[i]++;
                    }
                }

                setInterval(draw, 33);
            """)
        )
    )

serve()
