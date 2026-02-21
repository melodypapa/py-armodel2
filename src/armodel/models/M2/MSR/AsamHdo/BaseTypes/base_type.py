"""BaseType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 302)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 291)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2002)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_BaseTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type_definition import (
    BaseTypeDefinition,
)
from armodel.serialization import SerializationHelper


class BaseType(ARElement):
    """AUTOSAR BaseType."""
    """Abstract base class - do not instantiate directly."""

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
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

        # Call parent serialize for inherited fields (short_name, category, etc.)
        elem = super().serialize()

        # Remove the BASE-TYPE-DIRECT-DEFINITION element that parent added
        # (we want flat format instead)
        for child in list(elem):
            tag = SerializationHelper.strip_namespace(child.tag)
            if tag == 'BASE-TYPE-DIRECT-DEFINITION':
                elem.remove(child)

        # Flatten base_type_definition fields as direct children
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

        Expects BASE-TYPE-SIZE, BASE-TYPE-ENCODING, etc. as direct children
        of the element (not wrapped in BASE-TYPE-DEFINITION).

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BaseType object
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
        from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type_direct_definition import BaseTypeDirectDefinition

        # Use parent's standard deserialize for common fields (short_name, category, etc.)
        obj = super(BaseType, cls).deserialize(element)

        # Create BaseTypeDirectDefinition and populate from direct children
        # Using _extract_text with tag parameter for namespace-aware element finding
        defn = BaseTypeDirectDefinition()
        defn.base_type_size = SerializationHelper.extract_text(element, 'BASE-TYPE-SIZE')
        defn.base_type_encoding = SerializationHelper.extract_text(element, 'BASE-TYPE-ENCODING')
        defn.mem_alignment = SerializationHelper.extract_text(element, 'MEM-ALIGNMENT')
        defn.byte_order = SerializationHelper.extract_text(element, 'BYTE-ORDER')
        defn.native = SerializationHelper.extract_text(element, 'NATIVE-DECLARATION')

        obj.base_type_definition = defn

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
