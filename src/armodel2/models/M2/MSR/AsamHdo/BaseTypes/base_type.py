"""BaseType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 302)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 291)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2002)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_BaseTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.MSR.AsamHdo.BaseTypes.base_type_definition import (
    BaseTypeDefinition,
)
from armodel2.serialization import SerializationHelper


class BaseType(ARElement):
    """AUTOSAR BaseType."""
    """Abstract base class - do not instantiate directly."""

    _XML_TAG = "BASE-TYPE"

    _DESERIALIZE_DISPATCH = {
        "BASE-TYPE-SIZE": lambda obj, elem: setattr(
            obj.base_type_definition, 'base_type_size', elem.text
        ),
        "BASE-TYPE-ENCODING": lambda obj, elem: setattr(
            obj.base_type_definition, 'base_type_encoding', elem.text
        ),
        "MEM-ALIGNMENT": lambda obj, elem: setattr(
            obj.base_type_definition, 'mem_alignment', elem.text
        ),
        "BYTE-ORDER": lambda obj, elem: setattr(
            obj.base_type_definition, 'byte_order', elem.text
        ),
        "NATIVE-DECLARATION": lambda obj, elem: setattr(
            obj.base_type_definition, 'native', elem.text
        ),
    }

    base_type_definition: BaseTypeDefinition
    def __init__(self) -> None:
        """Initialize BaseType."""
        super().__init__()
        self.base_type_definition: BaseTypeDefinition = None

    def serialize(self) -> ET.Element:
        """Serialize BaseType to XML element with flat structure.

        Outputs BASE-TYPE-SIZE, BASE-TYPE-ENCODING, etc. as direct children
        instead of wrapping them in BASE-TYPE-DEFINITION element.

        Returns:
            xml.etree.ElementTree.Element representing this BaseType
        """
        from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

        # Call parent serialize for inherited fields (short_name, category, etc.)
        elem = super().serialize()

        # Remove the BASE-TYPE-DIRECT-DEFINITION element that parent added
        # (we want flat format instead)
        for child in list(elem):
            tag = SerializationHelper.strip_namespace(child.tag)
            if tag == 'BASE-TYPE-DIRECT-DEFINITION':
                elem.remove(child)

        # Flatten base_type_definition fields as direct children using pre-computed tags
        if self.base_type_definition is not None:
            defn = self.base_type_definition
            SerializationHelper.add_text_element(elem, 'BASE-TYPE-SIZE', getattr(defn, 'base_type_size', None))
            SerializationHelper.add_text_element(elem, 'BASE-TYPE-ENCODING', getattr(defn, 'base_type_encoding', None))
            SerializationHelper.add_text_element(elem, 'MEM-ALIGNMENT', getattr(defn, 'mem_alignment', None))
            SerializationHelper.add_text_element(elem, 'BYTE-ORDER', getattr(defn, 'byte_order', None))
            SerializationHelper.add_text_element(elem, 'NATIVE-DECLARATION', getattr(defn, 'native', None))

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BaseType":
        """Deserialize XML element to BaseType with flat structure.

        Uses static dispatch table for O(1) tag-to-handler lookup.
        Expects BASE-TYPE-SIZE, BASE-TYPE-ENCODING, etc. as direct children
        of the element (not wrapped in BASE-TYPE-DEFINITION).

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BaseType object
        """
        from armodel2.models.M2.MSR.AsamHdo.BaseTypes.base_type_direct_definition import BaseTypeDirectDefinition

        # Create object
        obj = cls.__new__(cls)
        obj.__init__()

        # Create BaseTypeDirectDefinition
        defn = BaseTypeDirectDefinition()
        obj.base_type_definition = defn

        # Process all children in a single pass
        for child in element:
            tag = child.tag.split('}', 1)[1] if child.tag.startswith('{') else child.tag

            # Check our dispatch table first for base_type_definition fields
            handler = cls._DESERIALIZE_DISPATCH.get(tag)
            if handler is not None:
                handler(obj, child)
                continue

            # Handle inherited fields using property setters
            if tag == "SHORT-NAME":
                obj.short_name = child.text
            elif tag == "LONG-NAME":
                from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import DocumentationBlock
                obj.long_name = DocumentationBlock.deserialize(child)
            elif tag == "DESC":
                from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import DocumentationBlock
                obj.desc = DocumentationBlock.deserialize(child)
            elif tag == "CATEGORY":
                obj.category = child.text
            elif tag == "CHECKSUM":
                obj.checksum = child.text
            elif tag == "ADMIN-DATA":
                # Handle admin data if needed
                pass

        # Handle XML attributes (timestamp)
        timestamp_str = element.get("T")
        if timestamp_str is not None:
            obj.timestamp = timestamp_str

        return obj


class BaseTypeBuilder:
    """Builder for BaseType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BaseType = BaseType()

    def build(self) -> BaseType:
        """Build and return BaseType object.

        Returns:
            BaseType instance
        """
        # TODO: Add validation
        return self._obj
