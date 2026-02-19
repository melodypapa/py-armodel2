"""J1939Cluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 321)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 78)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class J1939Cluster(ARObject):
    """AUTOSAR J1939Cluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    network_id: Optional[PositiveInteger]
    request2_support: Optional[Boolean]
    uses_address: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize J1939Cluster."""
        super().__init__()
        self.network_id: Optional[PositiveInteger] = None
        self.request2_support: Optional[Boolean] = None
        self.uses_address: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize J1939Cluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize network_id
        if self.network_id is not None:
            serialized = ARObject._serialize_item(self.network_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize request2_support
        if self.request2_support is not None:
            serialized = ARObject._serialize_item(self.request2_support, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST2-SUPPORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize uses_address
        if self.uses_address is not None:
            serialized = ARObject._serialize_item(self.uses_address, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USES-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939Cluster":
        """Deserialize XML element to J1939Cluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939Cluster object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse network_id
        child = ARObject._find_child_element(element, "NETWORK-ID")
        if child is not None:
            network_id_value = child.text
            obj.network_id = network_id_value

        # Parse request2_support
        child = ARObject._find_child_element(element, "REQUEST2-SUPPORT")
        if child is not None:
            request2_support_value = child.text
            obj.request2_support = request2_support_value

        # Parse uses_address
        child = ARObject._find_child_element(element, "USES-ADDRESS")
        if child is not None:
            uses_address_value = child.text
            obj.uses_address = uses_address_value

        return obj



class J1939ClusterBuilder:
    """Builder for J1939Cluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939Cluster = J1939Cluster()

    def build(self) -> J1939Cluster:
        """Build and return J1939Cluster object.

        Returns:
            J1939Cluster instance
        """
        # TODO: Add validation
        return self._obj
