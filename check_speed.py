import bpy
import math
sce = bpy.context.scene
number_of_uavs = 2 # we have 20 objects
scale = 1 # we want to scale scene by 1.3
scene_frames = 1080 # scene frame length
speed_treshold = 3 # speed treshold in meters per second
frame_rate = 4 # our target, autopilot, framerate. Usually it's 4 FPS.
blender_frame_rate = 24 # blender framerate

l_x = 0
l_y = 0
l_z = 0

for i in range(0, number_of_uavs):
    ob = bpy.data.objects['Sphere.00' + str(i)]
    for f in range(sce.frame_start, scene_frames):
        if ((f-1) % (blender_frame_rate / frame_rate) == 0):
            sce.frame_set(f)
            if (f>(blender_frame_rate / frame_rate)):
                x = ob.matrix_world.to_translation().x * scale
                y = ob.matrix_world.to_translation().y * scale
                z = ob.matrix_world.to_translation().z * scale
                dx = l_x - x
                dy = l_y - y
                dz = l_z - z
                d = math.sqrt(dx*dx + dy*dy + dz*dz)
                s = d * frame_rate
                if (s > speed_treshold):
                    print("Danger! Speed = " + str(s) + " m\s for " + str(i) + " on " + str(f) + " frame")
                # else:
                #    print("OK! Speed = " + str(s) + " m\s for " + str(i) + " on " + str(f) + " frame")
                l_x = x
                l_y = y
                l_z = z
        else:
            l_x = ob.matrix_world.to_translation().x * scale
            l_y = ob.matrix_world.to_translation().y * scale
            l_z = ob.matrix_world.to_translation().z * scale
