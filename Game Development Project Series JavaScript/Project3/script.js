const canvas = document.getElementById('canvas1');
const ctx = canvas.getContext('2d');
CANVAS_WIDTH = canvas.width = 1200;
CANVAS_HEIGHT = canvas.height = 700;
const numberOfEnemies = 5;
const enemiesArray = [];
let gameFrame = 0;

class Enemy {
	constructor(imageSrc, spriteWidth, spriteHeight, widthRatio, heightRatio, speed, flapSpeed) {
		this.image = new Image();
		this.image.src = imageSrc;
		this.speed = speed;
		this.spriteWidth = spriteWidth;
		this.spriteHeight = spriteHeight;
		this.width = spriteWidth / widthRatio;
		this.height = spriteHeight / heightRatio;
		this.x = Math.random() * (canvas.width - this.width);
		this.y = Math.random() * (canvas.height - this.height);
		this.frame = 0;
		this.flapSpeed = Math.floor(Math.random() * flapSpeed + 1);
	}

	update() {
		this.x += Math.random() * 5 - 2.5;
		this.y += Math.random() * 5 - 2.5;
		if (gameFrame % this.flapSpeed === 0) {
			this.frame > 4 ? (this.frame = 0) : this.frame++;
		}
	}

	draw() {
		ctx.drawImage(
			this.image,
			this.frame * this.spriteWidth,
			0,
			this.spriteWidth,
			this.spriteHeight,
			this.x,
			this.y,
			this.width,
			this.height
		);
	}
}

class Enemy1 extends Enemy {
	constructor() {
		super('./enemies/enemy1.png', 293, 155, 2.5, 2.5, Math.random() * 4 - 2, 3);
	}
}

class Enemy2 extends Enemy {
	constructor() {
		super('./enemies/enemy2.png', 266, 188, 2, 2, Math.random() * 4 + 1, 3);
		this.angle = 0;
		this.angleSpeed = Math.random() * 0.2;
		this.curve = Math.random() * 7;
	}

	update() {
		this.x -= this.speed;
		this.y += this.curve * Math.sin(this.angle);
		this.angle += this.angleSpeed;
		if (this.x + this.width < 0) this.x = canvas.width;
		super.update();
	}
}

class Enemy3 extends Enemy {
	constructor() {
		super('./enemies/enemy3.png', 218, 177, 2, 2, Math.random() * 4 + 1, 3);
		this.angle = 0;
		this.angleSpeed = Math.random() * 0.5 + 0.5;
	}

	update() {
		this.x =
			(canvas.width / 2) * Math.sin((this.angle * Math.PI) / 90) +
			(canvas.width / 2 - this.width / 2);
		this.y =
			(canvas.height / 2) * Math.cos((this.angle * Math.PI) / 360) +
			(canvas.height / 2 - this.height / 2);
		this.angle += this.angleSpeed;
		if (this.x + this.width < 0) this.x = canvas.width;
		super.update();
	}
}

class Enemy4 extends Enemy {
	constructor() {
		super('./enemies/enemy4.png', 213, 213, 2, 2, Math.random() * 4 + 1, 3);
		this.newX = Math.random() * canvas.width;
		this.newY = Math.random() * canvas.height;
		this.interval = Math.floor(Math.random() * 200 + 50);
	}

	update() {
		if (gameFrame % this.interval === 0) {
			this.newX = Math.random() * (canvas.width - this.width);
			this.newY = Math.random() * (canvas.height - this.height);
		}
		let dx = this.x - this.newX;
		let dy = this.y - this.newY;
		this.x -= dx / 70;
		this.y -= dy / 70;
		if (this.x + this.width < 0) this.x = canvas.width;
		super.update();
	}
}

for (let i = 0; i < numberOfEnemies; i++) {
	enemiesArray.push(new Enemy1());
	enemiesArray.push(new Enemy2());
	enemiesArray.push(new Enemy3());
	enemiesArray.push(new Enemy4());
}

function animate() {
	ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
	enemiesArray.forEach((enemy) => {
		enemy.update();
		enemy.draw();
	});
	gameFrame++;
	requestAnimationFrame(animate);
}

animate();
