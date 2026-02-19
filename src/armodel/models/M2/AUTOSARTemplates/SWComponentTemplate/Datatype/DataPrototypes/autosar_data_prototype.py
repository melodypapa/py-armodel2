"""AutosarDataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 305)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 301)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 306)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2001)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.autosar_data_type import (
    AutosarDataType,
)
from abc import ABC, abstractmethod


class AutosarDataPrototype(DataPrototype, ABC):
    """AUTOSAR AutosarDataPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    type: Optional[AutosarDataType]
    def __init__(self) -> None:
        """Initialize AutosarDataPrototype."""
        super().__init__()
        self.type: Optional[AutosarDataType] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AutosarDataPrototype":
        """Deserialize XML element to AutosarDataPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AutosarDataPrototype object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse type
        child = ARObject._find_child_element(element, "TYPE")
        if child is not None:
            type_value = ARObject._deserialize_by_tag(child, "AutosarDataType")
            obj.type = type_value

        return obj



class AutosarDataPrototypeBuilder:
    """Builder for AutosarDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarDataPrototype = AutosarDataPrototype()

    def build(self) -> AutosarDataPrototype:
        """Build and return AutosarDataPrototype object.

        Returns:
            AutosarDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
