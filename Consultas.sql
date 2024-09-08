CREATE TABLE MaquinaDeGrabados (
    id INT PRIMARY KEY AUTO_INCREMENT,
    potencia_max DECIMAL(10, 2) NOT NULL,
    velocidad_grabado_max INT NOT NULL,
    estado BOOLEAN DEFAULT FALSE,
    material_grabado DECIMAL(10, 2) DEFAULT 0
);
CREATE TABLE GrabadoTiempo (
    id INT PRIMARY KEY AUTO_INCREMENT,
    maquina_id INT,
    inicio_grabado DATETIME,
    fin_grabado DATETIME,
    cantidad_material DECIMAL(10, 2),
    FOREIGN KEY (maquina_id) REFERENCES MaquinaDeGrabados(id)
);


INSERT INTO MaquinaDeGrabados (potencia_max, velocidad_grabado_max) VALUES 
(10, 100),
(8, 80),
(7, 70),
(9, 90),
(6, 60),
(5, 50),
(4, 40),
(3, 30),
(2, 20),
(1, 10);

SELECT id, potencia_max, velocidad_grabado_max
FROM MaquinaDeGrabados
ORDER BY potencia_max DESC;

SELECT id, potencia_max
FROM MaquinaDeGrabados
ORDER BY potencia_max DESC
LIMIT 3;

SELECT 
    AVG(potencia_max) as avg_potencia,
    AVG(velocidad_grabado_max) as avg_velocidad
FROM MaquinaDeGrabados;

SELECT COUNT(*) as maquinas_encendidas
FROM MaquinaDeGrabados
WHERE estado = TRUE;

SELECT id, potencia_max, material_grabado
FROM MaquinaDeGrabados
WHERE material_grabado > (potencia_max * 0.9)
ORDER BY (material_grabado / potencia_max) DESC;
