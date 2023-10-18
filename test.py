import unreal
import os
import sys

# asset = unreal.EditorUtilityLibrary().get_selected_assets()
# asset = list(asset)
# print(asset[0].get_fname())

# asset2 = unreal.EditorActorSubsystem.get_fname(list(asset)[0])
# print(type(asset2))

asset_folder = 'C:\\Users\\fresh\\Desktop\\maya\\arctic'
asset_type = ['.fbx', '.exr']

#Check if the folder is correct
def checkFolderPath(directory):
    try:
        if not os.path.exists(directory) or not os.path.isdir(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist, or provided path is not directory.")
    except FileNotFoundError as exception:
        unreal.log_error(exception)
        sys.exit()
    else:
        pass
        

# Get assets to import. Set asset type by providing extension argument, or leave blank for all types:
# assets = getAssets(asset_folder, asset_type)
def getAssets(directory, extension=None):
    
    # Check path if the path is correct
    checkFolderPath(directory)

    # Go through all file in the directory. If extension type(s) is(are) provided, append only those files with such extension,
    # otherwise append all files in the directory to the list
    assets = {}
    for file in os.listdir(directory):
        if extension != None:
            for ext_type in extension:
                if file.endswith(ext_type):
                    assets[directory + '\\' + os.path.basename(file)] = ext_type
        else:
            assets[directory + '\\' + os.path.basename(file)] = os.path.splitext(file)[1]
    # return dict
    return assets

# Determine destination folder in the game, depending on the file type
def setDestination(type):
    return{
        '.fbx': '/Game/Assets/FBX',
        '.png': '/Game/Assets/textures',
        '.jpg': '/Game/Assets/textures',
        '.exr': '/Game/Assets/textures'
    }[type]

# Import assets' list

def createTask(destination_path, file_name):
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)
    task.set_editor_property('destination_name', '')
    task.set_editor_property('destination_path', destination_path)
    task.set_editor_property('filename', file_name)
    task.set_editor_property('replace_existing', True)
    task.set_editor_property('save', True)
    return task


def startImport():
    
    assets = getAssets(asset_folder, asset_type)
    task = []
    for file, destination in assets.items():
        task.append(createTask(setDestination(destination), file))
    # The actual method that performs the task. It take list.
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(task)
    
startImport()
