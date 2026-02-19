"""Ieee1722Tp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 460)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class Ieee1722Tp(TransportProtocolConfiguration):
    """AUTOSAR Ieee1722Tp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    relative: Optional[TimeValue]
    stream_identifier: Optional[PositiveInteger]
    sub_type: Optional[PositiveInteger]
    version: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize Ieee1722Tp."""
        super().__init__()
        self.relative: Optional[TimeValue] = None
        self.stream_identifier: Optional[PositiveInteger] = None
        self.sub_type: Optional[PositiveInteger] = None
        self.version: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ieee1722Tp":
        """Deserialize XML element to Ieee1722Tp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ieee1722Tp object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ieee1722Tp, cls).deserialize(element)

        # Parse relative
        child = ARObject._find_child_element(element, "RELATIVE")
        if child is not None:
            relative_value = child.text
            obj.relative = relative_value

        # Parse stream_identifier
        child = ARObject._find_child_element(element, "STREAM-IDENTIFIER")
        if child is not None:
            stream_identifier_value = child.text
            obj.stream_identifier = stream_identifier_value

        # Parse sub_type
        child = ARObject._find_child_element(element, "SUB-TYPE")
        if child is not None:
            sub_type_value = child.text
            obj.sub_type = sub_type_value

        # Parse version
        child = ARObject._find_child_element(element, "VERSION")
        if child is not None:
            version_value = child.text
            obj.version = version_value

        return obj



class Ieee1722TpBuilder:
    """Builder for Ieee1722Tp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ieee1722Tp = Ieee1722Tp()

    def build(self) -> Ieee1722Tp:
        """Build and return Ieee1722Tp object.

        Returns:
            Ieee1722Tp instance
        """
        # TODO: Add validation
        return self._obj
