"""FramePid AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 437)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
)


class FramePid(ARObject):
    """AUTOSAR FramePid."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    index: Optional[Integer]
    pid: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize FramePid."""
        super().__init__()
        self.index: Optional[Integer] = None
        self.pid: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FramePid":
        """Deserialize XML element to FramePid object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FramePid object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse index
        child = ARObject._find_child_element(element, "INDEX")
        if child is not None:
            index_value = child.text
            obj.index = index_value

        # Parse pid
        child = ARObject._find_child_element(element, "PID")
        if child is not None:
            pid_value = child.text
            obj.pid = pid_value

        return obj



class FramePidBuilder:
    """Builder for FramePid."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FramePid = FramePid()

    def build(self) -> FramePid:
        """Build and return FramePid object.

        Returns:
            FramePid instance
        """
        # TODO: Add validation
        return self._obj
