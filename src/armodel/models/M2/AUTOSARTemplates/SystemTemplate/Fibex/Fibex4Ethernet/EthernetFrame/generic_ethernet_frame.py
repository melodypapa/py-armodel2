"""GenericEthernetFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 578)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetFrame.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame.abstract_ethernet_frame import (
    AbstractEthernetFrame,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class GenericEthernetFrame(AbstractEthernetFrame):
    """AUTOSAR GenericEthernetFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize GenericEthernetFrame."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "GenericEthernetFrame":
        """Deserialize XML element to GenericEthernetFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GenericEthernetFrame object
        """
        # Delegate to parent class to handle inherited attributes
        return super(GenericEthernetFrame, cls).deserialize(element)



class GenericEthernetFrameBuilder:
    """Builder for GenericEthernetFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GenericEthernetFrame = GenericEthernetFrame()

    def build(self) -> GenericEthernetFrame:
        """Build and return GenericEthernetFrame object.

        Returns:
            GenericEthernetFrame instance
        """
        # TODO: Add validation
        return self._obj
