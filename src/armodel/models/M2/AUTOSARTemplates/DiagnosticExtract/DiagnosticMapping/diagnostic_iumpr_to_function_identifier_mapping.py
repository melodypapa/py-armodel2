"""DiagnosticIumprToFunctionIdentifierMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 265)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr import (
    DiagnosticIumpr,
)


class DiagnosticIumprToFunctionIdentifierMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticIumprToFunctionIdentifierMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    function_ref: Optional[Any]
    iumpr_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticIumprToFunctionIdentifierMapping."""
        super().__init__()
        self.function_ref: Optional[Any] = None
        self.iumpr_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticIumprToFunctionIdentifierMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticIumprToFunctionIdentifierMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize function_ref
        if self.function_ref is not None:
            serialized = SerializationHelper.serialize_item(self.function_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUNCTION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize iumpr_ref
        if self.iumpr_ref is not None:
            serialized = SerializationHelper.serialize_item(self.iumpr_ref, "DiagnosticIumpr")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IUMPR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIumprToFunctionIdentifierMapping":
        """Deserialize XML element to DiagnosticIumprToFunctionIdentifierMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIumprToFunctionIdentifierMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticIumprToFunctionIdentifierMapping, cls).deserialize(element)

        # Parse function_ref
        child = SerializationHelper.find_child_element(element, "FUNCTION-REF")
        if child is not None:
            function_ref_value = ARRef.deserialize(child)
            obj.function_ref = function_ref_value

        # Parse iumpr_ref
        child = SerializationHelper.find_child_element(element, "IUMPR-REF")
        if child is not None:
            iumpr_ref_value = ARRef.deserialize(child)
            obj.iumpr_ref = iumpr_ref_value

        return obj



class DiagnosticIumprToFunctionIdentifierMappingBuilder:
    """Builder for DiagnosticIumprToFunctionIdentifierMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIumprToFunctionIdentifierMapping = DiagnosticIumprToFunctionIdentifierMapping()

    def build(self) -> DiagnosticIumprToFunctionIdentifierMapping:
        """Build and return DiagnosticIumprToFunctionIdentifierMapping object.

        Returns:
            DiagnosticIumprToFunctionIdentifierMapping instance
        """
        # TODO: Add validation
        return self._obj
