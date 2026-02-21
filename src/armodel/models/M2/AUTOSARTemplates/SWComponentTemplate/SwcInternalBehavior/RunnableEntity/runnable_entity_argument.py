"""RunnableEntityArgument AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 536)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RunnableEntity.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
)


class RunnableEntityArgument(ARObject):
    """AUTOSAR RunnableEntityArgument."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    symbol: Optional[CIdentifier]
    def __init__(self) -> None:
        """Initialize RunnableEntityArgument."""
        super().__init__()
        self.symbol: Optional[CIdentifier] = None

    def serialize(self) -> ET.Element:
        """Serialize RunnableEntityArgument to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RunnableEntityArgument, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize symbol
        if self.symbol is not None:
            serialized = SerializationHelper.serialize_item(self.symbol, "CIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RunnableEntityArgument":
        """Deserialize XML element to RunnableEntityArgument object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RunnableEntityArgument object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RunnableEntityArgument, cls).deserialize(element)

        # Parse symbol
        child = SerializationHelper.find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = SerializationHelper.deserialize_by_tag(child, "CIdentifier")
            obj.symbol = symbol_value

        return obj



class RunnableEntityArgumentBuilder:
    """Builder for RunnableEntityArgument."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RunnableEntityArgument = RunnableEntityArgument()

    def build(self) -> RunnableEntityArgument:
        """Build and return RunnableEntityArgument object.

        Returns:
            RunnableEntityArgument instance
        """
        # TODO: Add validation
        return self._obj
