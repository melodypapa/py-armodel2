"""DdsDurability AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 530)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsDurabilityKindEnum,
)


class DdsDurability(ARObject):
    """AUTOSAR DdsDurability."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    durability_kind: Optional[DdsDurabilityKindEnum]
    def __init__(self) -> None:
        """Initialize DdsDurability."""
        super().__init__()
        self.durability_kind: Optional[DdsDurabilityKindEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsDurability to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsDurability, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize durability_kind
        if self.durability_kind is not None:
            serialized = SerializationHelper.serialize_item(self.durability_kind, "DdsDurabilityKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DURABILITY-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsDurability":
        """Deserialize XML element to DdsDurability object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsDurability object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsDurability, cls).deserialize(element)

        # Parse durability_kind
        child = SerializationHelper.find_child_element(element, "DURABILITY-KIND")
        if child is not None:
            durability_kind_value = DdsDurabilityKindEnum.deserialize(child)
            obj.durability_kind = durability_kind_value

        return obj



class DdsDurabilityBuilder:
    """Builder for DdsDurability."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsDurability = DdsDurability()

    def build(self) -> DdsDurability:
        """Build and return DdsDurability object.

        Returns:
            DdsDurability instance
        """
        # TODO: Add validation
        return self._obj
