"""DiagnosticSessionControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 93)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_SessionControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_session import (
    DiagnosticSession,
)


class DiagnosticSessionControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticSessionControl."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_session_session_ref: Optional[ARRef]
    session_control_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticSessionControl."""
        super().__init__()
        self.diagnostic_session_session_ref: Optional[ARRef] = None
        self.session_control_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticSessionControl to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticSessionControl, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diagnostic_session_session_ref
        if self.diagnostic_session_session_ref is not None:
            serialized = SerializationHelper.serialize_item(self.diagnostic_session_session_ref, "DiagnosticSession")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-SESSION-SESSION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize session_control_ref
        if self.session_control_ref is not None:
            serialized = SerializationHelper.serialize_item(self.session_control_ref, "DiagnosticSession")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SESSION-CONTROL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSessionControl":
        """Deserialize XML element to DiagnosticSessionControl object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSessionControl object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticSessionControl, cls).deserialize(element)

        # Parse diagnostic_session_session_ref
        child = SerializationHelper.find_child_element(element, "DIAGNOSTIC-SESSION-SESSION-REF")
        if child is not None:
            diagnostic_session_session_ref_value = ARRef.deserialize(child)
            obj.diagnostic_session_session_ref = diagnostic_session_session_ref_value

        # Parse session_control_ref
        child = SerializationHelper.find_child_element(element, "SESSION-CONTROL-REF")
        if child is not None:
            session_control_ref_value = ARRef.deserialize(child)
            obj.session_control_ref = session_control_ref_value

        return obj



class DiagnosticSessionControlBuilder:
    """Builder for DiagnosticSessionControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSessionControl = DiagnosticSessionControl()

    def build(self) -> DiagnosticSessionControl:
        """Build and return DiagnosticSessionControl object.

        Returns:
            DiagnosticSessionControl instance
        """
        # TODO: Add validation
        return self._obj
