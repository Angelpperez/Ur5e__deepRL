import mujoco
import mujoco.viewer
import os
import numpy as np
from threading import Thread
import time

# Ruta del modelo
model_path = os.path.join("mujoco_menagerie", "universal_robots_ur5e", "scene.xml")

    # Cargar el modelo
model = mujoco.MjModel.from_xml_path(model_path)
data = mujoco.MjData(model)

    # Frecuencias y amplitudes de movimiento para cada articulación
frequencies = np.array([0.2, 0.2, 0.4, 0.3, 0.5, 0.1])  # Hz
amplitudes = np.array([0.4, 0.3, 0.2, 0.11, -0.2, 1])  # Radianes

def main_script():


    # Lanzar el visor interactivo
    with mujoco.viewer.launch_passive(model, data) as viewer:
        step = 0
        while viewer.is_running():
            step += 1
            t = step * model.opt.timestep  # Tiempo de simulación

            # Aplicar movimientos sinusoidales en todas las articulaciones
            data.qpos[:6] = -0.5 + (amplitudes * np.sin(2 * np.pi * frequencies * t))

            mujoco.mj_step(model, data)  # Avanzar la simulación
            viewer.sync()
            
def interactive_console():
    # Proporciona acceso a las variables globales del script
    import code
    code.interact(local=globals())


if __name__ == "__main__":
    # Lanza el hilo principal para tu script
    Thread(target=main_script, daemon=True).start()
    
    # Inicia la consola interactiva
    interactive_console()