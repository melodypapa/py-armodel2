"""BaseTypeDirectDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 302)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 290)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2002)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 29)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_BaseTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type_definition import (
    BaseTypeDefinition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NativeDeclarationString,
    PositiveInteger,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes import (
    BaseTypeEncodingString,
)


class BaseTypeDirectDefinition(BaseTypeDefinition):
    """AUTOSAR BaseTypeDirectDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_type_encoding: Optional[BaseTypeEncodingString]
    base_type_size: Optional[PositiveInteger]
    byte_order: Optional[ByteOrderEnum]
    mem_alignment: Optional[PositiveInteger]
    native: Optional[NativeDeclarationString]
    def __init__(self) -> None:
        """Initialize BaseTypeDirectDefinition."""
        super().__init__()
        self.base_type_encoding: Optional[BaseTypeEncodingString] = None
        self.base_type_size: Optional[PositiveInteger] = None
        self.byte_order: Optional[ByteOrderEnum] = None
        self.mem_alignment: Optional[PositiveInteger] = None
        self.native: Optional[NativeDeclarationString] = None
    def serialize(self) -> ET.Element:
        """Serialize BaseTypeDirectDefinition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BaseTypeDirectDefinition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_type_encoding
        if self.base_type_encoding is not None:
            serialized = ARObject._serialize_item(self.base_type_encoding, "BaseTypeEncodingString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-TYPE-ENCODING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize base_type_size
        if self.base_type_size is not None:
            serialized = ARObject._serialize_item(self.base_type_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-TYPE-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize byte_order
        if self.byte_order is not None:
            serialized = ARObject._serialize_item(self.byte_order, "ByteOrderEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BYTE-ORDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mem_alignment
        if self.mem_alignment is not None:
            serialized = ARObject._serialize_item(self.mem_alignment, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MEM-ALIGNMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize native
        if self.native is not None:
            serialized = ARObject._serialize_item(self.native, "NativeDeclarationString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NATIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BaseTypeDirectDefinition":
        """Deserialize XML element to BaseTypeDirectDefinition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BaseTypeDirectDefinition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BaseTypeDirectDefinition, cls).deserialize(element)

        # Parse base_type_encoding
        child = ARObject._find_child_element(element, "BASE-TYPE-ENCODING")
        if child is not None:
            base_type_encoding_value = child.text
            obj.base_type_encoding = base_type_encoding_value

        # Parse base_type_size
        child = ARObject._find_child_element(element, "BASE-TYPE-SIZE")
        if child is not None:
            base_type_size_value = child.text
            obj.base_type_size = base_type_size_value

        # Parse byte_order
        child = ARObject._find_child_element(element, "BYTE-ORDER")
        if child is not None:
            byte_order_value = ByteOrderEnum.deserialize(child)
            obj.byte_order = byte_order_value

        # Parse mem_alignment
        child = ARObject._find_child_element(element, "MEM-ALIGNMENT")
        if child is not None:
            mem_alignment_value = child.text
            obj.mem_alignment = mem_alignment_value

        # Parse native
        child = ARObject._find_child_element(element, "NATIVE")
        if child is not None:
            native_value = child.text
            obj.native = native_value

        return obj



class BaseTypeDirectDefinitionBuilder:
    """Builder for BaseTypeDirectDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BaseTypeDirectDefinition = BaseTypeDirectDefinition()

    def build(self) -> BaseTypeDirectDefinition:
        """Build and return BaseTypeDirectDefinition object.

        Returns:
            BaseTypeDirectDefinition instance
        """
        # TODO: Add validation
        return self._obj
