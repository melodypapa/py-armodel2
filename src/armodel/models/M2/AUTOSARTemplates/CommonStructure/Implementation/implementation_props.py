"""ImplementationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 86)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 287)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2033)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Implementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
)
from abc import ABC, abstractmethod


class ImplementationProps(Referrable, ABC):
    """AUTOSAR ImplementationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    symbol: Optional[CIdentifier]
    def __init__(self) -> None:
        """Initialize ImplementationProps."""
        super().__init__()
        self.symbol: Optional[CIdentifier] = None

    def serialize(self) -> ET.Element:
        """Serialize ImplementationProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ImplementationProps, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "ImplementationProps":
        """Deserialize XML element to ImplementationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ImplementationProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ImplementationProps, cls).deserialize(element)

        # Parse symbol
        child = SerializationHelper.find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = SerializationHelper.deserialize_by_tag(child, "CIdentifier")
            obj.symbol = symbol_value

        return obj



class ImplementationPropsBuilder:
    """Builder for ImplementationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationProps = ImplementationProps()

    def build(self) -> ImplementationProps:
        """Build and return ImplementationProps object.

        Returns:
            ImplementationProps instance
        """
        # TODO: Add validation
        return self._obj
