"""EthernetPriorityRegeneration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 128)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class EthernetPriorityRegeneration(Referrable):
    """AUTOSAR EthernetPriorityRegeneration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ingress_priority: Optional[PositiveInteger]
    regenerated: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize EthernetPriorityRegeneration."""
        super().__init__()
        self.ingress_priority: Optional[PositiveInteger] = None
        self.regenerated: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize EthernetPriorityRegeneration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthernetPriorityRegeneration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ingress_priority
        if self.ingress_priority is not None:
            serialized = SerializationHelper.serialize_item(self.ingress_priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INGRESS-PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize regenerated
        if self.regenerated is not None:
            serialized = SerializationHelper.serialize_item(self.regenerated, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REGENERATED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetPriorityRegeneration":
        """Deserialize XML element to EthernetPriorityRegeneration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetPriorityRegeneration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthernetPriorityRegeneration, cls).deserialize(element)

        # Parse ingress_priority
        child = SerializationHelper.find_child_element(element, "INGRESS-PRIORITY")
        if child is not None:
            ingress_priority_value = child.text
            obj.ingress_priority = ingress_priority_value

        # Parse regenerated
        child = SerializationHelper.find_child_element(element, "REGENERATED")
        if child is not None:
            regenerated_value = child.text
            obj.regenerated = regenerated_value

        return obj



class EthernetPriorityRegenerationBuilder:
    """Builder for EthernetPriorityRegeneration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetPriorityRegeneration = EthernetPriorityRegeneration()

    def build(self) -> EthernetPriorityRegeneration:
        """Build and return EthernetPriorityRegeneration object.

        Returns:
            EthernetPriorityRegeneration instance
        """
        # TODO: Add validation
        return self._obj
