# import unreal
import json
# import subprocess
import mayaShader
#
# file = r"C:/Users/fresh/PycharmProjects/unreal/mayaShader.py"
# # Run script2.py using the specified interpreter
# result = subprocess.Popen(['mayapy', file], stdout=subprocess.PIPE, text=True)
# stdout, stderr = result.communicate()

# Open ths exported JSON file containing the material from the Maya 
file_path = mayaShader.file_path


# Read the JSON file and load the data
with open(file_path, 'r') as json_file:
    materials = json.load(json_file)


# Define the material name and folder path
material_name = materials.keys()[0]
dest_path = '/Game/Materials'
material_path = dest_path + "/" + material_name
# ----------------------------------------------------------------------------------------------------------------------
# Import textures





# ----------------------------------------------------------------------------------------------------------------------

texture_path = '/Game/Textures/bark07'

# # Create new material - name, path, class, factory
# tools = unreal.AssetToolsHelpers.get_asset_tools()
# new_mat = tools.create_asset(material_name, dest_path, unreal.Material, unreal.MaterialFactoryNew())

# # Load asset as object
# texture = unreal.EditorAssetLibrary.load_asset(texture_path)

# # Create texture sampler - point to material. Material expression is the actual node being created
# texture_sampler = unreal.MaterialEditingLibrary.create_material_expression(new_mat, unreal.MaterialExpressionTextureSample, -200, -200)

# # Connect texture to texture sampler
# texture_sampler.texture = texture

# # Connect texture sampler 'RGB' channel to the base color channel of the material
# unreal.MaterialEditingLibrary.connect_material_property(texture_sampler, 'RGB', unreal.MaterialProperty.MP_BASE_COLOR)

# # Compile and save
# unreal.MaterialEditingLibrary.recompile_material(new_mat)
# unreal.EditorAssetLibrary.save_asset(material_path)
