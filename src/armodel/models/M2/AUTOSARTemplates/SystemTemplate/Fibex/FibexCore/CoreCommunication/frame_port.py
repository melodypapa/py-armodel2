"""FramePort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 304)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class FramePort(CommConnectorPort):
    """AUTOSAR FramePort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize FramePort."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FramePort":
        """Deserialize XML element to FramePort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FramePort object
        """
        # Delegate to parent class to handle inherited attributes
        return super(FramePort, cls).deserialize(element)



class FramePortBuilder:
    """Builder for FramePort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FramePort = FramePort()

    def build(self) -> FramePort:
        """Build and return FramePort object.

        Returns:
            FramePort instance
        """
        # TODO: Add validation
        return self._obj
