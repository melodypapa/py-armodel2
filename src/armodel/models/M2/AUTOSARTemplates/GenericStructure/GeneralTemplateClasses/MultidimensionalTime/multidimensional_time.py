"""MultidimensionalTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 164)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 109)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 165)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_MultidimensionalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Integer,
)


class MultidimensionalTime(ARObject):
    """AUTOSAR MultidimensionalTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cse_code: Optional[CseCodeType]
    cse_code_factor: Optional[Integer]
    def __init__(self) -> None:
        """Initialize MultidimensionalTime."""
        super().__init__()
        self.cse_code: Optional[CseCodeType] = None
        self.cse_code_factor: Optional[Integer] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultidimensionalTime":
        """Deserialize XML element to MultidimensionalTime object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultidimensionalTime object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse cse_code
        child = ARObject._find_child_element(element, "CSE-CODE")
        if child is not None:
            cse_code_value = child.text
            obj.cse_code = cse_code_value

        # Parse cse_code_factor
        child = ARObject._find_child_element(element, "CSE-CODE-FACTOR")
        if child is not None:
            cse_code_factor_value = child.text
            obj.cse_code_factor = cse_code_factor_value

        return obj



class MultidimensionalTimeBuilder:
    """Builder for MultidimensionalTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultidimensionalTime = MultidimensionalTime()

    def build(self) -> MultidimensionalTime:
        """Build and return MultidimensionalTime object.

        Returns:
            MultidimensionalTime instance
        """
        # TODO: Add validation
        return self._obj
