"""EcucInstanceReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 77)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_external_reference_def import (
    EcucAbstractExternalReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class EcucInstanceReferenceDef(EcucAbstractExternalReferenceDef):
    """AUTOSAR EcucInstanceReferenceDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination: Optional[String]
    destination_type: Optional[String]
    def __init__(self) -> None:
        """Initialize EcucInstanceReferenceDef."""
        super().__init__()
        self.destination: Optional[String] = None
        self.destination_type: Optional[String] = None
    def serialize(self) -> ET.Element:
        """Serialize EcucInstanceReferenceDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucInstanceReferenceDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination
        if self.destination is not None:
            serialized = ARObject._serialize_item(self.destination, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize destination_type
        if self.destination_type is not None:
            serialized = ARObject._serialize_item(self.destination_type, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucInstanceReferenceDef":
        """Deserialize XML element to EcucInstanceReferenceDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucInstanceReferenceDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucInstanceReferenceDef, cls).deserialize(element)

        # Parse destination
        child = ARObject._find_child_element(element, "DESTINATION")
        if child is not None:
            destination_value = child.text
            obj.destination = destination_value

        # Parse destination_type
        child = ARObject._find_child_element(element, "DESTINATION-TYPE")
        if child is not None:
            destination_type_value = child.text
            obj.destination_type = destination_type_value

        return obj



class EcucInstanceReferenceDefBuilder:
    """Builder for EcucInstanceReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucInstanceReferenceDef = EcucInstanceReferenceDef()

    def build(self) -> EcucInstanceReferenceDef:
        """Build and return EcucInstanceReferenceDef object.

        Returns:
            EcucInstanceReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
