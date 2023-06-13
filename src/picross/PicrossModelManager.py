import json
import os

import logging
LOGGER = logging.getLogger(__name__)

from .PicrossModel import PicrossModel


__all__ = ['PicrossModelManager']


class PicrossModelManager:

    def __init__(self, modelsFilePath: str) -> None:
        if not modelsFilePath.endswith('.json'):
            raise ValueError('Models file path must be a JSON file')
        
        if not os.path.exists(modelsFilePath) or os.path.getsize(modelsFilePath) == 0:
            LOGGER.warning(f'No models file found at "{modelsFilePath}", creating a new one')
            with open(modelsFilePath, 'w', encoding = 'utf-8') as f:
                json.dump([], f)
        
        self.__path = modelsFilePath


    def loadAll(self) -> list[PicrossModel]:
        with open(self.__path, 'r', encoding = 'utf-8') as f:
            models = json.load(f)

        return [PicrossModel.fromDictData(m['name'], m['grid']) for m in models]
    

    def load(self, name: str) -> PicrossModel:
        models = self.loadAll()
        for m in models:
            if m.name == name:
                return m
        
        raise ValueError(f'No model named "{name}" found')
        

    def save(self, model: PicrossModel, oldName: str = ...) -> None:
        models = self.loadAll()

        if oldName is ...:
            oldName = model.name
        
        found = False
        for m in models:
            if m.name == oldName:
                models.remove(m)
                found = True
                break
        
        models.append(model)

        with open(self.__path, 'w', encoding = 'utf-8') as f:
            json.dump([m.toDict() for m in models], f)
        
        if not found:
            LOGGER.warning(f'Model to replace "{oldName}" not found in models file')
        else:
            LOGGER.info(f'Model "{oldName}" overwritten in models file')
        LOGGER.info(f'Model "{model.name}" saved in models file')