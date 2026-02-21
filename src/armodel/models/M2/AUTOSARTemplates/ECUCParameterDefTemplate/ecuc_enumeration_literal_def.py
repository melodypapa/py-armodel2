"""EcucEnumerationLiteralDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 67)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class EcucEnumerationLiteralDef(Identifiable):
    """AUTOSAR EcucEnumerationLiteralDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecuc_cond: Optional[Any]
    origin: Optional[String]
    def __init__(self) -> None:
        """Initialize EcucEnumerationLiteralDef."""
        super().__init__()
        self.ecuc_cond: Optional[Any] = None
        self.origin: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucEnumerationLiteralDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucEnumerationLiteralDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecuc_cond
        if self.ecuc_cond is not None:
            serialized = ARObject._serialize_item(self.ecuc_cond, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECUC-COND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize origin
        if self.origin is not None:
            serialized = ARObject._serialize_item(self.origin, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ORIGIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucEnumerationLiteralDef":
        """Deserialize XML element to EcucEnumerationLiteralDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucEnumerationLiteralDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucEnumerationLiteralDef, cls).deserialize(element)

        # Parse ecuc_cond
        child = ARObject._find_child_element(element, "ECUC-COND")
        if child is not None:
            ecuc_cond_value = child.text
            obj.ecuc_cond = ecuc_cond_value

        # Parse origin
        child = ARObject._find_child_element(element, "ORIGIN")
        if child is not None:
            origin_value = child.text
            obj.origin = origin_value

        return obj



class EcucEnumerationLiteralDefBuilder:
    """Builder for EcucEnumerationLiteralDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucEnumerationLiteralDef = EcucEnumerationLiteralDef()

    def build(self) -> EcucEnumerationLiteralDef:
        """Build and return EcucEnumerationLiteralDef object.

        Returns:
            EcucEnumerationLiteralDef instance
        """
        # TODO: Add validation
        return self._obj
