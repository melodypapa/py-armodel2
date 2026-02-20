"""TpAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 588)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class TpAddress(Identifiable):
    """AUTOSAR TpAddress."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_address: Optional[Integer]
    def __init__(self) -> None:
        """Initialize TpAddress."""
        super().__init__()
        self.tp_address: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize TpAddress to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TpAddress, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tp_address
        if self.tp_address is not None:
            serialized = ARObject._serialize_item(self.tp_address, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TpAddress":
        """Deserialize XML element to TpAddress object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TpAddress object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TpAddress, cls).deserialize(element)

        # Parse tp_address
        child = ARObject._find_child_element(element, "TP-ADDRESS")
        if child is not None:
            tp_address_value = child.text
            obj.tp_address = tp_address_value

        return obj



class TpAddressBuilder:
    """Builder for TpAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpAddress = TpAddress()

    def build(self) -> TpAddress:
        """Build and return TpAddress object.

        Returns:
            TpAddress instance
        """
        # TODO: Add validation
        return self._obj
