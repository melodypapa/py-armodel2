"""DdsOwnership AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 532)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsOwnershipKindEnum,
)


class DdsOwnership(ARObject):
    """AUTOSAR DdsOwnership."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ownership_kind: Optional[DdsOwnershipKindEnum]
    def __init__(self) -> None:
        """Initialize DdsOwnership."""
        super().__init__()
        self.ownership_kind: Optional[DdsOwnershipKindEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsOwnership to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsOwnership, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ownership_kind
        if self.ownership_kind is not None:
            serialized = SerializationHelper.serialize_item(self.ownership_kind, "DdsOwnershipKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OWNERSHIP-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsOwnership":
        """Deserialize XML element to DdsOwnership object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsOwnership object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsOwnership, cls).deserialize(element)

        # Parse ownership_kind
        child = SerializationHelper.find_child_element(element, "OWNERSHIP-KIND")
        if child is not None:
            ownership_kind_value = DdsOwnershipKindEnum.deserialize(child)
            obj.ownership_kind = ownership_kind_value

        return obj



class DdsOwnershipBuilder:
    """Builder for DdsOwnership."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsOwnership = DdsOwnership()

    def build(self) -> DdsOwnership:
        """Build and return DdsOwnership object.

        Returns:
            DdsOwnership instance
        """
        # TODO: Add validation
        return self._obj
