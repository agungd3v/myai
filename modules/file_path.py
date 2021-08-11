import os, fnmatch

FILE_PATH = ["Documents", "Desktop", "Downloads", "Pictures", "Videos", "Music"]
ADD_SLASH = None

def findmyfiles(file, path):
  find = fnmatch.filter(os.listdir(path), file)
  finalresults = []
  while True:
    for trimpath in FILE_PATH:
      if len(find) < 1:
        try:
          ADD_SLASH = "/" + trimpath
          find = fnmatch.filter(os.listdir(path + ADD_SLASH), file)
          if len(find) > 0:
            return find
          elif FILE_PATH[-1] == trimpath:
            return []
        except Exception as e:
          continue
      else:
        for result in find:
          finalresults.append(path + ADD_SLASH + "/" + result)
        return finalresults
