"""DiagnosticControlEnableMaskBit AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 119)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_IOControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)


class DiagnosticControlEnableMaskBit(ARObject):
    """AUTOSAR DiagnosticControlEnableMaskBit."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bit_number: Optional[PositiveInteger]
    controlled_data_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticControlEnableMaskBit."""
        super().__init__()
        self.bit_number: Optional[PositiveInteger] = None
        self.controlled_data_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticControlEnableMaskBit to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize bit_number
        if self.bit_number is not None:
            serialized = SerializationHelper.serialize_item(self.bit_number, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BIT-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize controlled_data_refs (list to container "CONTROLLED-DATA-REFS")
        if self.controlled_data_refs:
            wrapper = ET.Element("CONTROLLED-DATA-REFS")
            for item in self.controlled_data_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticDataElement")
                if serialized is not None:
                    child_elem = ET.Element("CONTROLLED-DATA-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticControlEnableMaskBit":
        """Deserialize XML element to DiagnosticControlEnableMaskBit object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticControlEnableMaskBit object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bit_number
        child = SerializationHelper.find_child_element(element, "BIT-NUMBER")
        if child is not None:
            bit_number_value = child.text
            obj.bit_number = bit_number_value

        # Parse controlled_data_refs (list from container "CONTROLLED-DATA-REFS")
        obj.controlled_data_refs = []
        container = SerializationHelper.find_child_element(element, "CONTROLLED-DATA-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.controlled_data_refs.append(child_value)

        return obj



class DiagnosticControlEnableMaskBitBuilder:
    """Builder for DiagnosticControlEnableMaskBit."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticControlEnableMaskBit = DiagnosticControlEnableMaskBit()

    def build(self) -> DiagnosticControlEnableMaskBit:
        """Build and return DiagnosticControlEnableMaskBit object.

        Returns:
            DiagnosticControlEnableMaskBit instance
        """
        # TODO: Add validation
        return self._obj
