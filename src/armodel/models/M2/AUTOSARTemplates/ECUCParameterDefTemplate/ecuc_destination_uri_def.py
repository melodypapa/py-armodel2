"""EcucDestinationUriDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class EcucDestinationUriDef(Identifiable):
    """AUTOSAR EcucDestinationUriDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination_uri: Optional[Any]
    def __init__(self) -> None:
        """Initialize EcucDestinationUriDef."""
        super().__init__()
        self.destination_uri: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucDestinationUriDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucDestinationUriDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_uri
        if self.destination_uri is not None:
            serialized = SerializationHelper.serialize_item(self.destination_uri, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION-URI")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDestinationUriDef":
        """Deserialize XML element to EcucDestinationUriDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDestinationUriDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucDestinationUriDef, cls).deserialize(element)

        # Parse destination_uri
        child = SerializationHelper.find_child_element(element, "DESTINATION-URI")
        if child is not None:
            destination_uri_value = child.text
            obj.destination_uri = destination_uri_value

        return obj



class EcucDestinationUriDefBuilder:
    """Builder for EcucDestinationUriDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDestinationUriDef = EcucDestinationUriDef()

    def build(self) -> EcucDestinationUriDef:
        """Build and return EcucDestinationUriDef object.

        Returns:
            EcucDestinationUriDef instance
        """
        # TODO: Add validation
        return self._obj
