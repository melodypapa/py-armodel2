"""AsynchronousServerCallResultPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 304)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 581)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServerCall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class AsynchronousServerCallResultPoint(AbstractAccessPoint):
    """AUTOSAR AsynchronousServerCallResultPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    asynchronous_server: Optional[Any]
    def __init__(self) -> None:
        """Initialize AsynchronousServerCallResultPoint."""
        super().__init__()
        self.asynchronous_server: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AsynchronousServerCallResultPoint":
        """Deserialize XML element to AsynchronousServerCallResultPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AsynchronousServerCallResultPoint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse asynchronous_server
        child = ARObject._find_child_element(element, "ASYNCHRONOUS-SERVER")
        if child is not None:
            asynchronous_server_value = child.text
            obj.asynchronous_server = asynchronous_server_value

        return obj



class AsynchronousServerCallResultPointBuilder:
    """Builder for AsynchronousServerCallResultPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AsynchronousServerCallResultPoint = AsynchronousServerCallResultPoint()

    def build(self) -> AsynchronousServerCallResultPoint:
        """Build and return AsynchronousServerCallResultPoint object.

        Returns:
            AsynchronousServerCallResultPoint instance
        """
        # TODO: Add validation
        return self._obj
