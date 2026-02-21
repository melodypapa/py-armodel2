"""DdsLiveliness AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 534)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsLivenessKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsLiveliness(ARObject):
    """AUTOSAR DdsLiveliness."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    liveliness_lease: Optional[Float]
    liveness_kind: Optional[DdsLivenessKindEnum]
    def __init__(self) -> None:
        """Initialize DdsLiveliness."""
        super().__init__()
        self.liveliness_lease: Optional[Float] = None
        self.liveness_kind: Optional[DdsLivenessKindEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsLiveliness to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsLiveliness, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize liveliness_lease
        if self.liveliness_lease is not None:
            serialized = SerializationHelper.serialize_item(self.liveliness_lease, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LIVELINESS-LEASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize liveness_kind
        if self.liveness_kind is not None:
            serialized = SerializationHelper.serialize_item(self.liveness_kind, "DdsLivenessKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LIVENESS-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsLiveliness":
        """Deserialize XML element to DdsLiveliness object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsLiveliness object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsLiveliness, cls).deserialize(element)

        # Parse liveliness_lease
        child = SerializationHelper.find_child_element(element, "LIVELINESS-LEASE")
        if child is not None:
            liveliness_lease_value = child.text
            obj.liveliness_lease = liveliness_lease_value

        # Parse liveness_kind
        child = SerializationHelper.find_child_element(element, "LIVENESS-KIND")
        if child is not None:
            liveness_kind_value = DdsLivenessKindEnum.deserialize(child)
            obj.liveness_kind = liveness_kind_value

        return obj



class DdsLivelinessBuilder:
    """Builder for DdsLiveliness."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsLiveliness = DdsLiveliness()

    def build(self) -> DdsLiveliness:
        """Build and return DdsLiveliness object.

        Returns:
            DdsLiveliness instance
        """
        # TODO: Add validation
        return self._obj
