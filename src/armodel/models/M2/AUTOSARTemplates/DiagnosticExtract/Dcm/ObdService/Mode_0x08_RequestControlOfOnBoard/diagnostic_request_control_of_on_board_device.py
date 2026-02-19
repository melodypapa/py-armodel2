"""DiagnosticRequestControlOfOnBoardDevice AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 157)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x08_RequestControlOfOnBoard.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x08_RequestControlOfOnBoard.diagnostic_test_routine_identifier import (
    DiagnosticTestRoutineIdentifier,
)


class DiagnosticRequestControlOfOnBoardDevice(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestControlOfOnBoardDevice."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request_control: Optional[Any]
    test_id_identifier: Optional[DiagnosticTestRoutineIdentifier]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestControlOfOnBoardDevice."""
        super().__init__()
        self.request_control: Optional[Any] = None
        self.test_id_identifier: Optional[DiagnosticTestRoutineIdentifier] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestControlOfOnBoardDevice to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestControlOfOnBoardDevice, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize request_control
        if self.request_control is not None:
            serialized = ARObject._serialize_item(self.request_control, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-CONTROL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize test_id_identifier
        if self.test_id_identifier is not None:
            serialized = ARObject._serialize_item(self.test_id_identifier, "DiagnosticTestRoutineIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TEST-ID-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestControlOfOnBoardDevice":
        """Deserialize XML element to DiagnosticRequestControlOfOnBoardDevice object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestControlOfOnBoardDevice object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRequestControlOfOnBoardDevice, cls).deserialize(element)

        # Parse request_control
        child = ARObject._find_child_element(element, "REQUEST-CONTROL")
        if child is not None:
            request_control_value = child.text
            obj.request_control = request_control_value

        # Parse test_id_identifier
        child = ARObject._find_child_element(element, "TEST-ID-IDENTIFIER")
        if child is not None:
            test_id_identifier_value = ARObject._deserialize_by_tag(child, "DiagnosticTestRoutineIdentifier")
            obj.test_id_identifier = test_id_identifier_value

        return obj



class DiagnosticRequestControlOfOnBoardDeviceBuilder:
    """Builder for DiagnosticRequestControlOfOnBoardDevice."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestControlOfOnBoardDevice = DiagnosticRequestControlOfOnBoardDevice()

    def build(self) -> DiagnosticRequestControlOfOnBoardDevice:
        """Build and return DiagnosticRequestControlOfOnBoardDevice object.

        Returns:
            DiagnosticRequestControlOfOnBoardDevice instance
        """
        # TODO: Add validation
        return self._obj
