class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        # Sort the list of folder paths to ensure that parent directories are before their subfolders
        folders.sort()
      
        # Initialize the result list with the first folder since it is guaranteed not to be a subfolder
        result = [folders[0]]
      
        # Iterate through the sorted folders starting from the second folder
        for folder in folders[1:]:
            last_added_folder_length = len(result[-1])  # Length of the last added folder to result
            current_folder_length = len(folder)         # Length of the current folder
          
            # Check if the current folder is not a subfolder of the last added folder
            # This is determined by checking if the last added folder does not match the prefix of the current folder and there is a '/' after the prefix
            if last_added_folder_length >= current_folder_length or not (result[-1] == folder[:last_added_folder_length] and folder[last_added_folder_length] == '/'):
                result.append(folder)  # The current folder is not a subfolder, so add it to the result
      
        # Return the list of folders without subfolders
        return result
