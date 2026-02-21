"""EcucFunctionNameDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 65)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


@atp_variant()

class EcucFunctionNameDef(ARObject):
    """AUTOSAR EcucFunctionNameDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize EcucFunctionNameDef."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize EcucFunctionNameDef to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucFunctionNameDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "EcucFunctionNameDef")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucFunctionNameDef":
        """Deserialize XML element to EcucFunctionNameDef object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucFunctionNameDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucFunctionNameDef, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "EcucFunctionNameDef")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        return obj



class EcucFunctionNameDefBuilder:
    """Builder for EcucFunctionNameDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucFunctionNameDef = EcucFunctionNameDef()

    def build(self) -> EcucFunctionNameDef:
        """Build and return EcucFunctionNameDef object.

        Returns:
            EcucFunctionNameDef instance
        """
        # TODO: Add validation
        return self._obj
