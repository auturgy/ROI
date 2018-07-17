# import blender packets
import bpy
# blender context scene
sce = bpy.context.scene
number_of_uavs = 2 # we have 20 objects
scale = 1 # we want to scale scene by 1.3
scene_frames = 1080 # scene frame length
frame_rate = 4 # our target, autopilot, framerate. Usually it's 4 FPS.

blender_frame_rate = 24 # blender framerate
# iterate through every drone
for i in range(0, number_of_uavs):
    # get object in scene (from Spehre_0 to Sphere_19)
    ob = bpy.data.objects["Sphere.00" + str(i)]
    # create PATH file for every object
    file = open('/Users/smirart/Desktop/ROI/roi2-APM-' + str(i+1) + '.PATH', 'wb')
    # iterate through frames
    for f in range(sce.frame_start, scene_frames):
        # for every third frame get and save object position into file.
        # we should have 867 frames in output file
        if (((f-1) % (blender_frame_rate / frame_rate)) == 0):
            sce.frame_set(f)
            # get scaled position
            x = int(ob.matrix_world.to_translation().x * 100 * scale)
            y = int(ob.matrix_world.to_translation().y * 100 * scale)
            z = int(ob.matrix_world.to_translation().z * 100 * scale)
            # get color
            r = int(ob.active_material.diffuse_color.r * 255)
            g = int(ob.active_material.diffuse_color.g * 255)
            b = int(ob.active_material.diffuse_color.b * 255)
            file.write((x).to_bytes(2, byteorder='little', signed=True))
            file.write((y).to_bytes(2, byteorder='little', signed=True))
            file.write((z).to_bytes(2, byteorder='little', signed=True))
            file.write((r).to_bytes(2, byteorder='little', signed=True))
            file.write((g).to_bytes(2, byteorder='little', signed=True))
            file.write((b).to_bytes(2, byteorder='little', signed=True))
    file.close()
