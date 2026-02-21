"""DiagnosticTroubleCodeUdsToTroubleCodeObdMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 188)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)


class DiagnosticTroubleCodeUdsToTroubleCodeObdMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticTroubleCodeUdsToTroubleCodeObdMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    trouble_code_ref: Optional[ARRef]
    trouble_code_uds_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeUdsToTroubleCodeObdMapping."""
        super().__init__()
        self.trouble_code_ref: Optional[ARRef] = None
        self.trouble_code_uds_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticTroubleCodeUdsToTroubleCodeObdMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticTroubleCodeUdsToTroubleCodeObdMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize trouble_code_ref
        if self.trouble_code_ref is not None:
            serialized = SerializationHelper.serialize_item(self.trouble_code_ref, "DiagnosticTroubleCode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TROUBLE-CODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trouble_code_uds_ref
        if self.trouble_code_uds_ref is not None:
            serialized = SerializationHelper.serialize_item(self.trouble_code_uds_ref, "DiagnosticTroubleCode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TROUBLE-CODE-UDS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping":
        """Deserialize XML element to DiagnosticTroubleCodeUdsToTroubleCodeObdMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTroubleCodeUdsToTroubleCodeObdMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticTroubleCodeUdsToTroubleCodeObdMapping, cls).deserialize(element)

        # Parse trouble_code_ref
        child = SerializationHelper.find_child_element(element, "TROUBLE-CODE-REF")
        if child is not None:
            trouble_code_ref_value = ARRef.deserialize(child)
            obj.trouble_code_ref = trouble_code_ref_value

        # Parse trouble_code_uds_ref
        child = SerializationHelper.find_child_element(element, "TROUBLE-CODE-UDS-REF")
        if child is not None:
            trouble_code_uds_ref_value = ARRef.deserialize(child)
            obj.trouble_code_uds_ref = trouble_code_uds_ref_value

        return obj



class DiagnosticTroubleCodeUdsToTroubleCodeObdMappingBuilder:
    """Builder for DiagnosticTroubleCodeUdsToTroubleCodeObdMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeUdsToTroubleCodeObdMapping = DiagnosticTroubleCodeUdsToTroubleCodeObdMapping()

    def build(self) -> DiagnosticTroubleCodeUdsToTroubleCodeObdMapping:
        """Build and return DiagnosticTroubleCodeUdsToTroubleCodeObdMapping object.

        Returns:
            DiagnosticTroubleCodeUdsToTroubleCodeObdMapping instance
        """
        # TODO: Add validation
        return self._obj
