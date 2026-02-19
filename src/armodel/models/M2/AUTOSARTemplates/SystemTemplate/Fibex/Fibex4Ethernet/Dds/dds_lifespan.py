"""DdsLifespan AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 536)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsLifespan(ARObject):
    """AUTOSAR DdsLifespan."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    lifespan_duration: Optional[Float]
    def __init__(self) -> None:
        """Initialize DdsLifespan."""
        super().__init__()
        self.lifespan_duration: Optional[Float] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsLifespan":
        """Deserialize XML element to DdsLifespan object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsLifespan object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse lifespan_duration
        child = ARObject._find_child_element(element, "LIFESPAN-DURATION")
        if child is not None:
            lifespan_duration_value = child.text
            obj.lifespan_duration = lifespan_duration_value

        return obj



class DdsLifespanBuilder:
    """Builder for DdsLifespan."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsLifespan = DdsLifespan()

    def build(self) -> DdsLifespan:
        """Build and return DdsLifespan object.

        Returns:
            DdsLifespan instance
        """
        # TODO: Add validation
        return self._obj
