"""AliasNameSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 174)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 968)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.alias_name_assignment import (
    AliasNameAssignment,
)


class AliasNameSet(ARElement):
    """AUTOSAR AliasNameSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    alias_names: list[AliasNameAssignment]
    def __init__(self) -> None:
        """Initialize AliasNameSet."""
        super().__init__()
        self.alias_names: list[AliasNameAssignment] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AliasNameSet":
        """Deserialize XML element to AliasNameSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AliasNameSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse alias_names (list)
        obj.alias_names = []
        for child in ARObject._find_all_child_elements(element, "ALIAS-NAMES"):
            alias_names_value = ARObject._deserialize_by_tag(child, "AliasNameAssignment")
            obj.alias_names.append(alias_names_value)

        return obj



class AliasNameSetBuilder:
    """Builder for AliasNameSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AliasNameSet = AliasNameSet()

    def build(self) -> AliasNameSet:
        """Build and return AliasNameSet object.

        Returns:
            AliasNameSet instance
        """
        # TODO: Add validation
        return self._obj
