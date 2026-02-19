"""LinFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 428)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class LinFrame(Frame, ABC):
    """AUTOSAR LinFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize LinFrame."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinFrame":
        """Deserialize XML element to LinFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinFrame object
        """
        # Delegate to parent class to handle inherited attributes
        return super(LinFrame, cls).deserialize(element)



class LinFrameBuilder:
    """Builder for LinFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinFrame = LinFrame()

    def build(self) -> LinFrame:
        """Build and return LinFrame object.

        Returns:
            LinFrame instance
        """
        # TODO: Add validation
        return self._obj
