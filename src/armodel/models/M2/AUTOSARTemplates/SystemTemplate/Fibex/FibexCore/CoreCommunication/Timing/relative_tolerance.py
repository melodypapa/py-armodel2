"""RelativeTolerance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 398)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class RelativeTolerance(ARObject):
    """AUTOSAR RelativeTolerance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    relative: Optional[Integer]
    def __init__(self) -> None:
        """Initialize RelativeTolerance."""
        super().__init__()
        self.relative: Optional[Integer] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RelativeTolerance":
        """Deserialize XML element to RelativeTolerance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RelativeTolerance object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse relative
        child = ARObject._find_child_element(element, "RELATIVE")
        if child is not None:
            relative_value = child.text
            obj.relative = relative_value

        return obj



class RelativeToleranceBuilder:
    """Builder for RelativeTolerance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RelativeTolerance = RelativeTolerance()

    def build(self) -> RelativeTolerance:
        """Build and return RelativeTolerance object.

        Returns:
            RelativeTolerance instance
        """
        # TODO: Add validation
        return self._obj
