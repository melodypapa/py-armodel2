"""RequestResponseDelay AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 515)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class RequestResponseDelay(ARObject):
    """AUTOSAR RequestResponseDelay."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_value: Optional[TimeValue]
    min_value: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize RequestResponseDelay."""
        super().__init__()
        self.max_value: Optional[TimeValue] = None
        self.min_value: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RequestResponseDelay":
        """Deserialize XML element to RequestResponseDelay object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RequestResponseDelay object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse max_value
        child = ARObject._find_child_element(element, "MAX-VALUE")
        if child is not None:
            max_value_value = child.text
            obj.max_value = max_value_value

        # Parse min_value
        child = ARObject._find_child_element(element, "MIN-VALUE")
        if child is not None:
            min_value_value = child.text
            obj.min_value = min_value_value

        return obj



class RequestResponseDelayBuilder:
    """Builder for RequestResponseDelay."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RequestResponseDelay = RequestResponseDelay()

    def build(self) -> RequestResponseDelay:
        """Build and return RequestResponseDelay object.

        Returns:
            RequestResponseDelay instance
        """
        # TODO: Add validation
        return self._obj
