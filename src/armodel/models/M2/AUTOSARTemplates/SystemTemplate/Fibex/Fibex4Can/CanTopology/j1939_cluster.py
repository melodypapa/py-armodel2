"""J1939Cluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 321)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 78)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


@atp_variant()

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
        """Serialize J1939Cluster to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939Cluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize network_id
        if self.network_id is not None:
            serialized = SerializationHelper.serialize_item(self.network_id, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("NETWORK-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize request2_support
        if self.request2_support is not None:
            serialized = SerializationHelper.serialize_item(self.request2_support, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("REQUEST2-SUPPORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize uses_address
        if self.uses_address is not None:
            serialized = SerializationHelper.serialize_item(self.uses_address, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("USES-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "J1939Cluster")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939Cluster":
        """Deserialize XML element to J1939Cluster object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939Cluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939Cluster, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "J1939Cluster")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse network_id
        child = SerializationHelper.find_child_element(inner_elem, "NETWORK-ID")
        if child is not None:
            network_id_value = child.text
            obj.network_id = network_id_value

        # Parse request2_support
        child = SerializationHelper.find_child_element(inner_elem, "REQUEST2-SUPPORT")
        if child is not None:
            request2_support_value = child.text
            obj.request2_support = request2_support_value

        # Parse uses_address
        child = SerializationHelper.find_child_element(inner_elem, "USES-ADDRESS")
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
