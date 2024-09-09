from Maquina_de_grabados import MaquinaDeGrabados
import pytest

def test_inicializacion_componentes():
    maquina = MaquinaDeGrabados(5, 50)
    assert isinstance(maquina, MaquinaDeGrabados)
    assert maquina.potencia_max == 5
    assert maquina.velocidad_grabado_max == 50
    assert maquina.estado() == False

def test_representacion_en_str():
    maquina = MaquinaDeGrabados(5, 50)
    str_esperado = 'Máquina de Grabados [Potencia: 5, Velocidad: 50, Estado: apagada]'
    assert str(maquina) == str_esperado

def test_estado_de_la_maquina():
    maquina = MaquinaDeGrabados(5, 50)
    assert maquina.estado() == False
    maquina.encender()
    assert maquina.estado() == True

def test_estado_de_la_maquina_encendida():
    maquina = MaquinaDeGrabados(5, 50)
    maquina.encender()
    with pytest.raises(ValueError, match='La máquina ya está encendida!'):
        maquina.encender()

def test_estado_de_la_maquina_apagada():
    maquina = MaquinaDeGrabados(5, 50)
    maquina.encender()
    maquina.apagar()
    with pytest.raises(ValueError, match='La máquina ya está apagada!'):
        maquina.apagar()

def test_iniciar_grabado():
    maquina = MaquinaDeGrabados(5, 50)
    maquina.encender()
    maquina.iniciar_grabado(4)
    assert maquina.material_grabado == 4
    
    with pytest.raises(ValueError, match='La máquina debe estar encendida para grabar material.'):
        maquina.apagar()
        maquina.iniciar_grabado(2)

def test_tiempo_para_grabar():
    maquina = MaquinaDeGrabados(5, 50)
    maquina.encender()
    maquina.iniciar_grabado(3)
    assert maquina.tiempo_necesario_para_grabar() == 30.0
