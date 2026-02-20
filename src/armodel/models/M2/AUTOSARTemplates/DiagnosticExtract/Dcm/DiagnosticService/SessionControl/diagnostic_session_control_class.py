"""DiagnosticSessionControlClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 93)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_SessionControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class DiagnosticSessionControlClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticSessionControlClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    s3_server: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize DiagnosticSessionControlClass."""
        super().__init__()
        self.s3_server: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticSessionControlClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticSessionControlClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize s3_server
        if self.s3_server is not None:
            serialized = ARObject._serialize_item(self.s3_server, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("S3-SERVER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSessionControlClass":
        """Deserialize XML element to DiagnosticSessionControlClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSessionControlClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticSessionControlClass, cls).deserialize(element)

        # Parse s3_server
        child = ARObject._find_child_element(element, "S3-SERVER")
        if child is not None:
            s3_server_value = child.text
            obj.s3_server = s3_server_value

        return obj



class DiagnosticSessionControlClassBuilder:
    """Builder for DiagnosticSessionControlClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSessionControlClass = DiagnosticSessionControlClass()

    def build(self) -> DiagnosticSessionControlClass:
        """Build and return DiagnosticSessionControlClass object.

        Returns:
            DiagnosticSessionControlClass instance
        """
        # TODO: Add validation
        return self._obj
