"""CanFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 442)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class CanFrame(Frame):
    """AUTOSAR CanFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize CanFrame."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanFrame":
        """Deserialize XML element to CanFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanFrame object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class CanFrameBuilder:
    """Builder for CanFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanFrame = CanFrame()

    def build(self) -> CanFrame:
        """Build and return CanFrame object.

        Returns:
            CanFrame instance
        """
        # TODO: Add validation
        return self._obj
