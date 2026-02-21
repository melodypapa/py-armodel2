"""DiagnosticClearResetEmissionRelatedInfo AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 154)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x04_ClearResetEmission.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticClearResetEmissionRelatedInfo(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticClearResetEmissionRelatedInfo."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    clear_reset_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticClearResetEmissionRelatedInfo."""
        super().__init__()
        self.clear_reset_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticClearResetEmissionRelatedInfo to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticClearResetEmissionRelatedInfo, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize clear_reset_ref
        if self.clear_reset_ref is not None:
            serialized = SerializationHelper.serialize_item(self.clear_reset_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLEAR-RESET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticClearResetEmissionRelatedInfo":
        """Deserialize XML element to DiagnosticClearResetEmissionRelatedInfo object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticClearResetEmissionRelatedInfo object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticClearResetEmissionRelatedInfo, cls).deserialize(element)

        # Parse clear_reset_ref
        child = SerializationHelper.find_child_element(element, "CLEAR-RESET-REF")
        if child is not None:
            clear_reset_ref_value = ARRef.deserialize(child)
            obj.clear_reset_ref = clear_reset_ref_value

        return obj



class DiagnosticClearResetEmissionRelatedInfoBuilder:
    """Builder for DiagnosticClearResetEmissionRelatedInfo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticClearResetEmissionRelatedInfo = DiagnosticClearResetEmissionRelatedInfo()

    def build(self) -> DiagnosticClearResetEmissionRelatedInfo:
        """Build and return DiagnosticClearResetEmissionRelatedInfo object.

        Returns:
            DiagnosticClearResetEmissionRelatedInfo instance
        """
        # TODO: Add validation
        return self._obj
