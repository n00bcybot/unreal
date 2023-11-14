import os.path

import unreal
import json
# import subprocess
import numpy as np

#
# file = r"C:/Users/fresh/PycharmProjects/unreal/mayaShader.py"
# # Run script2.py using the specified interpreter
# result = subprocess.Popen(['mayapy', file], stdout=subprocess.PIPE, text=True)
# stdout, stderr = result.communicate()

# Open the exported JSON file containing the materials from the Maya scene
file_path = "C:/Users/fresh/Desktop/maya/rendertest/materials.json"

# Get texture paths
def getTexturePaths(materials_json):
    mat_paths_list = []
    for mesh in materials_json.values():
        material = mesh.values()
        paths_list = []
        for mat in material:
            texture = mat.values()
            paths = list(texture)
            for path in paths:
                paths_list.append(path['path'])
            mat_paths_list.append(paths_list)
    # np.unique looks into the list for repeating path and eliminates them

    return mat_paths_list



def getAttributes(materials_json):
    attr_list = []
    for mesh in materials_json.values():
        material = mesh.values()
        list1 = []
        for mat in material:
            attributes = list(mat.keys())
            list1.append(attributes)
        for attr in list1:
            attr_list.append(attr)

    return attr_list



def setConnection(type):
    return {
        'baseColor': 'RGB',
        'normalCamera': 'RGB',
        'specularRoughness': 'RGB'

    }[type]

# Read the JSON file and load the data
with open(file_path, 'r') as json_file:
    materials = json.load(json_file)

texture_paths = getTexturePaths(materials)
attributes = getAttributes(materials)

# Define the material name and folder path
material_name = list(materials.keys())
for name, paths_list, attr in zip(material_name, texture_paths, attributes):

    dest_path = '/Game/Assets/Materials/'
    material_path = dest_path + "/" + name

    # Create new material - name, path, class, factory
    tools = unreal.AssetToolsHelpers.get_asset_tools()
    new_mat = tools.create_asset(name, dest_path, unreal.Material, unreal.MaterialFactoryNew())


    for path, atr in zip(paths_list, attr):

        # Load asset as object
        texture = unreal.EditorAssetLibrary.load_asset('/Game/Assets/Textures/' + os.path.splitext(os.path.basename(path))[0])
        
        # Create texture sampler - point to material. Material expression is the actual node being created
        texture_sampler = unreal.MaterialEditingLibrary.create_material_expression(new_mat, unreal.MaterialExpressionTextureSample, 0, 0)

        if atr == 'baseColor':
            # Connect texture sampler 'RGB' channel to the base color channel of the material
            unreal.MaterialEditingLibrary.connect_material_property(texture_sampler, 'RGB', unreal.MaterialProperty.MP_BASE_COLOR)
            texture_sampler.texture = texture         
            
        elif atr == 'normalCamera':
            unreal.MaterialEditingLibrary.connect_material_property(texture_sampler, 'RGB', unreal.MaterialProperty.MP_NORMAL)
            texture_sampler.texture = texture
            texture_sampler.sampler_type = unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL
            
        elif atr == 'specularRoughness':
            unreal.MaterialEditingLibrary.connect_material_property(texture_sampler, 'RGB', unreal.MaterialProperty.MP_ROUGHNESS)
            texture_sampler.texture = texture
            
        # Compile and save
        unreal.MaterialEditingLibrary.recompile_material(new_mat)
        unreal.EditorAssetLibrary.save_asset(material_path)
