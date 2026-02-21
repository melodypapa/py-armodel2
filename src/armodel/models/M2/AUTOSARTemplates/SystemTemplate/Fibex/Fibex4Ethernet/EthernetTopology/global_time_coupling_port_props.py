"""GlobalTimeCouplingPortProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 875)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class GlobalTimeCouplingPortProps(ARObject):
    """AUTOSAR GlobalTimeCouplingPortProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    propagation: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize GlobalTimeCouplingPortProps."""
        super().__init__()
        self.propagation: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeCouplingPortProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeCouplingPortProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize propagation
        if self.propagation is not None:
            serialized = SerializationHelper.serialize_item(self.propagation, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROPAGATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeCouplingPortProps":
        """Deserialize XML element to GlobalTimeCouplingPortProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeCouplingPortProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeCouplingPortProps, cls).deserialize(element)

        # Parse propagation
        child = SerializationHelper.find_child_element(element, "PROPAGATION")
        if child is not None:
            propagation_value = child.text
            obj.propagation = propagation_value

        return obj



class GlobalTimeCouplingPortPropsBuilder:
    """Builder for GlobalTimeCouplingPortProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeCouplingPortProps = GlobalTimeCouplingPortProps()

    def build(self) -> GlobalTimeCouplingPortProps:
        """Build and return GlobalTimeCouplingPortProps object.

        Returns:
            GlobalTimeCouplingPortProps instance
        """
        # TODO: Add validation
        return self._obj
