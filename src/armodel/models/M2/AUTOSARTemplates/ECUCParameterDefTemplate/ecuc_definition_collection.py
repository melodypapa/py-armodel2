"""EcucDefinitionCollection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 25)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 185)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_module_def import (
    EcucModuleDef,
)


class EcucDefinitionCollection(ARElement):
    """AUTOSAR EcucDefinitionCollection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    modules: list[EcucModuleDef]
    def __init__(self) -> None:
        """Initialize EcucDefinitionCollection."""
        super().__init__()
        self.modules: list[EcucModuleDef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDefinitionCollection":
        """Deserialize XML element to EcucDefinitionCollection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDefinitionCollection object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse modules (list)
        obj.modules = []
        for child in ARObject._find_all_child_elements(element, "MODULES"):
            modules_value = ARObject._deserialize_by_tag(child, "EcucModuleDef")
            obj.modules.append(modules_value)

        return obj



class EcucDefinitionCollectionBuilder:
    """Builder for EcucDefinitionCollection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDefinitionCollection = EcucDefinitionCollection()

    def build(self) -> EcucDefinitionCollection:
        """Build and return EcucDefinitionCollection object.

        Returns:
            EcucDefinitionCollection instance
        """
        # TODO: Add validation
        return self._obj
