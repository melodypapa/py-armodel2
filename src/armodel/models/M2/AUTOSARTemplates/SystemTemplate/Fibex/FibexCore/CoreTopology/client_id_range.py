"""ClientIdRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 52)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
)


class ClientIdRange(ARObject):
    """AUTOSAR ClientIdRange."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    lower_limit: Optional[Limit]
    upper_limit: Optional[Limit]
    def __init__(self) -> None:
        """Initialize ClientIdRange."""
        super().__init__()
        self.lower_limit: Optional[Limit] = None
        self.upper_limit: Optional[Limit] = None

    def serialize(self) -> ET.Element:
        """Serialize ClientIdRange to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientIdRange, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize lower_limit
        if self.lower_limit is not None:
            serialized = SerializationHelper.serialize_item(self.lower_limit, "Limit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-LIMIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_limit
        if self.upper_limit is not None:
            serialized = SerializationHelper.serialize_item(self.upper_limit, "Limit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-LIMIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientIdRange":
        """Deserialize XML element to ClientIdRange object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientIdRange object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientIdRange, cls).deserialize(element)

        # Parse lower_limit
        child = SerializationHelper.find_child_element(element, "LOWER-LIMIT")
        if child is not None:
            lower_limit_value = SerializationHelper.deserialize_by_tag(child, "Limit")
            obj.lower_limit = lower_limit_value

        # Parse upper_limit
        child = SerializationHelper.find_child_element(element, "UPPER-LIMIT")
        if child is not None:
            upper_limit_value = SerializationHelper.deserialize_by_tag(child, "Limit")
            obj.upper_limit = upper_limit_value

        return obj



class ClientIdRangeBuilder:
    """Builder for ClientIdRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientIdRange = ClientIdRange()

    def build(self) -> ClientIdRange:
        """Build and return ClientIdRange object.

        Returns:
            ClientIdRange instance
        """
        # TODO: Add validation
        return self._obj
