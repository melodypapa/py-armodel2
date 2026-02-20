"""TlvDataIdDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 830)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.argument_data_prototype import (
    ArgumentDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
        AbstractImplementationDataType,
    )



class TlvDataIdDefinition(ARObject):
    """AUTOSAR TlvDataIdDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    id: Optional[PositiveInteger]
    tlv_argument_ref: Optional[ARRef]
    tlv_ref: Optional[ARRef]
    tlv_record_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize TlvDataIdDefinition."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.tlv_argument_ref: Optional[ARRef] = None
        self.tlv_ref: Optional[ARRef] = None
        self.tlv_record_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TlvDataIdDefinition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize id
        if self.id is not None:
            serialized = ARObject._serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tlv_argument_ref
        if self.tlv_argument_ref is not None:
            serialized = ARObject._serialize_item(self.tlv_argument_ref, "ArgumentDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TLV-ARGUMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tlv_ref
        if self.tlv_ref is not None:
            serialized = ARObject._serialize_item(self.tlv_ref, "AbstractImplementationDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TLV-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tlv_record_ref
        if self.tlv_record_ref is not None:
            serialized = ARObject._serialize_item(self.tlv_record_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TLV-RECORD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlvDataIdDefinition":
        """Deserialize XML element to TlvDataIdDefinition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TlvDataIdDefinition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse id
        child = ARObject._find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse tlv_argument_ref
        child = ARObject._find_child_element(element, "TLV-ARGUMENT-REF")
        if child is not None:
            tlv_argument_ref_value = ARRef.deserialize(child)
            obj.tlv_argument_ref = tlv_argument_ref_value

        # Parse tlv_ref
        child = ARObject._find_child_element(element, "TLV-REF")
        if child is not None:
            tlv_ref_value = ARRef.deserialize(child)
            obj.tlv_ref = tlv_ref_value

        # Parse tlv_record_ref
        child = ARObject._find_child_element(element, "TLV-RECORD-REF")
        if child is not None:
            tlv_record_ref_value = ARRef.deserialize(child)
            obj.tlv_record_ref = tlv_record_ref_value

        return obj



class TlvDataIdDefinitionBuilder:
    """Builder for TlvDataIdDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TlvDataIdDefinition = TlvDataIdDefinition()

    def build(self) -> TlvDataIdDefinition:
        """Build and return TlvDataIdDefinition object.

        Returns:
            TlvDataIdDefinition instance
        """
        # TODO: Add validation
        return self._obj
